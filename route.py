from ipAddress import Ip
import json


class Route:
    """
    The class represent a route that will be store in the routing table.
    """
    def __init__(self, message_json):
        """
        The init function to create the Route class
        :param message_json: The json object to build the route
        """
        # this is used to decide the priority of the origin
        self.ORIGIN_PRIORITY = {
            "IGP": 3,
            "EGP": 2,
            "UNK": 1
        }
        # the source of the ip that send this route
        self.source = message_json["src"]
        self.network = message_json["msg"]['network']
        self.netmask = message_json["msg"]['netmask']
        self.localpref = message_json["msg"]['localpref']
        self.ASPath = message_json["msg"]['ASPath']
        self.origin = message_json["msg"]['origin']
        self.selfOrigin = message_json["msg"]['selfOrigin']
        self.ip = Ip(self.network, self.netmask)

    def copy(self, new_as_path):
        """
        The function to return the new As path in a json format string
        :param new_as_path: the new path
        :return: string of the netmask, ASPath, network
        """
        return {
            'netmask': self.netmask,
            'ASPath': new_as_path,
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

    def copy_route(self):
        return Route({
            "msg": {
                "origin": self.origin,
                "localpref": self.localpref,
                "network": self.network,
                "ASPath": self.ASPath,
                "netmask": self.netmask,
                "peer": "",
                "selfOrigin": self.selfOrigin
            },
            "src": self.source,
            "dst": self.source,
            "type": "update"
        })
    def dump(self):
        """
        Dump the class information in a json format
        :return: string represent of the class
        """
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
        """
        Send the withdrawa message with the given json value
        :param message: json object that send the with draw
        :return: string format of the withdraw message
        """
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
        """
        The equal method to check if the two route is the same
        :param other: Route class to compare
        :return: True if equal, False otherwise
        """
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
    def is_adjacent(self, other):
        """
        Check if the two Route class is adjacent and can be combined
        :param other: Route class to check
        :return: True if adjacent, False otherwise
        """
        return (self.source == other.source and
                self.localpref == other.localpref and
                self.ASPath == other.ASPath and
                self.origin == other.origin and
                self.selfOrigin == other.selfOrigin and
                self.netmask == other.netmask and
                self.ip_adjacent(other))

    def ip_adjacent(self, other_route):
        """
        To check if the other_route is different in the last bit of the network prefix
        :param other_route: Route class to check
        :return: True if the address is adjacent, False otherwise
        """

        ip_int1 = self.ip.network_to_int()
        ip_int2 = other_route.ip.network_to_int()

        mask = self.ip.mask_len

        return abs(ip_int1 - ip_int2) == 2 ** (32 - mask)

    def compare_origin(self, other_origin):
        """
        Compare the origin of this route with another route's origin based on priority.
        Returns:
            1 if this route's origin is better, -1 if the other route's origin is better, 0 if they are equal.
        """
        my_priority = self.ORIGIN_PRIORITY.get(self.origin, 0)
        other_priority = self.ORIGIN_PRIORITY.get(other_origin, 0)

        if my_priority > other_priority:
            return 1
        elif my_priority < other_priority:
            return -1
        else:
            return 0

    def source_to_int(self):
        """
        Turn the source ip of the route class to an integer
        :return: integer
        """
        octets = self.source.split('.')
        return (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])


if __name__ == "__main__":
    x = Route(json.loads(
        '{"type": "update", "src": "192.168.0.2", "dst": "192.168.0.1", "msg": {"network": "192.168.1.0", "netmask": "255.255.255.0", "localpref": 100, "ASPath": [1], "origin": "EGP", "selfOrigin": true}}'))
    print(type(x.localpref))
    print(type(x.selfOrigin))
    print(x.selfOrigin)
    print(x.ASPath)
    print(type(x.ASPath))
    print(x.origin)
    print(type(x.origin))
