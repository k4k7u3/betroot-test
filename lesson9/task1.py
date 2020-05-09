new_text_file = open('myfile.txt', 'w+')
new_text_file.write('Hello file world! =)\n')
new_text_file.close()

read_text_file = open('myfile.txt') # если не указан параметр, то по умолчанию 'r' - read
print(read_text_file.read())
read_text_file.close()

# Does the new file show up in the directory where you ran your scripts? - да, файл создается в той категории, в которой находится наш исполняемый файл

# What if you add a different directory path to the filename passed to open? - если этого файла нет в нашей директории, то выдаст ошибку NotFoundError
# Но мы можем указать путь через директории например: open('..\README.md')
