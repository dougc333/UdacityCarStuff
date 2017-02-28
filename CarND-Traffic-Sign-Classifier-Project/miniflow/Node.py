

class Node(object):
    def __init__(self,inbound_nodes=[]):
        self.inbound_nodes = inbound_nodes
        self.outbound_nodes = []

        for n in self.inbound_nodes:
            n.outbound_nodes.append(self)
        self.value = None

    def forward(self):
        raise NotImplemented
    