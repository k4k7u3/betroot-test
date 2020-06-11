import sys
sys.path.insert(0, "D:\\github_test\\betroot-test")
from lesson15 import mymod

print(mymod.count_lines("task3.txt"))
print(mymod.count_chars("task3.txt"))
print(mymod.test("task3.txt"))

print(sys.path)

# Does your PYTHONPATH need to include the directory where you created mymod.py? -yes