class Computer():

    def __init__(self, graphics_card, cpu, ram, motherboard, hdd, ssd):
        self.graphics_card = graphics_card
        self.cpu = cpu
        self.ram = ram
        self.motherboard = motherboard
        self.hdd = hdd
        self.ssd = ssd

Computer1 = Computer('rtx 2080 ', 'amd ryzen 5', '32 gb', 'msi nighthawk', 'westren ditgal', 'nvme')

def printcomputer():
    computer1 = print(Computer1.graphics_card)
    computer1 = print(Computer1.cpu)
    computer1 = print(Computer1.ram)
    computer1 = print(Computer1.motherboard)
    computer1 = print(Computer1.hdd)
    computer1 = print(Computer1.ssd)


printcomputer()
