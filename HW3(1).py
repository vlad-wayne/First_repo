from datetime import datetime

def get_days_from_today():

    current_datetime = datetime.now().date()
    
    while True:

        date = input('write YYYY-MM-DD: ')

        try:

            date_str = datetime.strptime(date, '%Y-%m-%d' ).date()
            break

        except ValueError:
            print("Invalid date format. Please try YYYY-MM-DD.")

    difference = (current_datetime - date_str).days
    
    return difference

result = get_days_from_today()
print(result)


