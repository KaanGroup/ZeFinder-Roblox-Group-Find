import random

def Get_IDs():
    IDs = str([random.randint(32_000_000, 35_230_999) for _ in range(100)])
    return IDs.replace(" ", "")[:-1][1:]