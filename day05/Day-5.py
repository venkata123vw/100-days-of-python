import random
letters = [
'a','b','c','d','e','f','g','h','i','j','k','l','m','n',
'o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N',
'O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','%','&','(',')','*','+']

#easy level - order not randomised:
# password = ""

# print("Welcome to the PyPassword Generator!")

# nr_letters = int(input("How many letters would you like in your password?\n"))
# for random_letters in range(nr_letters) :
#     random_letters = random.choice(letters)
#     password += random_letters


# nr_symbols = int(input("How many symbols would you like?\n"))
# for random_symbols in range(nr_symbols) :
#     random_symbol = random.choice(symbols)
#     password += random_symbol
    

# nr_numbers = int(input("How many numbers would you like?\n"))
# for random_numbers in range(nr_numbers) :
#     random_number = random.choice(numbers)
#     password += random_number

# print(password)
#hard level - order of characters randomised:
password_list = []
nr_letters = int(input("How many letters would you like in your password?\n"))
for random_letters in range(nr_letters) :
    random_letters = random.choice(letters)
    password_list.append(random_letters)


nr_symbols = int(input("How many symbols would you like?\n"))
for random_symbols in range(nr_symbols) :
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)
    

nr_numbers = int(input("How many numbers would you like?\n"))
for random_numbers in range(nr_numbers) :
    random_number = random.choice(numbers)
    password_list.append(random_number)

random.shuffle(password_list)
password = ""
for char in password_list :
    password += char
print(password)
