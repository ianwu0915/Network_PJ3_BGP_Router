

class Ip:
    """ This is a class to represent the ip address and net mask"""
    def __init__(self, ip, netmask):
        """ The init function to set up the ip class
        :param:
            ip: The string that represent the ip address like "192.168.23.4"
            netmask: The string of the netmask like "255.255.0.0"
        """
        self.ip_string = ip
        self.netmask_string = netmask
        self.length = 4
        self.address = [int(qdn) for qdn in ip.split('.')]
        self.mask = [int(qdn) for qdn in netmask.split('.')]
        self.network_prefix = [self.address[i] & self.mask[i] for i in range(self.length)]
        self.network_prefix_string = ".".join(str(qdn) for qdn in self.network_prefix)
        self.mask_len = 0
        for i in range(self.length):
            # self.mask_len += self.mask[i].bit_count()
            self.mask_len += bin(self.mask[i]).count("1")


    def network_to_int(self):
        """
        This is a function that convert the
        :return: The number of the number with the proper bit shift
        """
        return (self.network_prefix[0] << 24) + (self.network_prefix[1] << 16) + \
               (self.network_prefix[2] << 8) + (self.network_prefix[3])

    def shift_ip_and_mask(self):
        """
        This is a function that shift the netmask left by one bit
        :return: the string represent of the new netmask after shift
        """
        # Convert IP and mask to integer
        mask_int = sum(part << (24 - i * 8) for i, part in enumerate(map(int, self.netmask_string.split('.'))))

        # Shift one bit to the left
        mask_int <<= 1

        # Convert back to dot-decimal form
        mask = '.'.join(str((mask_int >> (24 - i * 8)) & 0xFF) for i in range(4))

        return mask

    # check if the given ip address belong to this network ip class and return the longest len
    def belong_to(self, other_ip):
        """
        Check if the other ip belong to this ip class after masking and return the matching length
        :param other_ip: Could be a string or the other ip class
        :return: The length of the matching network name length, -1 if the other ip is not in this
                ip range.
        """
        # check if the other is an ip class
        if isinstance(other_ip, Ip):
            other_network = other_ip.network_prefix
        else:
            other_address = [int(qdn) for qdn in other_ip.split(".")]
            other_network = [other_address[i] & self.mask[i] for i in range(self.length)]
        for i in range(self.length):
            if self.network_prefix[i] != other_network[i]:
                return -1
        return self.mask_len

    def __str__(self) -> str:
        """
        To string method of the ip class
        :return: The string of the ip class as "192.156.23.23/16"
        """
        return ".".join(str(qdn) for qdn in self.address) + f"/{self.mask_len}"

    def update_mask_length(self, new_mask_len):
        """
        The function can set the netmask to a given netmask link
        :param new_mask_len: the length of the netmask
        :return: The new string of the netmask
        """
        if new_mask_len < 0 or new_mask_len > 32:
            raise ValueError("Invalid mask length")
        new_mask = [0, 0, 0, 0]
        for i in range(new_mask_len):
            new_mask[i // 8] |= 1 << (7 - (i % 8))
        self.mask = new_mask
        self.mask_len = new_mask_len
        return ".".join(str(qdn) for qdn in self.mask)


if __name__ == "__main__":
    x = Ip("192.168.0.1", "255.255.255.0")
    print("Original mask:", x.mask)
    print("Original mask length:", x.mask_len)

    # Update mask length to 25
    x.update_mask_length(20)
    print("Updated mask:", x.mask)
    print("Updated mask length:", x.mask_len)
