class Ip:
    def __init__(self, ip, netmask):
        self.ip_string = ip
        self.length = 4
        self.address = [int(qdn) for qdn in ip.split('.')]
        # self.binary_address = "".join(format(part, "08b") for part in self.address)
        self.mask = [int(qdn) for qdn in netmask.split('.')]
        # self.binary_mask = "".join(format(part, "08b") for part in self.mask)
        self.network_prefix = [self.address[i] & self.mask[i] for i in range(self.length)]
        # self.binary_network = [int(format(part, "08b")) for part in self.network_prefix]
        self.mask_len = 0
        for i in range(self.length):
            self.mask_len += self.mask[i].bit_count()

    def longest_match(self, other_ip):
        if isinstance(other_ip, Ip):
            other_network = other_ip.network_prefix
        else:
            other_address = [int(qdn) for qdn in other_ip.split('.')]
        max_match_length = 0
        for i in range(self.length):
            xor_result = int(self.network_prefix[i]) ^ int(other_network[i])
            match_length = 0
            while xor_result > 0:
                xor_result >>= 1
                match_length += 1
            if match_length > max_match_length:
                max_match_length = match_length
        return max_match_length

    def belong_to(self, other_ip) -> bool:
        if isinstance(other_ip, Ip):
            other_network = other_ip.network_prefix
        else:
            other_address = [int(qdn) for qdn in other_ip.split(".")]
            other_network = [other_address[i] & self.mask[i] for i in range(self.length)]
        for i in range(self.length):
            if self.network_prefix[i] != other_network[i]:
                return False
        return True

    def __str__(self) -> str:
        return ".".join(str(qdn) for qdn in self.address) + f"/{self.mask_len}"


if __name__ == "__main__":
    x = Ip("192.168.0.1", "255.255.255.0")
    y = Ip("192.168.1.10", "255.255.254.0")
    print(x.mask_len)
    print(x)
    print(x.belong_to(y))
