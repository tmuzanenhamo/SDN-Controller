#!/usr/bin/python

# EEE4121F-B Lab 2
# SDN

# Implementing a Layer-2 Firewall using POX and Mininet


from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def treeTopo():
    net = Mininet( controller=RemoteController )
    # Adding controller
    net.addController('c0')
    h1=net.addHost('h1',mac='00:00:00:00:00:01')
    h2=net.addHost('h2',mac='00:00:00:00:00:02')
    h3=net.addHost('h3',mac='00:00:00:00:00:03')
    h4=net.addHost('h4',mac='00:00:00:00:00:04')
    h5=net.addHost('h5',mac='00:00:00:00:00:05')
    h6=net.addHost('h6',mac='00:00:00:00:00:06')
    h7=net.addHost('h7',mac='00:00:00:00:00:07')
    h8=net.addHost('h8',mac='00:00:00:00:00:08')
    #Adding switches
    s1=net.addSwitch('s1')
    s2=net.addSwitch('s2')
    s3=net.addSwitch('s3')
    s4=net.addSwitch('s4')
    s5=net.addSwitch('s5')
    s6=net.addSwitch('s6')
    s7=net.addSwitch('s7')
    #creating links
    net.addLink(h1,s3)
    net.addLink(h2,s3)
    net.addLink(h3,s4)
    net.addLink(h4,s4)
    net.addLink(h5,s5)
    net.addLink(h6,s6)
    net.addLink(h7,s7)
    net.addLink(h8,s7)
    
    root=s1
    layer1=[s2,s5]
    layer2=[s3,s4,s6,s7]
    for idx,l1 in enumerate(layer1):
        net.addLink( root,l1 )
        net.addLink( l1, layer2[2*idx] )
        net.addLink( l1, layer2[2*idx + 1] )
        
    # Starting network
    net.start()

    # Running CLI
    CLI( net )

    # Stopping network
    net.stop()
    
    
    

if __name__ == '__main__':
    setLogLevel( 'info' )
    treeTopo()
