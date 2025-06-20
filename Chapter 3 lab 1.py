#Chad Collard
#Chapter 3-1
#6/20/2025
print("                    Numeric Workday Translator")

user_input_num = int(input ("Please enter day of the week desired (1-7): "))
print(user_input_num)

if user_input_num == 1:
    print("Monday")
elif user_input_num == 2: 
    print("Tuesday")
elif user_input_num == 3:
    print("Wednesday")
elif user_input_num == 4:
    print("Thursday")
elif user_input_num == 5:
    print("Friday")
elif user_input_num == 0:
    print("Weekend")
elif user_input_num == 6:
    print("Weekend")
elif user_input_num == 7:
    print("Weekend")
else: 
    print("invalid")
