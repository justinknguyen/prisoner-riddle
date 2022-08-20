import random

number = int(input("\nWhat is your prisoner number? "))

keys = [i for i in range(1,101)]
values = [i for i in range(1,101)]
random.shuffle(values)
box = dict(zip(keys, values))

print("\nEnter '0' to quit.")
print("Enter 'help' to see your opened boxes.\n")

count = 0
opened = {}
while 1:
    check = input("Enter a number (1-100): ")
    if count > 50:
        print("You die!")
        break
    try:
        if check == 'help':
            print("You've opened",count,"boxes:", end=' ')
            for key, value in opened.items():
                print(str(key)+"("+str(value)+")", end=', ')
            print("")
        elif int(check) in box and not int(check) in opened:
            count += 1
            print(box[int(check)])
            opened[int(check)] = box[int(check)]
            if box[int(check)] == number:
                print("Congrats! You found your number",number,"in",count,"tries.")
                break
        elif int(check) in opened:
            print("You've already opened this box. Enter 'help' to view your opened boxes.")
        elif int(check) == 0:
            break
        else:
            raise ValueError

    except ValueError:
        print("Enter a valid number between and including 1-100.")