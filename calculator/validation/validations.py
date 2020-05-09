from init import init

# Функция для вводимого числа
def input_chislo():
    while True:
        init.input_per = input('Введите число: ')
        init.input_per = init.input_per.strip().replace(' ', '')
        if init.input_per == '':
            print('Вы ввели некоректное число!')
            continue
        elif init.input_per[0] == '-' and init.input_per.count('-') == 1:
            init.input_per = init.input_per.replace('-', '')
            negative_number = 1
        else:
            negative_number = 0
        if init.input_per.isdigit() == False:
            if init.input_per.count('.') == 0 or init.input_per.count('.') > 1:
                print('Вы ввели некоректное число!')
                continue
            elif init.input_per.count('.') == 1:
                input_per1 = init.input_per
                init.input_per = init.input_per.replace('.', '')
                if init.input_per.isdigit() == False:
                    print('Вы ввели некоректное число!')
                    continue
                else:
                    init.input_per = input_per1
                    init.input_per = float(init.input_per)
                    if negative_number == 1:
                        init.input_per = init.input_per * -1
                    break
        else:
            init.input_per = int(init.input_per)
            if negative_number == 1:
                init.input_per = init.input_per * -1
            break
    return init.input_per


# Функция для автоматического ввода
def auto_oper(input_value):
    if input_value[0] == '-' and input_value.count('-') == 1:
        input_value = input_value.replace('-', '')
        negative_number = 1
    else:
        negative_number = 0
    if input_value.isdigit() == False:
        if input_value.count('.') == 0 or input_value.count('.') > 1:
            print('Вы ввели некоректное число!')
            input_value = 'Error'
        elif input_value.count('.') == 1:
            input_value1 = input_value
            input_value = input_value.replace('.', '')
            if input_value.isdigit() == False:
                print('Вы ввели некоректное число!')
                input_value = 'Error'
            else:
                input_value = input_value1
                input_value = float(input_value)
                if negative_number == 1:
                    input_value = input_value * -1
                return input_value
    else:
        input_value = int(input_value)
        if negative_number == 1:
            input_value = input_value * -1
    return input_value

# Функция для сортировки вводимой строки в автоматическом режиме


def sort_string(s):
    flag1 = 0
    num = ''
    number = []
    for i in s:
        if i.isdigit() == True:
            num += i
            flag1 = 1
        elif i == '-' and flag1 == 0:
            num += i
        elif i == '.' and flag1 == 1:
            num += i
        elif i in init.list_operation and flag1 == 1:
            init.input_operation.append(i)
            number.append(num)
            num = ''
            flag1 = 0
        elif i in init.list_operation and flag1 == 0:
            init.input_operation.append(i)
        else:
            print('Вы ввели неверное число')
            return None
    number.append(num)
    return number, init.input_operation

