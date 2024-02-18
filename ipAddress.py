
class Ip:
    def __init__(self, ip, netmask):
        self.length = 4
        self.address = [int(qdn) for qdn in ip.split('.')]
        self.binary_address = [int(format(part, "08b")) for part in self.address]
        self.mask = [int(qdn) for qdn in netmask.split('.')]
        self.binary_mask = [int(format(part, "08b")) for part in self.mask]
        self.network_prefix = [self.address[i] & self.mask[i] for i in range(len(self.address))]
        self.binary_network = [int(format(part, "08b")) for part in self.network_prefix]


    def longest_match(self, other_ip):
        if isinstance(other_ip, Ip):
            other_binary_address = other_ip.binary_network
        else:
            other_address = [int(qdn) for qdn in other_ip.split('.')]
            other_binary_address = [int(format(part, '08b')) for part in other_address]

        max_match_length = 0
        for i in range(self.length):
            xor_result = self.binary_network[i] ^ other_binary_address[i]
            match_length = 0
            while xor_result > 0:
                xor_result >>= 1
                match_length += 1
            if match_length > max_match_length:
                max_match_length = match_length

        return max_match_length
    
    def belong_to(self, other_ip) -> bool:
        if isinstance(other_ip, Ip):
            
if __name__ == "__main__":
    x = Ip("192.168.0.1", "255.255.255.0")
    y = Ip("192.168.0.10", "255.255.255.0")
    print(x.binary_network)
    print(y.binary_network)
    match_length = x.longest_match(y)
    print("Longest match length:", match_length)