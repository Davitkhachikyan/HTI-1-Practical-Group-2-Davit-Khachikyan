import csv


class Laptop:
    def __init__(self, manufacturer, model, category, screen_size, screen, cpu, ram, storage, gpu, op_system, op_sys_ver, weight, price):
        self.brand = manufacturer
        self.model = model
        self.category = category
        self.screen_size = screen_size
        self.screen = screen
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu
        self.op_system = op_system
        self.op_sys_ver = op_sys_ver
        self.weight = weight
        self.price = price


def get_laptops():
    laps = []
    with open("/home/davo/Desktop/laptops.csv") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            laps.append(Laptop(
                row[0],
                row[1],
                row[2],
                float(row[3].strip('"')),
                row[4],
                row[5],
                int(row[6].rstrip("GB")),
                row[7],
                row[8],
                row[9],
                row[10],
                float(row[11].replace(",", ".").rstrip("kgs")),
                float(row[12].replace(",", "."))
                ))
    return laps


def highest_price(laps, count):
    laps.sort(key=lambda x: x.price)
    return laps[-count-1:-1]


def heaviest(laps, count):
    laps.sort(key=lambda x: x.weight)
    return laps[-count-1:-1]


def cheapest(laps, count):
    laps.sort(key=lambda x: x.price)
    return laps[0:count]


def brand_count(laps):
    diction = {}
    for i in laps:
        diction[i.brand] = diction.get(i.brand, 0) + 1
    return diction


def op_count(laps):
    diction = {}
    for i in laps:
        diction[i.op_system] = diction.get(i.op_system, 0) + 1
    return diction


def ram_count(laps):
    diction = {}
    for i in laps:
        diction[f"{i.ram}GB"] = diction.get(i.ram, 0) + 1
    return diction


def powerful_ram(laps, count):
    laps.sort(key=lambda x: x.ram)
    return laps[-count-1:-1]


obj_list = get_laptops()

for i in highest_price(obj_list, 5):
    print(f"{i.brand} : {i.model} : {i.price}")


for i in cheapest(obj_list, 5):
    print(f"{i.brand} : {i.model} : {i.price}")


for i in heaviest(obj_list, 5):
    print(f"{i.brand} : {i.model} : {i.weight}")


for i in powerful_ram(obj_list, 5):
    print(f" {i.brand} : {i.model} : {i.ram}GB")


print(ram_count(obj_list))

print(brand_count(obj_list))

print(op_count(obj_list))


