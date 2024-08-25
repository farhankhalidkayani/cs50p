class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.__capacity = capacity
        self.__filled = 0

    def __str__(self):
        res = ""
        for i in range(self.__filled):
            res += "🍪"
        return res

    def deposit(self, n):
        if n <= self.__capacity - self.__filled:
            self.__filled += n
        else:
            raise ValueError

    def withdraw(self, n):
        if n <= self.__filled:
            self.__filled -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self.__capacity

    @property
    def size(self):
        return self.__filled
