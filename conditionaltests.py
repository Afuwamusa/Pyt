color = 'purple'
print("is color = 'purple'? i predict True.")
print(color == 'purple')
print("\nis color = 'blue'? i predict True")
print(color.upper() == 'blue')
print("\nis color = 'purple'? i predict False")
print(color.upper() != 'purple')
print("\nis color = 'yellow'? i predict True")
print(color.lower() != 'yellow')
year_1 = 2018
year_2 = 2015
print("\nis year_1 and year_2 = 2017? i predict False")
print(year_1 >= 2017 and year_2 <=2017)
print("\nis year_1 and year_2 = 2017? i predict True")
print(year_1 <= 2017 and year_2 >=2017)
print("\nis year_1 and year_2 = 2017? i predict True")
print(year_1 == 2017 and year_2 == 2017)
print("\nis year_1 and year_2 = 2018? i predict False")
print(year_1 != 2018 and year_2 == 2018)
print("\nis year_1 and year_2 = 2015? i predict False")
print(year_1 <= 2015 and year_2 >=2015 )
print("\nis year_1 and year_2 = 2015? i predict False")
print(year_1 >= 2015 and year_2 <= 2015)
print("\nis year_1 and year_2 = 2015? i predict False")
print(year_1 ==2015 or year_2 >= 2015)
used_clothes = ["dresses","trousers","jumpsuits","shirts","t-shirts"]
non_used = ["sweaters"]
if non_used != "dresses":
    print("\ni'll wear dresses tomorrow")
if used_clothes != "sweaters":
    print("\nAm not wearing sweaters.")
if non_used not in used_clothes:
    print("\nI'll wear " + " " + non_used[0].title() + " " + "tomorrow")
if "t-shirts" in used_clothes:
    print('\nI like t-shirts')
if "sweaters" in used_clothes:
    print('\nIn like sweaters')
if "skirts" in non_used:
    print('\nI like skirts ')

alien_color = ['green','yellow','red']
if 'green' in alien_color:
    print("\nThe player earned 5 points")
if  'blue' in alien_color:
    print("\nThe player earns 5 points")
elif 'yellow' in alien_color:
    print("\nThe player earns 5 points")
else:
    print("\nThe  player earns 0 points")
if  alien_color is 'green':
    print("\nThe player just earned 5 points for shooting the alien")
if alien_color is not 'green':
    print("\nThe player just earned 10 points for shooting the alien")
if alien_color is 'yellow':
    print("\nThe player earns 5 points for shooting the alien")
else:
    print("\nThe player earns 10 points for shooting the alien")
if alien_color is 'green':
    print("\nThe player earned 5points")

elif alien_color is  'green':
    print("\nThe player earned 10 points")
else:
    print("\nThe player earned 15 points")
age = 70
if age < 2:
    print("\nThis person is a baby")
elif age  < 4:
    print("\nThis person is a toddler")
elif age < 13:
    print("\nThis person is a child")
elif age < 20:
    print("\nThis person is a teenager")
elif age < 65:
    print("\nThis person is an adult")
elif age > 65:
    print("\nThis person is an elder")
else:
    print("\nThis person is old")

favourite_fruits = ['watermelon','grapes','strawberries']
if 'banana' in favourite_fruits:
    print("\nI really like banana!")
if 'grapes' in favourite_fruits:
    print("\nI really like grapes")
if 'cherry' in favourite_fruits:
    print("\nI really like cherry")
if 'strawberries' in  favourite_fruits:
    print("\nI really like strawberries")
if 'watermelon' in favourite_fruits:
    print("\nI really like watermelon")
print("\nThose are my favourite fruits")

usernames = ["admin","Eric","moses","assistant admin","Recheal","Jenny"]
print("\nHello" + " " +   usernames[0]  + ",would you like to see a status report?" ) 
for username in usernames:
    print("\nHello" + " " + username + ",thank you for logging in")
usernames = []
if usernames:
    for username in usernames:
        print("\nno users found!")
else:
    print("\nwe need to find some users!")

current_users = ["shafiq","luis","moses","fifi","sharon"]
new_users = ["Merry","suzan","luis","moses","micheal"]
for new_user in new_users:
    if new_user not in current_users:
        print("\nThe person will need to enter a new username.")
    else:
        ("\nThe username is available.")
for current_user in current_users:
    if current_user  in new_users:
        print("\nThe user should not be accepted")

numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if  number == 1: 
         print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    elif number == [4,5,6,7,8,9]:
        if digits = number:
            for digit in digits:
                print(digit)
                # print('4th','5th','6th','7th','8th','9th')

    #        print('4th')
    # elif number == 5:
    #     print('5th')
    # elif number == 6:
    #     print('6th')
    # elif number == 7:
    #     print('7th')
    # elif number == 8:
    #     print('8th')
    # elif number == 9:
    #     print('9th')
    