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

        s9 = self.addSwitch('s9', dpid = int2dpid(19))
        s10 = self.addSwitch('s10', dpid = int2dpid(20))


        s11 = self.addSwitch('s11',dpid = int2dpid(21))
        s12 = self.addSwitch('s12',dpid = int2dpid(22))

        s13 = self.addSwitch('s13',dpid = int2dpid(23))



        h0 = self.addHost('h0')
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')
        h11 = self.addHost('h11')
        h12 = self.addHost('h12')
        h13 = self.addHost('h13')


        self.addLink(s0,h0)
        self.addLink(s1,h1)
        self.addLink(s2,h2)
        self.addLink(s3,h3)
        self.addLink(s4,h4)
        self.addLink(s5,h5)
        self.addLink(s6,h6)
        self.addLink(s7,h7)
        self.addLink(s8,h8)
        self.addLink(s9,h9)
        self.addLink(s10,h10)
        self.addLink(s11,h11)
        self.addLink(s12,h12)
        self.addLink(s13,h13)

        self.addLink(s0,s1)
        self.addLink(s0,s2)
        self.addLink(s1,s2)

        self.addLink(s3,s4)
        self.addLink(s3,s5)


        self.addLink(s6,s7)
        self.addLink(s6,s8)
        self.addLink(s7,s8)

        self.addLink(s9,s10)

        self.addLink(s11,s12)





        self.addLink(s0,s3)
        self.addLink(s2,s4)
        self.addLink(s5,s7)
        self.addLink(s3,s6)
        self.addLink(s8,s9)
        self.addLink(s10,s11)
        self.addLink(s12,s13)
        self.addLink(s1,s13)


topos = { '13nodes34591013n': ( lambda: MyTopo() ) }
