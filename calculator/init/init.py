result = 0
flag = 0
x = 0  # Первое вводимое число
y = 0  # Второе вводимое число
z = 0  # Третье вводимое число
input_per = ''  # Переменная для функции
input_operation = []
input_number = []
per_word = 0

operation_sum = '+'
operation_min = '-'
operation_umn = '*'
operation_del = '/'
operation_celdel = '//'
operation_ostatok = '%'
operation_step = '^'
operation_sqrt = 'sqrt'
operation_modul = 'abs'
operation_fact = '!'
operation_auto = 'auto'
operation_exit = 'exit'
operation_info = 'info'

list_operation = [operation_sum, operation_min, operation_umn, operation_del, operation_celdel, operation_ostatok,
                  operation_step, operation_sqrt, operation_modul, operation_fact, operation_auto, operation_exit,
                  operation_info, '?']

# Функция для вывода информации об операциях
def description_oper():
    print('+' + '\t' * 2 + '- сложение;')
    print('-' + '\t' * 2 + '- вычитание;')
    print('*' + '\t' * 2 + '- умножение;')
    print('/' + '\t' * 2 + '- деление;')
    print('//' + '\t' * 2 + '- получение целой части от деления;')
    print('%' + '\t' * 2 + '- получение остатка от деления;')
    print('^' + '\t' * 2 + '- возведение числа в степень;')
    print('sqrt' + '\t' + '- извлечение квадратного корня;')
    print('abs n' + '\t' + '- модуль числа, где n - введеное число;')
    print('!' + '\t' * 2 + '- факториал числа, n! - где n введеное число;')
    print('auto' + '\t' + '- позволяет вводить команду полностью (доступна только одна операция!!!)')