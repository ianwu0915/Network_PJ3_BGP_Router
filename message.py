class Message:
    def __init__(self, messageJson,):
        self.network = messageJson['network']
        self.netmask = messageJson['netmask']
        self.localpref = messageJson['localpref']
        self.ASPath = messageJson['ASPath']
        self.origin = messageJson['origin']
        self.selfOrigin = messageJson['selfOrigin']

    def convertToJSON(self):
        return {
            "network": self.network,
            "netmask": self.netmask,
            "localpref": self.localpref,
            "ASPath": self.ASPath,
            "origin": self.origin,
            "selfOrigin": self.selfOrigin
        }
