import random
def get_numbers_ticket(min_num, max_num, quantity):
    roll_list = []
    if min_num < 1 or max_num > 1000:
        return roll_list
    for roll in range(quantity):
        num = random.randint(min_num, max_num)
        roll_list.append(num)
    roll_list.sort()
    return roll_list

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
