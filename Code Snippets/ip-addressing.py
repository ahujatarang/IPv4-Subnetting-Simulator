# IP Addressing logic class used for subnetting simulation
class Addressing:
    def __init__(self, ip, block, ipx):
        self.ip = ip 
        self.block = block 
        self.ipx = ipx

    # Determine the class of the IP address
    def className(self): 
        netId = int(self.ip.split('.')[0]) 
        if netId < 128:
            return "Class A" 
        elif netId < 192:
            return "Class B" 
        elif netId < 224:
            return "Class C"
        elif netId < 240:
            return "Class D"
        elif netId < 256:
            return "Class E"
        else:
            return "Tarang"

    # Calculate number of subnets based on class and block size
    def subnet(self): 
        netId = int(self.ip.split('.')[0]) 
        if netId < 128:
            sub = int(self.block) - 8
        elif netId < 192:
            sub = int(self.block) - 16 
        elif netId < 224: 
            sub = int(self.block) - 24
        subnet = 2 ** sub
        return subnet

    # Calculate number of usable hosts per subnet
    def host(self): 
        sub = 32 - int(self.block) 
        subnet = (2 ** sub) - 2 
        return subnet

    # Convert block size to dotted decimal subnet mask
    def mask(self): 
        block = int(self.block) 
        mask = "1" * block + "0" * (32 - block)
        ip11 = str(self.BinaryToDecimal(mask[0:8])) 
        ip22 = str(self.BinaryToDecimal(mask[8:16])) 
        ip33 = str(self.BinaryToDecimal(mask[16:24])) 
        ip44 = str(self.BinaryToDecimal(mask[24:32]))
        submask = ip11 + '.' + ip22 + '.' + ip33 + '.' + ip44 
        return submask

    # Convert binary string to decimal number
    def BinaryToDecimal(self, binary): 
        decimal = 0
        for digit in binary:
            decimal = decimal * 2 + int(digit) 
        return decimal

    # Compare whether second IP lies in same subnet as the first
    def IpCompare(self):
        hostId = self.host() + 2 
        x = int(self.ip.split('.')[-1]) // hostId
        netId = x * hostId
        brodId = netId + hostId - 1
        if (int(self.ipx) < brodId) and (int(self.ipx) > netId):
            return "YES" 
        else:
            return "NO"
