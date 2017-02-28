

class Input(Node):
    def __init__(self):
        Node.__init__(self)

    def forward(self,value=None):
        if value is not None:
            self.value = value