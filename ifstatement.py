floor = 22
sagar_floor = 13
current__floor = 20
different = sagar_floor - current__floor


if different < 0 :
    current__floor = sagar_floor
    print("move down")


if different > 0 :
    current__floor = sagar_floor
    print("move up") 