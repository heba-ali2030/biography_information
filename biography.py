# 1- check string
def check_alphabet(name):
    while name.isalpha() == False:
        print('Ooh, there is typing mistake?!')
        name = input('Please type answer in alphabet: ')
    return name

# 2- check numbers
def check_number(number):
    while number.isdigit() == False:
        number = input('please enter a valid number to continue: ')
    return (int(number))


# 3- check day
def check_day(birth_day):
    days = range(1,32,1)
    for birth_day in days:
        if birth_day in days:
            break
        else:
            print('Ooh, Sorry, there is a mistake in your typing, try again!')
            birth_day= input('please type birth day in numbers : \n ')
        
    return int(birth_day)
        
# 4- check month
def check_month(birth_month):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for birth_month  in months:
        if birth_month in months:
            break
        else:
            print('Ooh, Sorry, there is a mistake in your typing, try again!')
            birth_month= input('please type the first 3 letters of the birth month : \n ').casefold()

    return birth_month

# 5- check year
def check_year(birth_year):
    year = range(1900,2021)
    for birth_year in year:
        if birth_year in year:
            break
        else:
            print('Ooh, Sorry, there is a mistake in your typing, try again!')
            birth_year = input('please type the 4 numbers of your birth year: \n ')

    return int(birth_year)


# ask the user about name 
first_name = check_alphabet(input('please enter your first name:\n'))
last_name = check_alphabet(input('please enter your last name:\n'))

# ask the user about date of birth
birth_day = check_day(input('Enter your day of birth?: \n'))
birth_month = check_month(input('Enter your birth month?: \n'))
birth_year = check_year(input('Enter your birth year?: \n')) 


# ask the user about address
street_number = check_number(input('enter your address street number: \n'))
street_name = check_alphabet(input('enter your address street name: \n'))
state = check_alphabet(input('enter your address state: \n'))

# ask the user about goals
goals = input('please enter your personal goals: \n')

print('------------------------------------------------------------')
# print user biography
print('Biography information:')

print(f'- Name: {first_name} {last_name}')
print(f'- Date of birth: {birth_month} {birth_day}, {birth_year}')
print(f'- Address: {street_number} {street_name}, {state}')
print(f'- Personal goals:  {goals}')

