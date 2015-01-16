__author__ = 'mininet'
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def int2dpid( dpid ):
        try:
            dpid = hex( dpid )[ 2: ]
            dpid = '0' * ( 16 - len( dpid ) ) + dpid
            return dpid
        except IndexError:
            raise Exception( 'Unable to derive default datapath ID - '
                             'please either specify a dpid or use a '
                             'canonical switch name such as s23.' )
class Fournodes(Topo):

    def __init__(self, k=3, **opts):

        Topo.__init__(self, **opts)
        s0 = self.addSwitch('s0', dpid = int2dpid(10))
        s1 = self.addSwitch('s1', dpid = int2dpid(11))
        s2 = self.addSwitch('s2', dpid = int2dpid(12))
        s3 = self.addSwitch('s3', dpid = int2dpid(13))

        h0 = self.addHost('h0')
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')

        self.addLink(s0,h0)
        self.addLink(s1,h1)

        self.addLink(s2,h2)
        self.addLink(s3,h3)

        self.addLink(s0,s1)
        self.addLink(s1,s2)
        self.addLink(s2,s3)
        self.addLink(s3,s0)


topos = {'4nodes': (lambda:Fournodes())}
