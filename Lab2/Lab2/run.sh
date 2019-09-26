#!/bin/bash

# Note: Mininet must be run as root.  So invoke this shell script
# using sudo.

gnome-terminal --tab -- bash -c "sudo mn --topo single,8 --controller remote --mac"
sudo fuser -k 6633/tcp
cd $HOME
cd pox
./pox.py log.level
--DEBUG openflow.of_01
forwarding.l2_learning misc.firewall
