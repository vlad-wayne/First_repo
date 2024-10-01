import random 

def get_numbers_ticket():

    min_value = int(input('min: '))
    if min_value < 1:
        print('ERROR.Write the number >= 1 ')
        return []

    max_value = int(input('max: '))
    if max_value > 1000:
        print('ERROR.Write the number <= 1000 ')
        return []

    quantity = int(input('quantity: '))
    if quantity <= 0 or quantity > (max_value - min_value + 1):
        print('ERROR.Write the number between min and max ')
        return []
    
    result = random.sample(range(min_value, max_value + 1), quantity)
    result.sort()
    return result

result  = get_numbers_ticket()
print(result)