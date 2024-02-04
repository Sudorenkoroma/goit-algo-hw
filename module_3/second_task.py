import random
def get_numbers_ticket(min_num, max_num, quantity):
    roll_list = set()
    if min_num < 1 or max_num > 1000:
        return roll_list
    while len(roll_list) < quantity:
        roll_list.add(random.randint(min_num, max_num))
    roll_list = list(roll_list)
    roll_list.sort()
    return roll_list

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

