available_parts = ['computer', 'mouse', 'keyboard', 'table', 'cable', 'hdmi']
current_choice = "_"
computer_parts = []  # create empty list

while current_choice != '0':
    if current_choice in '123456':
        print('adding {} '.format(current_choice))
        print(id(computer_parts))
        if current_choice == '1':
            computer_parts.append("computer")
        elif current_choice == '2':
            computer_parts.append("mouse")
        elif current_choice == '3':
            computer_parts.append("keyboard")
        elif current_choice == '4':
            computer_parts.append("table")
        elif current_choice == '5':
            computer_parts.append("cable")
        elif current_choice == '6':
            computer_parts.append("hdmi")

    else:
        print('add option from the list below')
        for part in available_parts:
            print("{0}:{1}".format(available_parts.index(part) + 1, part))
        for number, part in enumerate(available_parts):
            print("{0}:{1}".format(number + 1, part))
    current_choice = input()
else:
    print(computer_parts)
    print(id(computer_parts))
