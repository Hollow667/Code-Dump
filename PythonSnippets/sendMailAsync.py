
import sys
import chilkat

#  The mailman object is used for sending and receiving email.
mailman = chilkat.CkMailMan()

#  Any string argument automatically begins the 30-day trial.
success = mailman.UnlockComponent("30-day trial")
if (success != True):
    print(mailman.lastErrorText())
    sys.exit()

#  Set the SMTP server and any required settings.
mailman.put_SmtpHost("smtp.mymailserver.com")
mailman.put_SmtpUsername("myLogin")
mailman.put_SmtpPassword("myPassword")
mailman.put_StartTLS(True)

#  Create a new email object
email = chilkat.CkEmail()

email.put_Subject("This is a test")
email.put_Body("This is a test")
email.put_From("Chilkat Support <support@chilkatsoft.com>")
success = email.AddTo("Chilkat Admin","admin@chilkatsoft.com")

#  Call the async version of the SendEmail method to return a task object.
#  The task object is loaded, but is in the Inert state -- meaning it is
#  not yet scheduled to run on Chilkat's background thread pool.
# task is a CkTask
task = mailman.SendEmailAsync(email)
if (task == None ):
    print(mailman.lastErrorText())
    sys.exit()

#  Schedule the task for running on the thread pool.  This changes the task's state
#  from Inert to Live.
success = task.Run()
if (success != True):
    print(task.lastErrorText())

    sys.exit()

#  The application is now free to do anything else
#  while the email is being sent.

#  For this example, we'll simply sleep and periodically
#  check to see if the SendEmail if finished.  While checking
#  however, we'll report on the progress.
curPctDone = 0
while task.get_Finished() != True :

    if (task.get_PercentDone() != curPctDone):
        curPctDone = task.get_PercentDone()
        print(str(curPctDone) + " percent done")

    #  Sleep 100 ms.
    task.SleepMs(100)

#  A finished task could be one that was canceled, aborted, or truly finished.

#  If the task was "canceled", it was canceled prior to actually starting.  This could
#  happen if the task was canceled while waiting in a thread pool queue to be scheduled by Chilkat's
#  background thread pool scheduler.

#  If the task was "aborted", it indicates that it was canceled while running in a background thread.
#  The ResultErrorText will likely indicate that the task was aborted.

#  If the task "completed", then it ran to completion, but the actual success/failure of the method
#  is determined by the result obtained via a GetResult* method.  (A "completed" task will
#  have a StatusInt equal to 7.   If the task finished, but was not completed, then it must've
#  been aborted or canceled:
if (task.get_StatusInt() != 7):
    print("Task did not complete.")
    print("task status: " + task.status())

    sys.exit()

#  The SendEmail method returns a boolean.  Therefore, after the task is finished,
#  we can get the boolean result by calling GetResultBool.  This is the return value had
#  we called SendEmail synchronously.
success = task.GetResultBool()
if (success != True):
    #  The task's ResultErrorText contains what would have been in the LastErrorText property had
    #  the SendEmail method been called synchronously.
    print(task.resultErrorText())
else:
    print("Email sent asynchronously.")

success = mailman.CloseSmtpConnection()
if (success != True):
    print("Connection to SMTP server not closed cleanly.")
