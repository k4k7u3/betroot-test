class Mathematician:

    def square_nums(self, s):
        square_list = []
        for i in s:
            if type(i) != int:
                return None
            square_list.append(i * i)
        return square_list

    def remove_positives(self, s):
        negative = []
        for i in s:
            if type(i) != int:
                return None
            if i < 0:
                negative.append(i)
        return negative

    def filter_leaps(self, s):
        leaps_years = []
        for i in s:
            if type(i) != int:
                return None
            if i % 4 == 0 or (i % 100 != 0 and i % 400 == 0):
                leaps_years.append(i)
        return leaps_years


x = Mathematician()
print(x.square_nums([3, 4, 5, 6]))
print(x.remove_positives([3, -4, 12, 6, -48, -1]))
print(x.filter_leaps([2001, 1884, 1995, 2020]))