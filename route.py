class Route:
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

    # {
    #       "origin": "EGP",
    #       "localpref": 100,
    #       "network": "172.168.0.0",
    #       "ASPath": [2],
    #       "netmask": "255.255.0.0",
    #       "peer": "172.168.0.2",
    #       "selfOrigin": true
    #     }
    def dump(self):
        return {
            'origin': self.origin,
            'localpref': self.localpref,
            'network': self.network,
            'ASPath': self.ASPath,
            'netmask': self.netmask,
            'peer': "",
            'selfOrigin': self.selfOrigin
        }

