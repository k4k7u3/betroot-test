class TVController:
    channels = ["BBC", "Discovery", "TV1000"]
    num_channel = 0
    choise_channel = ''

    def first_channel(self):
        self.num_channel = 1
        self.choise_channel = self.channels[self.num_channel -1]
        self.print_channel(self.choise_channel)

    def last_channel(self):
        self.num_channel = len(self.channels)
        self.choise_channel = self.channels[self.num_channel-1]
        self.print_channel(self.choise_channel)

    def turn_channel(self, num):
        if num > len(self.channels):
            print("Incorect channel")
        else:
            self.num_channel = num
            self.choise_channel = self.channels[int(num) - 1]
            self.print_channel(self.choise_channel)

    def next_channel(self):
        if self.num_channel == len(self.channels):
            self.num_channel = 1
            self.choise_channel = self.channels[0]
            self.print_channel(self.choise_channel)
        else:
            self.num_channel += 1
            self.choise_channel = self.channels[self.num_channel - 1]
            self.print_channel(self.choise_channel)

    def previous_channel(self):
        if self.num_channel == 1:
            self.num_channel = 3
            self.choise_channel = self.channels[self.num_channel-1]
            self.print_channel(self.choise_channel)
        else:
            self.num_channel -= 1
            self.choise_channel = self.channels[self.num_channel - 1]
            self.print_channel(self.choise_channel)

    def current_channel(self):
        self.choise_channel = self.channels[self.num_channel - 1]
        self.print_channel(self.choise_channel)

    def is_exist(self, name):
        if name in self.channels:
            print("Yes")
        else:
            print("No")
        pass

    def print_channel(self, choise_channel):
        print(f"Channel: {self.choise_channel}")

my_tv= TVController()
my_tv.first_channel()
my_tv.last_channel()
my_tv.turn_channel(3)
my_tv.next_channel()
my_tv.next_channel()
my_tv.next_channel()
my_tv.previous_channel()
my_tv.previous_channel()
my_tv.previous_channel()
my_tv.current_channel()
my_tv.is_exist("blabla")