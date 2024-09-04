
def happy_birthday():
    name = input('Enter your name: ')
    birth_month = input('Enter your birth month: ')
    birth_day = input('Enter the day of your birth: ')
    birth_year = input('Enter your birt year: ')

    return name, birth_month, birth_day, birth_year

num_users = int(input('Enter the number of users: '))

for i in range (num_users):
    name, birth_month, birth_day, birth_year = happy_birthday()
    print (name, ',your birthday is on', birth_month, ',', birth_day, birth_year, '!' )
