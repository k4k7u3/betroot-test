import sys

print(sys.path)

# Is it possible to change it from within Python?
# Answer: Если я правильно понял вопрос: то да,  можно изменить этот список). Как и обычный список мы можем удалять и добавлять элементы списка

sys.path.append("D:\\github_test\\betroot-test\\lesson17")
print(sys.path)
sys.path.remove("D:\\github_test")
print(sys.path)

#  If so, does it affect where Python looks for module files?
# Answer: ну да, просто можно добавить отдельный каталог для поиска подключаемого модуля