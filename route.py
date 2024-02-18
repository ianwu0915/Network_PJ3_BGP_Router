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