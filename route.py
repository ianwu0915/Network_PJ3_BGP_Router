from ipAddress import Ip


class Route:
    def __init__(self, messageJson):
        self.source = messageJson["src"]
        self.network = messageJson["msg"]['network']
        self.netmask = messageJson["msg"]['netmask']
        self.localpref = messageJson["msg"]['localpref']
        self.ASPath = messageJson["msg"]['ASPath']
        self.origin = messageJson["msg"]['origin']
        self.selfOrigin = messageJson["msg"]['selfOrigin']
        self.ip = Ip(self.network, self.netmask)

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

    def withdraw(self, message):
        return {
            "msg": {
                "netmask": self.netmask,
                "ASPath": self.ASPath,
                "network": self.network
            },
            "src": message["src"],
            "dst": message["src"],
            "type": "withdraw"
        }

    # Update check for the exact same route
    def __eq__(self, other):
        if isinstance(other, Route):
            return (self.source == other.source and
                    self.network == other.network and
                    self.netmask == other.netmask and
                    self.localpref == other.localpref and
                    self.ASPath == other.ASPath and
                    self.origin == other.origin and
                    self.selfOrigin == other.selfOrigin)
        return False

    # Check if the route is adjacent to another route
    def isAdjacent(self, other):
        return (self.source == other.source and
                self.localpref == other.localpref and
                self.ASPath == other.ASPath and
                self.origin == other.origin and
                self.selfOrigin == other.selfOrigin and
                self.Ip_isAdjacent(other))

    def Ip_isAdjacent(self, other_route):

        ip_int1 = self.ip.ip_to_int()
        ip_int2 = other_route.ip.ip_to_int()

        mask = self.ip.mask_len

        return abs(ip_int1 - ip_int2) == 2 ** (32 - mask)
