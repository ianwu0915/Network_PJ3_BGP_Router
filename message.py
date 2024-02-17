class Message:
    def __init__(self, messageJson,):
        self.network = messageJson['network']
        self.netmask = messageJson['netmask']
        self.localpref = messageJson['localpref']
        self.ASPath = messageJson['ASPath']
        self.origin = messageJson['origin']
        self.selfOrigin = messageJson['selfOrigin']

    def copy(self, new_AsPath):
        return {
            'netmask': self.netmask,
            'ASPath': new_AsPath,
            'network': self.network
        }
