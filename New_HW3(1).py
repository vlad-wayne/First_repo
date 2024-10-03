from datetime import datetime

def get_days_from_today(current_date, another_date):
    try:
        
        current_datetime = datetime.strptime(current_date, '%Y-%m-%d').date()
        another_datetime = datetime.strptime(another_date, '%Y-%m-%d').date()

        
        difference = (current_datetime - another_datetime).days
        return difference
    except ValueError:
        return "Invalid date format. Please use 'YYYY-MM-DD'."


result = get_days_from_today('2024-10-02', '2024-09-02')  
print(result)

invalid_result = get_days_from_today('2024-10-02', '02-09-2024') 
print(invalid_result)
