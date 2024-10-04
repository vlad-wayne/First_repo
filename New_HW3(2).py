import random

def get_numbers_ticket(min_value, max_value, quantity):
    if min_value < 1:
        print('ERROR: Write the number >= 1')
        return []
    
    if max_value > 1000:
        print('ERROR: Write the number <= 1000')
        return []
    
    if quantity <= 0 or quantity > (max_value - min_value + 1):
        print('ERROR: Write the number between min and max')
        return []

    result = random.sample(range(min_value, max_value + 1), quantity)
    result.sort()
    
    return result

result = get_numbers_ticket(1, 49, 6)
print(result)

result_invalid_min = get_numbers_ticket(0, 49, 6)  
print(result_invalid_min)

result_invalid_max = get_numbers_ticket(1, 1001, 6)  
print(result_invalid_max)

result_invalid_quantity = get_numbers_ticket(1, 49, 60)  
print(result_invalid_quantity)
