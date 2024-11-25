#0

def print_greeting():
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

print_greeting()

#1

def check_letter():
    letter = input("Enter a letter (a-z or A-Z): ").lower()
    if not letter.isalpha() or len(letter) != 1:
        print("Invalid input. Please enter a single alphabetical character.")
        return
    
    vowels = 'aeiou'
    if letter in vowels:
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")

check_letter()

#2

def check_voting_eligibility():
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            print("Age cannot be negative.")
        elif age >= 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

check_voting_eligibility()

#3

def calculate_dog_years():
    try:
        dog_age = int(input("Input a dog's age: "))
        if dog_age < 0:
            print("Age cannot be negative.")
            return
        if dog_age <= 2:
            dog_years = dog_age * 10.5
        else:
            dog_years = 21 + (dog_age - 2) * 4
        print(f"The dog's age in dog years is {dog_years}.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

calculate_dog_years()

#4

def weather_advice():
    is_cold = input("Is it cold? (yes/no): ").lower() == 'yes'
    is_raining = input("Is it raining? (yes/no): ").lower() == 'yes'
    
    if is_cold and is_raining:
        print("Wear a waterproof coat.")
    elif is_cold and not is_raining:
        print("Wear a warm coat.")
    elif not is_cold and is_raining:
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")

weather_advice()

#5

def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ").capitalize()
    try:
        day = int(input("Enter the day of the month: "))
        if day < 1 or day > 31:
            print("Invalid day.")
            return
    except ValueError:
        print("Invalid input. Please enter a numerical value for the day.")
        return
    
    if month in ['Dec', 'Jan', 'Feb'] or (month == 'Mar' and day < 20):
        season = "Winter"
    elif month in ['Mar', 'Apr', 'May'] or (month == 'Jun' and day < 21):
        season = "Spring"
    elif month in ['Jun', 'Jul', 'Aug'] or (month == 'Sep' and day < 22):
        season = "Summer"
    elif month in ['Sep', 'Oct', 'Nov'] or (month == 'Dec' and day < 21):
        season = "Fall"
    else:
        season = "Invalid date"

    if season != "Invalid date":
        print(f"{month} {day} is in {season}.")
    else:
        print("Invalid date input.")

determine_season()
