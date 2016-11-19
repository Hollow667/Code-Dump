# -d says not to attach to the sessions yet. top runs in the first
# window
tmux new-session -d top
# In the most recently created session, split the (only) window
# and run htop in the new pane
tmux split-window -v htop
# Split the new pane and run perl
tmux split-pane -v perl re.pl
# Make all three panes the same size (currently, the first pane
# is 50% of the window, and the two new panes are 25% each).
tmux select-layout even-vertical
# Now attach to the window
tmux attach-session
