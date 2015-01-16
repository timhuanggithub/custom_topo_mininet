__author__ = 'mininet'
from mininet.topo import Topo

def int2dpid( dpid ):
        try:
            dpid = hex( dpid )[ 2: ]
            dpid = '0' * ( 16 - len( dpid ) ) + dpid
            return dpid
        except IndexError:
            raise Exception( 'Unable to derive default datapath ID - '
                             'please either specify a dpid or use a '
                             'canonical switch name such as s23.' )

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        s0 = self.addSwitch('s0', dpid = int2dpid(10))
        s1 = self.addSwitch('s1', dpid = int2dpid(11))
        s2 = self.addSwitch('s2', dpid = int2dpid(12))
        s3 = self.addSwitch('s3', dpid = int2dpid(13))
        s4 = self.addSwitch('s4', dpid = int2dpid(14))
        s5 = self.addSwitch('s5', dpid = int2dpid(15))
        h0 = self.addHost('h0')
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')

        self.addLink(s2,s0)
        self.addLink(s2,s1)
        self.addLink(s2,h0)
        self.addLink(s2,h1)

        self.addLink(s3,s0)
        self.addLink(s3,s1)
        self.addLink(s3,h2)
        self.addLink(s3,h3)

        self.addLink(s4,s0)
        self.addLink(s4,s1)
        self.addLink(s4,h4)
        self.addLink(s4,h5)

        self.addLink(s5,s0)
        self.addLink(s5,s1)
        self.addLink(s5,h6)
        self.addLink(s5,h7)


topos = { '6nodes': ( lambda: MyTopo() ) }
