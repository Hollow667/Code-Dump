#you can create a fifo
ESPEAK_FIFO=/tmp/espeak_fifo
mkfifo $ESPEAK_FIFO
# start espeak in the background
espeak -f $ESPEAK_FIFO &
# or use tee to keep text on display too
cat $ESPEAK_FIFO | tee /dev/tty | espeak
# redirect stdout to fifo
exec >$ESPEAK_FIFO
