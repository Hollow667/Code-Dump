import sys
import chilkat

chilkatGlob = chilkat.CkGlobal()
success = chilkatGlob.UnlockBundle("Anything for 30-day trial.")
if (success != True):
    print(chilkatGlob.lastErrorText())
    sys.exit()

tunnel = chilkat.CkSshTunnel()

sshHostname = "www.my-ssh-server.com"
sshPort = 22

#  Connect to an SSH server and establish the SSH tunnel:
success = tunnel.Connect(sshHostname,sshPort)
if (success != True):
    print(tunnel.lastErrorText())
    sys.exit()

#  Authenticate with the SSH server via a login/password
#  or with a public key.
#  This example demonstrates SSH password authentication.
success = tunnel.AuthenticatePw("mySshLogin","mySshPassword")
if (success != True):
    print(tunnel.lastErrorText())
    sys.exit()

#  The destination host/port is the database server.
#  The DestHostname may be the domain name or
#  IP address (in dotted decimal notation) of the database
#  server.
tunnel.put_DestPort(1433)
tunnel.put_DestHostname("myDbServer.com")

#  Start accepting connections in a background thread.
#  The SSH tunnels are autonomously run in a background
#  thread.  There is one background thread for accepting
#  connections, and another for managing the tunnel pool.
listenPort = 3316
success = tunnel.BeginAccepting(listenPort)
if (success != True):
    print(tunnel.lastErrorText())
    sys.exit()

#  At this point the app may connect to the database server through
#  the SSH tunnel.  The database connection string would
#  use "localhost" for the hostname and 3316 for the port.
#  We're not going to show the database coding here,
#  because it can vary depending on the API you're using
#  (ADO, ODBC, OLE DB, etc. )

#  This is where the application's database code would go...

#  Stop the background listen/accept thread:
waitForThreadExit = True
success = tunnel.StopAccepting(waitForThreadExit)
if (success != True):
    print(tunnel.lastErrorText())
    sys.exit()

#  Close the SSH tunnel (would also kick any remaining connected clients).
success = tunnel.CloseTunnel(waitForThreadExit)
if (success != True):
    print(tunnel.lastErrorText())
    sys.exit()
