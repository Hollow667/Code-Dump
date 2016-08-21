from datetime import datetime, timedelta
from gi import require_version
require_version('Notify', '0.7')
from gi.repository import Notify
import sys

class State:
    #length: the length of the state in minutes
    def __init__(self, length):
        if not length == None:
            self.length = length

class Clock:
    work = None
    sBreak = None
    lBreak = None

    numWork = 4
    remWork = numWork #number of work sessions remaining
    remBreaks = numWork - 1 #number of short break sessions remaining
    current = None #the current state
    endtime = None #datetime object for end time of current

    def __init__(self, workTime, sBreakTime, lBreakTime):
        if workTime == None or sBreakTime == None or lBreakTime == None:
            exit(1)
        self.work = State(workTime)
        self.sBreak = State(sBreakTime)
        self.lBreak = State(lBreakTime)
        self.states = [self.work, self.sBreak, self.lBreak]

    def change(self):
        if not self.current == None and not self.current in self.states:
            exit(1)

        title = ''
        timeStr = 'End Time: '

        #current doesn't exist: start the first work period
        if self.current == None:
            self.current = self.work
            title = 'Work Period'

        #in work state now: either short or long break
        elif self.current == self.work:
            self.remWork -= 1
            if self.remBreaks == 0:
                self.current = self.lBreak
                title = 'Long Break'
            else:
                self.current = self.sBreak
                title = 'Short Break'
        #in short break now: start work
        elif self.current == self.sBreak:
            self.remBreaks -= 1
            self.current = self.work
            title = 'Work Period'
        #in long break now: reset number of work and short break periods
        elif self.current == self.lBreak:
            self.current = self.work
            title = 'Work Period'
            self.remWork = self.numWork
            self.remBreaks = self.numWork - 1
        self.endtime = datetime.now() + timedelta(seconds = self.current.length)
        timeStr +=  self.endtime.strftime("%H:%M")
        Notify.init("a")
        notifyme=Notify.Notification.new(title,timeStr)
        notifyme.show()

    def tickTock(self):
        self.change()
        while True:
            if datetime.now() >= self.endtime:
                self.change()

def main():
    try:
        lengths = sys.argv[1:]
        workLen = int(lengths[0])
        sbLen = int(lengths[1])
        lbLen = int(lengths[2])

        clock = Clock(workLen, sbLen, lbLen)
        clock.tickTock()
    except:
        print("One or more arguments were invalid.")
        exit(1)

if __name__ == '__main__':
