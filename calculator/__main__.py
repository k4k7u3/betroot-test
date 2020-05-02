import random
import math
from init import init
from validation import validations

name = input('Здравствуйте! Введите ваше имя: ')
name = name.strip().capitalize()
# Основной цикл
while True:
    if init.flag == 0:
        init.input_operation = []
        init.input_number = []
        init.per_word = 0
        operation = input(
            f'{name}, выберите какую операцию Вы хотите произвести (для выхода введите "Exit"): ')
        operation = operation.strip().lower()
        if operation not in init.list_operation:
            print(f'{name}, Вы ввели некоректную операцию. Повторите попытку')
            continue
        if operation == 'exit':
            break
        elif operation == 'info':
            init.description_oper()
            continue
        elif operation == init.operation_sum:
            x = validations.input_chislo()
            y = validations.input_chislo()
            init.result = round(x + y, 3)
            print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', init.result)
            init.flag = 1
            continue
        elif operation == init.operation_min:
            init.x = validations.input_chislo()
            init.y = validations.input_chislo()
            init.result = round(init.x - init.y, 3)
            print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} {operation} {init.y} =', init.result)
            init.flag = 1
            continue
        elif operation == init.operation_umn:
            init.x = validations.input_chislo()
            init.y = validations.input_chislo()
            init.result = round(init.x * init.y, 3)
            print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} {operation} {init.y} =', init.result)
            init.flag = 1
            continue
        elif operation == init.operation_del:
            init.x = validations.input_chislo()
            while True:
                init.y = validations.input_chislo()
                if init.y == 0:
                    print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
                    continue
                break
            init.result = round(init.x / init.y, 3)
            print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} {operation} {init.y} =', init.result)
            flag = 1
            continue
        elif operation == init.operation_celdel:
            init.x = validations.input_chislo()
            while True:
                init.y = validations.input_chislo()
                if init.y == 0:
                    print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
                    continue
                break
            init.result = round(init.x // init.y, 3)
            print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} {operation} {init.y} =', init.result)
            init.flag = 1
            continue
        elif operation == init.operation_ostatok:
            init.x = validations.input_chislo()
            while True:
                init.y = validations.input_chislo()
                if init.y == 0:
                    print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
                    continue
                break
            init.result = round(init.x % init.y, 3)
            print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} {operation} {init.y} =', init.result)
            init.flag = 1
            continue
        elif operation == init.operation_step:
            init.x = validations.input_chislo()
            init.y = validations.input_chislo()
            init.result = round(init.x ** init.y, 3)
            print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} {operation} {init.y} =', init.result)
            init.flag = 1
            continue
        elif operation == init.operation_sqrt:
            while True:
                init.x = validations.input_chislo()
                if init.x < 0:
                    print("Мы не извлекаем корень с отрицательного числа! Может кто другой сможет, let's try = ) ")
                    continue
                break
            init.result = round(math.sqrt(init.x), 3)
            print(f'Вы ввели x = {init.x}. Результат {operation}({init.x}) =', init.result)
            init.flag = 1
            continue
        elif operation == init.operation_modul:
            init.x = validations.input_chislo()
            init.result = round(abs(init.x), 3)
            print(f'Вы ввели x = {init.x}. Результат {operation}({init.x}) =', init.result)
            init.flag = 1
            continue
        elif operation == init.operation_fact:
            while True:
                init.x = validations.input_chislo()
                if init.x < 0:
                    print('''Мы не находим факториал отрицательного числа! Может кто другой сможет, let's try = ) ''')
                    continue
                break
            init.result = round(math.factorial(init.x), 3)
            print(f'Вы ввели x = {init.x}. Результат {init.x}! =', init.result)
            init.flag = 1
            continue
        elif operation == init.operation_auto:
            while True:
                init.input_per = input('Введите операцию полностью (для выхода введите "Exit"): ')
                init.input_per = init.input_per.lower().strip().replace(' ', '')
                if init.input_per == '':
                    print('Вы ввели некоректное число')
                    continue
                elif init.operation_exit in init.input_per:
                    break
                if init.operation_sqrt in init.input_per:
                    init.input_operation.append('sqrt')
                    init.input_per = init.input_per.replace('sqrt', '')
                    init.per_word = 1
                elif init.operation_modul in init.input_per:
                    init.input_operation.append('abs')
                    init.input_per = init.input_per.replace('abs', '')
                    init.per_word = 1
                elif init.operation_fact in init.input_per:
                    init.input_operation.append('!')
                    init.input_per = init.input_per.replace('!', '')
                    init.per_word = 1
                elif init.operation_celdel in init.input_per:
                    init.input_operation.append('?')
                    init.input_per = init.input_per.replace('//', '?')
                return_all = validations.sort_string(init.input_per)
                if return_all == None:
                    continue
                init.input_number, init.input_operation = return_all
                if len(init.input_operation) < 1:
                    print('Вы ввели некоректное число')
                    init.input_operation = []
                    init.input_number = []
                    continue
                elif len(init.input_number) == 2:
                    if init.input_number[0] == '' or init.input_number[1] == '':
                        print('Вы ввели некоректное число')
                        init.input_operation = []
                        init.input_number = []
                        continue
                elif len(init.input_number) == 1 and init.per_word == 0:
                    print('Вы ввели некоректное число')
                    init.input_operation = []
                    init.input_number = []
                    continue
                if init.input_operation[0] == init.operation_sum:
                    init.x = init.input_number[0]
                    init.y = init.input_number[1]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    init.y = validations.auto_oper(init.y)
                    if init.y == 'Error':
                        continue
                    init.result = round(init.x + init.y, 3)
                    print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} + {init.y} =', init.result)
                    init.flag = 1
                    break
                elif init.input_operation[0] == init.operation_min:
                    init.x = init.input_number[0]
                    init.y = init.input_number[1]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    init.y = validations.auto_oper(init.y)
                    if init.y == 'Error':
                        continue
                    init.result = round(init.x - init.y, 3)
                    print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} - {init.y} =', init.result)
                    init.flag = 1
                    break
                elif init.input_operation[0] == init.operation_umn:
                    init.x = init.input_number[0]
                    init.y = init.input_number[1]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    init.y = validations.auto_oper(init.y)
                    if init.y == 'Error':
                        continue
                    init.result = round(init.x * init.y, 3)
                    print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} * {init.y} =', init.result)
                    init.flag = 1
                    break
                elif init.input_operation[0] == init.operation_del:
                    init.x = init.input_number[0]
                    init.y = init.input_number[1]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    init.y = validations.auto_oper(init.y)
                    if init.y == 0:
                        print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
                        continue
                    if init.y == 'Error':
                        continue
                    init.result = round(init.x / init.y, 3)
                    print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} / {init.y} =', init.result)
                    init.flag = 1
                    break
                elif init.input_operation[0] == '?':
                    init.x = init.input_number[0]
                    init.y = init.input_number[1]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    init.y = validations.auto_oper(init.y)
                    if init.y == 0:
                        print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
                        continue
                    if init.y == 'Error':
                        continue
                    init.result = round(init.x // init.y, 3)
                    print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} // {init.y} =', init.result)
                    init.flag = 1
                    break
                elif init.input_operation[0] == init.operation_ostatok:
                    init.x = init.input_number[0]
                    init.y = init.input_number[1]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    init.y = validations.auto_oper(init.y)
                    if init.y == 0:
                        print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
                        continue
                    if init.y == 'Error':
                        continue
                    init.result = round(init.x % init.y, 3)
                    print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} % {init.y} =', init.result)
                    init.flag = 1
                    break
                elif init.input_operation[0] == init.operation_step:
                    init.x = init.input_number[0]
                    init.y = init.input_number[1]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    init.y = validations.auto_oper(init.y)
                    if init.y == 'Error':
                        continue
                    init.result = round(init.x ** init.y, 3)
                    print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} ^ {init.y} =', init.result)
                    init.flag = 1
                    break
                elif init.input_operation[0] == init.operation_sqrt:
                    init.x = init.input_number[0]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    if init.x < 0:
                        print("Мы не извлекаем корень с отрицательного числа! Может кто другой сможет, let's try = ) ")
                        continue
                    init.result = round(math.sqrt(init.x), 3)
                    print(f'Вы ввели x = {init.x}. Результат sqrt({init.x}) =', init.result)
                    init.flag = 1
                    break
                elif init.input_operation[0] == init.operation_modul:
                    init.x = init.input_number[0]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    init.result = round(abs(init.x), 3)
                    print(f'Вы ввели x = {init.x}. Результат abs({init.x}) =', init.result)
                    init.flag = 1
                    break
                elif init.input_operation[0] == init.operation_fact:
                    init.x = init.input_number[0]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    if init.x < 0:
                        print(
                            '''Мы не находим факториал отрицательного числа! Может кто другой сможет, let's try = ) ''')
                        continue
                    init.result = round(math.factorial(init.x), 3)
                    print(f'Вы ввели x = {init.x}. Результат ({init.x})! =', init.result)
                    init.flag = 1
                    break
                elif init.input_per == 'exit':
                    break
    else:
        operation = input(
            'Ввести дальнейшую операцию или сбросить? (для cброса введите "clear", для описания операций введите "Info", для выхода введите "Exit"): ')
        operation = operation.strip().lower()
        print(init.result)
        if operation == 'exit':
            break
        elif operation == 'info':
            init.description_oper()
            continue
        elif operation == 'clear':
            init.result = 0
            init.flag = 0
            continue
        elif operation == init.operation_sum:
            init.z = validations.input_chislo()
            result1 = init.result
            init.result += init.z
            init.result = round(init.result, 3)
            print(f'Результат {result1} {operation} {init.z} =', init.result)
            continue
        elif operation == init.operation_min:
            init.z = validations.input_chislo()
            result1 = init.result
            init.result -= init.z
            init.result = round(init.result, 3)
            print(f'Результат {result1} {operation} {init.z} =', init.result)
            continue
        elif operation == init.operation_umn:
            init.z = validations.input_chislo()
            result1 = init.result
            init.result *= init.z
            init.result = round(init.result, 3)
            print(f'Результат {result1} {operation} {init.z} =', init.result)
            continue
        elif operation == init.operation_del:
            while True:
                init.z = validations.input_chislo()
                if init.z == 0:
                    print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
                    continue
                break
            result1 = init.result
            init.result /= init.z
            init.result = round(init.result, 3)
            print(f'Результат {result1} {operation} {init.z} =', init.result)
            continue
        elif operation == init.operation_celdel:
            while True:
                init.z = validations.input_chislo()
                if init.z == 0:
                    print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
                    continue
                break
            result1 = init.result
            init.result //= init.z
            init.result = round(init.result, 3)
            print(f'Результат {result1} {operation} {init.z} =', init.result)
            continue
        elif operation == init.operation_ostatok:
            while True:
                init.z = validations.input_chislo()
                if init.z == 0:
                    print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
                    continue
                break
            result1 = init.result
            init.result %= init.z
            init.result = round(init.result, 3)
            print(f'Результат {result1} {operation} {init.z} =', init.result)
            continue
        elif operation == init.operation_step:
            init.z = validations.input_chislo()
            result1 = init.result
            init.result **= init.z
            init.result = round(init.result, 3)
            print(f'Результат {result1} {operation} {init.z} =', init.result)
            continue
        elif operation == init.operation_sqrt:
            if init.result < 0:
                print("Мы не извлекаем корень с отрицательного числа! Может кто другой сможет, let's try = ) ")
                continue
            result1 = init.result
            init.result = round(math.sqrt(init.result), 3)
            print(f'Результат sqrt({result1}) =', init.result)
            continue
        elif operation == init.operation_modul:
            result1 = init.result
            init.result = round(abs(init.result), 3)
            print(f'Результат abs({result1}) =', init.result)
            continue
        elif operation == init.operation_fact:
            if init.result < 0:
                print("Мы не находим факториал отрицательного числа Может кто другой сможет, let's try = ) ")
                continue
            result1 = init.result
            init.result = round(math.factorial(init.result), 3)
            print(f'Результат abs({result1})! =', init.result)
            continue
        elif operation == init.operation_auto:
            while True:
                init.input_operation = []
                init.input_number = []
                init.input_per = input(
                    f'Введите операцию которую хотите сделать с результатом (для выхода введите "Exit"): {init.result} ')
                result1 = init.result
                init.result = str(init.result)
                init.input_per = init.result + init.input_per
                init.input_per = init.input_per.lower().strip().replace(' ', '')
                if init.input_per == '':
                    print('Вы ввели некоректное число')
                    continue
                elif init.operation_exit in init.input_per:
                    break
                elif init.operation_sqrt in init.input_per:
                    init.input_operation.append('sqrt')
                    init.input_per = init.input_per.replace('sqrt', '')
                elif init.operation_modul in init.input_per:
                    init.input_operation.append('abs')
                    init.input_per = init.input_per.replace('abs', '')
                elif init.operation_fact in init.input_per:
                    init.input_operation.append('!')
                    init.input_per = init.input_per.replace('!', '')
                elif init.operation_celdel in init.input_per:
                    init.input_operation.append('?')
                    init.input_per = init.input_per.replace('//', '?')
                return_all = validations.sort_string(init.input_per)
                if return_all == None:
                    continue
                init.input_number, init.input_operation = return_all
                if len(init.input_operation) < 1:
                    print('Вы ввели некоректное число')
                    init.input_operation = []
                    init.input_number = []
                    continue
                elif len(init.input_number) == 2:
                    if init.input_number[0] == '' or init.input_number[1] == '':
                        print('Вы ввели некоректное число')
                        init.input_operation = []
                        init.input_number = []
                        continue
                elif len(init.input_number) == 1 and init.per_word == 0:
                    print('Вы ввели некоректное число')
                    init.input_operation = []
                    init.input_number = []
                    continue
                if init.input_operation[0] == init.operation_sum:
                    init.x = init.input_number[0]
                    init.y = init.input_number[1]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    init.y = validations.auto_oper(init.y)
                    if init.y == 'Error':
                        continue
                    init.result = round(init.x + init.y, 3)
                    print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} + {init.y} =', init.result)
                    init.flag = 1
                    break
                elif init.input_operation[0] == init.operation_min:
                    init.x = init.input_number[0]
                    init.y = init.input_number[1]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    init.y = validations.auto_oper(init.y)
                    if init.y == 'Error':
                        continue
                    init.result = round(init.x - init.y, 3)
                    print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} - {init.y} =', init.result)
                    init.flag = 1
                    break
                elif init.input_operation[0] == init.operation_umn:
                    init.x = init.input_number[0]
                    init.y = init.input_number[1]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    init.y = validations.auto_oper(init.y)
                    if init.y == 'Error':
                        continue
                    init.result = round(init.x * init.y, 3)
                    print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} * {init.y} =', init.result)
                    init.flag = 1
                    break
                elif init.input_operation[0] == init.operation_del:
                    init.x = init.input_number[0]
                    init.y = init.input_number[1]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    init.y = validations.auto_oper(init.y)
                    if init.y == 0:
                        print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
                        continue
                    if init.y == 'Error':
                        continue
                    init.result = round(init.x / init.y, 3)
                    print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} / {init.y} =', init.result)
                    init.flag = 1
                    break
                elif init.input_operation[0] == '?':
                    init.x = init.input_number[0]
                    init.y = init.input_number[1]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    init.y = validations.auto_oper(init.y)
                    if init.y == 0:
                        print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
                        continue
                    if init.y == 'Error':
                        continue
                    init.result = round(init.x // init.y, 3)
                    print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} // {init.y} =', init.result)
                    init.flag = 1
                    break
                elif init.input_operation[0] == init.operation_ostatok:
                    init.x = init.input_number[0]
                    init.y = init.input_number[1]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    init.y = validations.auto_oper(init.y)
                    if init.y == 0:
                        print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
                        continue
                    if init.y == 'Error':
                        continue
                    init.result = round(init.x % init.y, 3)
                    print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} % {init.y} =', init.result)
                    init.flag = 1
                    break
                elif init.input_operation[0] == init.operation_step:
                    init.x = init.input_number[0]
                    init.y = init.input_number[1]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    init.y = validations.auto_oper(init.y)
                    if init.y == 'Error':
                        continue
                    init.result = round(init.x ** init.y, 3)
                    print(f'Вы ввели x = {init.x} , y = {init.y}. Результат {init.x} ^ {init.y} =', init.result)
                    init.flag = 1
                    break
                elif init.input_operation[0] == init.operation_sqrt:
                    init.x = init.input_number[0]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    if init.x < 0:
                        print("Мы не извлекаем корень с отрицательного числа! Может кто другой сможет, let's try = ) ")
                        continue
                    init.result = round(math.sqrt(init.x), 3)
                    print(f'Вы ввели x = {init.x}. Результат sqrt({init.x}) =', init.result)
                    init.flag = 1
                    break
                elif init.input_operation[0] == init.operation_modul:
                    init.x = init.input_number[0]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    init.result = round(abs(init.x), 3)
                    print(f'Вы ввели x = {init.x}. Результат abs({init.x}) =', init.result)
                    init.flag = 1
                    break
                elif init.input_operation[0] == init.operation_fact:
                    init.x = init.input_number[0]
                    init.x = validations.auto_oper(init.x)
                    if init.x == 'Error':
                        continue
                    if init.x < 0:
                        print(
                            '''Мы не находим факториал отрицательного числа! Может кто другой сможет, let's try = ) ''')
                        continue
                    init.result = round(math.factorial(init.x), 3)
                    print(f'Вы ввели x = {init.x}. Результат ({init.x})! =', init.result)
                    init.flag = 1
                    break
                elif init.input_per == 'exit':
                    break
        else:
            print(f'{name}, Вы ввели некоректную операцию. Повторите попытку')
            continue

print(f'{name}, спасибо, что воспользовались услугами нашего калькулятора! Заходите еще раз!')