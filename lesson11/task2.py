class Mathematician:
    def square_nums(self, s):
        self.square_list = []
        for i in s:
            if type(i) != int:
                return None
            self.square_list.append(i * i)
        return self.square_list

    def remove_positives(self, s):
        self.negative = []
        for i in s:
            if type(i) != int:
                return None
            if i < 0:
                self.negative.append(i)
        return self.negative

    def filter_leaps(self, s):
        self.leaps_years = []
        for i in s:
            if type(i) != int:
                return None
            if i % 4 == 0 or (i % 100 != 0 and i % 400 == 0):
                self.leaps_years.append(i)
        return self.leaps_years


x = Mathematician()
print(x.square_nums([3, 4, 5, 6]))
print(x.remove_positives([3, -4, 12, 6, -48, -1]))
print(x.filter_leaps([2001, 1884, 1995, 2020]))