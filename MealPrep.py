print('Welcome to the meal prep program!')
print("Let's see what you can make!")

meat = input('Do you have any meat?').lower()

if meat == 'y' or meat == 'yes':
    meat_options = input('Do you have beef, chicken, or other meat?').lower()
    if meat_options == 'beef':
        beef_types = input('Do you have steak, ground, or roast?').lower()
        if beef_types == 'steak':
            potatoes = input('Do you have any potatoes?').lower()
            if potatoes == 'y' or potatoes == 'yes':
                salad = input('Do you have any salad?').lower()
                if salad == 'y' or salad == 'yes':
                    print('You should make Steak, Baked Potatoes, and Salad.')
                elif salad == 'n' or salad == 'no':
                    fruit = input('Do you have any fruit?').lower()
                    if fruit == 'y' or fruit == 'yes':
                        print('You should have Steak, Baked Potatoes, and Fruit.')
                    elif fruit == 'n' or fruit == 'no':
                        print('You should make Steak and Potato Hash.')
                    else:
                        print('Invalid response')
                else:
                    print('Invalid response')
            elif potatoes == 'n' or potatoes == 'no':
                salad = input('Do you have any salad?').lower()
                if salad == 'y' or salad == 'yes':
                    print('You should make Steak Salad.')
                elif salad == 'n' or 'no':
                    print('You should make a Steak Sandwich')
                else:
                    print('Invalid response')
            else:
                print('Invalid response')
        elif beef_types == ground:
            buns = input('Do you have any buns?').lower()
            if buns == 'y' or buns == 'yes':
                print('You should make hamburgers')
            elif buns == 'n' or 'no':
