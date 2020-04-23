# Вариант 1 в лоб и очень примитивно т.е. печатаем тупо принтами
print('method 1:')
print('#'*9, end='\n')
print('#','#', sep=' '*7, end='\n')
print('#','#', sep=' '*7, end='\n')
print('#','#', sep=' '*7, end='\n')
print('#'*9, end='\n'*2)

print('#','#', sep=' '*7, end='\n')
print('#','#', sep=' '*7, end='\n')
print('#'*9, end='\n')
print('#','#', sep=' '*7, end='\n')
print('#','#', sep=' '*7, end='\n'*2)

#Вариант второй програма становится красивее ( имхо =)  
print('method 2:')
b = '#'*9
a = '#' + ' '*7 + '#'
print(b)
print(a)
print(a)
print(a)
print(b + '\n')

print(a)
print(a)
print(b)
print(a)
print(a + '\n')

# Вариант с использованием цикла но с одним принтом - потому что во втором примере не получается использовать print(a * 3)
print('method 3:')
text = '#' + ' '*7 + '#'
no_change = [1,2,3]
no_change1 = 2

for i in range(5):
    if i not in no_change:
        print(text.replace(' ', '#'))
    else:
        print(text)

print()

for i in range(5):
    if i == no_change1:
        print(text.replace(' ', '#'))
    else:
        print(text)

#Вариант с двумя принтами просто
print('#'*9 + '\n' + ('#' + '\t'*2 + '#' + '\n')*3 + '#'*9)
print()
print(('#' + '\t'*2 + '#' + '\n')*2 + '#'*9 + '\n' + ('#' + '\t'*2 + '#' + '\n')*2)