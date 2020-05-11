all_purchase = {'Other' : []}
category = [all_purchase]

def input_mode(input_text):
    x = input(input_text)
    x = x.capitalize().replace(' ', '')
    return x

def input_mode2(input_text2):
    y = input(input_text2)
    y = y.capitalize().strip()
    return y

while True:
    operation = input_mode("Hey! Choose mode: (1 - control category; 2 - control purchase; 'exit' - exit): ")
    if operation == '1':
        while True:
            print("Your list of category:", category)
            category_menu = input_mode("What do you want to do? (1 - choose category; 2 - add category; 3 - delete category; 'exit' - exit): ")
            if category_menu == 'Exit':
                break
            elif category_menu == '1':
                while True:
                    name_category = input_mode2(f"This is your category {category}. Which do you choose? ('other',.., 'exit' - exit) : ")
                    if name_category == 'Exit':
                        break
                    elif name_category not in all_purchase:
                        print("We don't have this category! Try again!")
                        continue
                    elif name_category in all_purchase:
                        temporary_purchase = all_purchase.get(name_category)
                        while True:
                            print(temporary_purchase)
                            operation_with_purchase = input_mode("What do you want to do with this purchase? (1 - add new purchase; 2 - delete some purchase; 3 - delete all purchase; 'exit' - exit): ")
                            if operation_with_purchase == 'Exit':
                                break
                            elif operation_with_purchase == '1':
                                if len(temporary_purchase) >= 10:
                                    print("We can only have 10 purchases in a category. Sorry")
                                    continue
                                else:
                                    name_new_purchase = input("Input new purchase: ")
                                    name_new_purchase = name_new_purchase.strip()
                                    temporary_purchase.append(name_new_purchase)
                                    continue
                            elif operation_with_purchase == '2':
                                del_purchase = input("Input name of purchase which you want delete: ")
                                del_purchase = del_purchase.strip()
                                if del_purchase not in temporary_purchase:
                                    print("We don't have this purchase! Try again")
                                    continue
                                elif del_purchase in temporary_purchase:
                                    temporary_purchase.remove(del_purchase)
                                    continue
                            elif operation_with_purchase == '3':
                                temporary_purchase.clear()
                                continue
                            else:
                                print("We don't support this operation. Try again")
                                continue
            elif category_menu == '2':
                name_new_category = input_mode2("Input a name for the new category: ")
                all_purchase[name_new_category] = []
                continue
            elif category_menu == '3':
                while True:
                    name_del_category = input_mode2("Input a name for the new category: ")
                    if name_del_category not in all_purchase:
                        print("We don't have this category! Try again")
                        continue
                    elif name_del_category in all_purchase:
                        temporary_purchase = all_purchase.get(name_del_category)
                        if len(temporary_purchase) != 0:
                            verification = input("Your category is not empty. Are you sure? (1 - yes, 2 - No): ")
                            if verification == '1':
                                all_purchase.pop(name_del_category)
                                break
                            elif verification == '2':
                                break
                        else:
                            all_purchase.pop(name_del_category)
                            break
            else:
                print("Incorrect input. Try again!")
                continue
    elif operation == '2':
        temporary_purchase = all_purchase.get('Other')
        if temporary_purchase == None:
            all_purchase["Other"] = []
            temporary_purchase = all_purchase.get('Other')
        print(f'This is your list of all_purchase: {temporary_purchase}')
        while True:
            print(temporary_purchase)
            operation_with_purchase = input_mode(
                "What do you want to do with this purchase? (1 - add new purchase; 2 - delete some purchase; 3 - delete all purchase; 'exit' - exit): ")
            if operation_with_purchase == 'Exit':
                break
            elif operation_with_purchase == '1':
                if len(temporary_purchase) >= 10:
                    print("We can only have 10 purchases in a category. Sorry")
                    continue
                else:
                    name_new_purchase = input("Input new purchase: ")
                    name_new_purchase = name_new_purchase.strip()
                    temporary_purchase.append(name_new_purchase)
                    continue
            elif operation_with_purchase == '2':
                del_purchase = input("Input name of purchase which you want delete: ")
                del_purchase = del_purchase.strip()
                if del_purchase not in temporary_purchase:
                    print("We don't have this purchase! Try again")
                    continue
                elif del_purchase in temporary_purchase:
                    temporary_purchase.remove(del_purchase)
                    continue
    elif operation == 'Exit':
        break
    else:
        print("We don't have this mode. Try again!!!")
        continue
print('Thank you! Good Bye!!! =) ')