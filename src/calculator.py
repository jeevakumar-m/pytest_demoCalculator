import src.constants as const


class Calculator:

    def __init__(self):
        self.alb = const.DEFAULT_NUM1_LOWER_BOUNDARY
        self.aub = const.DEFAULT_NUM1_UPPER_BOUNDARY
        self.blb = const.DEFAULT_NUM2_LOWER_BOUNDARY
        self.bub = const.DEFAULT_NUM2_UPPER_BOUNDARY

    def __add(self, a, b):
        if self.__check_boundary(a, b):
            return a + b
        else:
            raise Exception("boundary mismatch")

    def __sub(self, a, b):
        if self.__check_boundary(a, b):
            return a - b
        else:
            raise Exception("boundary mismatch")

    def __mul(self, a, b):
        if self.__check_boundary(a, b):
            return a * b
        else:
            raise Exception("boundary mismatch")

    def __div(self, a, b):
        if self.__check_boundary(a, b):
            if b > 0:
                return a / b
            else:
                raise Exception("avoiding divide by zero due to infinite result")
        else:
            raise Exception("boundary mismatch")

    def set_num_boundary(self, a_lower_bound, a_upper_bound, b_lower_bound, b_upper_bound):
        self.alb = a_lower_bound
        self.aub = a_upper_bound
        self.blb = b_lower_bound
        self.bub = b_upper_bound

    def __check_boundary(self, a, b):
        if (self.aub >= a >= self.alb) and (self.bub >= b >= self.blb):
            return True
        else:
            return False

    def calculate(self, a, b, operation):
        if operation == const.ADDITION:
            return self.__add(a, b)
        elif operation == const.SUBTRACTION:
            return self.__sub(a, b)
        elif operation == const.MULTIPLICATION:
            return self.__mul(a, b)
        elif operation == const.DIVISION:
            return self.__div(a, b)
