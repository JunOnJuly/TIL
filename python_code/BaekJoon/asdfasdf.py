import math
def fee(minute, distance):
    rent_fee = math.ceil(minute / 10) * 1200
    rent_insure = math.ceil(minute / 30) * 525
    if distance < 100:
        run_fee = distance * 170
    else:
        run_fee = (distance - 100) * 85 + 17000

    total = rent_fee + rent_insurance + run_fee
    return total