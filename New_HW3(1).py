from datetime import datetime

def get_days_from_today(another_date):
    try:
        
        current_datetime = datetime.now().date()
        another_datetime = datetime.strptime(another_date, '%Y-%m-%d').date()

        
        difference = (current_datetime - another_datetime).days
        return difference
    except ValueError:
        return "Invalid date format. Please use 'YYYY-MM-DD'."
        


result = get_days_from_today('2024-05-02')  
print(result)

invalid_result = get_days_from_today('02-09-2024') 
print(invalid_result)
