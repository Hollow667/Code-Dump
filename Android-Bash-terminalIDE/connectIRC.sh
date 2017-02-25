PS3='Please choose server> '
options=("irc.freenode.net" "irc.hak5.org" "chaostal.hackint.org" \
	"euroserv.fr.quakenet.org" "irc.servercentral.net" "jolly.geekshed.net" \
	"exit")

select opt in "${options[@]}"
do

	if [ $opt = "exit" ]; then
		echo """
		Terminating $0"""
		exit 0
	else
		IP=`jping $opt`

		BitchX -d -n Sepher $IP
	fi
done
