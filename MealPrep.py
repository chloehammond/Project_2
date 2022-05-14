def main():
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
            elif beef_types == 'ground':
                buns = input('Do you have any buns?').lower()
                if buns == 'y' or buns == 'yes':
                    print('You should make hamburgers')
                elif buns == 'n' or 'no':
                    rice = input('Do you have any rice?').lower()
                    if rice == 'y' or rice == 'yes':
                        print('You should make a casserole')
                    elif rice == 'n' or rice == 'no':
                        print('You should make Chili')
                    else:
                        print('Invalid response')
                else:
                    print('Invalid response')
            elif beef_types == 'roast':
                potatoes = input('Do you have any potatoes?').lower()
                if potatoes == 'y' or potatoes == 'yes':
                    vegetables = input('Do you have any vegetables?').lower()
                    if vegetables == 'y' or vegetables == 'yes':
                        print('You should make Pot Roast and veggies with Mashed Potatoes')
                    elif vegetables == 'n' or vegetables == 'no':
                        print('You should make Roasted Potatoes and Meat')
                    else:
                        print('Invalid response')
                elif potatoes == 'n' or potatoes == 'no':
                    vegetables = input('Do you have any vegetables?').lower()
                    if vegetables == 'y' or vegetables == 'yes':
                        print('You should make Meat and Veggie Soup')
                    elif vegetables == 'n' or vegetables == 'no':
                        print('You should make Pot Roast')
                    else:
                        print('Invalid response')
                else:
                    print('Invalid response')
            else:
                print('Invalid response')
        elif meat_options == 'chicken':
            chicken_type = input('Is your chicken whole or pieces?').lower()
            if chicken_type == 'whole':
                pasta = input('Do you have any pasta?').lower()
                if pasta == 'y' or pasta == 'yes':
                    print('You should make Chicken Pasta Casserole')
                elif pasta == 'n' or pasta == 'no':
                    rice = input('Do you have any rice?').lower()
                    if rice == 'y' or rice == 'yes':
                        vegetables = input('Do you have any vegetables?').lower()
                        if vegetables == 'y' or vegetables == 'yes':
                            print('You should make Stir Fry')
                        elif vegetables == 'n' or vegetables == 'no':
                            print('You should make Chicken Rice Casserole')
                        else:
                            print('Invalid Response')
                    elif rice == 'n' or rice == 'no':
                        print('You should make Smoked Chicken')
                    else:
                        print('Invalid response')
                else:
                    print('Invalid response')
            elif chicken_type == 'pieces':
                vegetables = input('Do you have any vegetables?').lower()
                if vegetables == 'y' or vegetables == 'yes':
                    print('You should make Grilled Chicken and Veggies')
                elif vegetables == 'n' or vegetables == 'no':
                    pasta = input('Do you have any pasta?').lower()
                    if pasta == 'y' or pasta == 'yes':
                        print('You should make Chicken Piccata')
                    elif pasta == 'n' or pasta == 'no':
                        print('You should make Fried Chicken')
                    else:
                        print('Invalid response')
                else:
                    print('Invalid response')
            else:
                print('Invalid response')
        elif meat_options == 'other meat':
            eggs = input('Do you have any eggs?').lower()
            if eggs == 'y' or eggs == 'yes':
                print('You should make Meat and Eggs')
            elif eggs == 'n' or eggs == 'no':
                vegetables = input('Do you have any vegetables?').lower()
                if vegetables == 'y' or vegetables == 'yes':
                    print('You should make Meat and Veggies')
                elif vegetables == 'n' or vegetables == 'no':
                    pasta = input('Do you have any pasta?').lower()
                    if pasta == 'y' or pasta == 'yes':
                        print('You should make Meat and Pasta')
                    elif pasta == 'n' or pasta == 'no':
                        print('Just meat tonight!')
                    else:
                        print('Invalid response')
                else:
                    print('Invalid response')
            else:
                print('Invalid response')
        else:
            print('Invalid response')
    elif meat == 'n' or meat == 'no':
        vegetables = input('Do you have any vegetables?').lower()
        if vegetables == 'y' or vegetables == 'yes':
            eggplant = input('Do you have any eggplants?').lower()
            if eggplant == 'y' or eggplant == 'yes':
                tomatoes = input('Do you have any tomatoes?').lower()
                if tomatoes == 'y' or tomatoes == 'yes':
                    print('You should make Eggplant Parmesan')
                elif tomatoes == 'n' or tomatoes == 'no':
                    print('You should make Roasted Eggplant')
                else:
                    print('Invalid response')
            elif eggplant == 'n' or eggplant == 'no':
                print('You should make Vegetable Soup')
            else:
                print('Invalid response')
        elif vegetables == 'n' or vegetables == 'no':
            eggs = input('Do you have any eggs?').lower()
            if eggs == 'y' or eggs == 'yes':
                onions_and_peppers = input('Do you have any onions and peppers?').lower()
                if onions_and_peppers == 'y' or onions_and_peppers == 'yes':
                    print('You should make a Frittata')
                elif onions_and_peppers == 'n' or onions_and_peppers == 'no':
                    print('You should make an Omelette')
                else:
                    print('Invalid response')
            elif eggs == 'n' or eggs == 'no':
                bread = input('Do you have any bread?').lower()
                if bread == 'y' or bread == 'yes':
                    print('You should make a PB & J sandwich')
                elif bread == 'n' or bread == 'no':
                    print('Your cupboard is bare!')
                else:
                    print('Invalid response')
            else:
                print('Invalid response')
        else:
            print('Invalid response')
    else:
        print('Invalid response')


if __name__ == '__main__':
    main()
