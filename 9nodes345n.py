from mininet.topo import Topo

def int2dpid( dpid ):
        try:
            dpid = hex( dpid )[ 2: ]
            dpid = '0' * ( 16 - len( dpid ) ) + dpid
            print dpid
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

        s6 = self.addSwitch('s6', dpid = int2dpid(16))
        s7 = self.addSwitch('s7', dpid = int2dpid(17))
        s8 = self.addSwitch('s8', dpid = int2dpid(18))



        h1 = self.addHost('h1')
        h4 = self.addHost('h4')
        h8 = self.addHost('h8')


        self.addLink(s1,h1)
        self.addLink(s4,h4)
        self.addLink(s8,h8)

        self.addLink(s0,s1)
        self.addLink(s0,s2)
        self.addLink(s1,s2)

        self.addLink(s3,s4)
        self.addLink(s4,s5)


        self.addLink(s6,s7)
        self.addLink(s6,s8)
        self.addLink(s7,s8)

        self.addLink(s0,s3)
        self.addLink(s2,s4)
        self.addLink(s5,s7)
        self.addLink(s4,s6)



topos = { '9nodes345n': ( lambda: MyTopo() ) }
