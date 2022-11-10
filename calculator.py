class Calculator:
    def __init__(self, battery: int = 100, filename=None):
        self.battery = battery
        self.filename = filename
        self.check_battery()

    def _get_content(self):
        with open(self.filename, "r") as f:
            lines = f.readlines()
            return [line.split(",") for line in lines]

    def _ensure_casted_data(self):
        raw_data = self._get_content()
        data = []
        for d in raw_data:
            data.append([float(n) for n in d])
        return data

    def check_battery(self):
        if self.battery <= 0:
            raise NoBatteryError("The battery has run out")

    def charge_battery(self, charge):
        if self.battery + charge > 100:
            self.battery = 100
        else:
            self.battery += charge

    def avg_file(self):
        numbers = self._ensure_casted_data()
        return [sum(n) / len(n) for n in numbers]

    def add(self, *args):
        self.check_battery()
        self.battery -= 1
        result_add = 0

        for number_to_add in args:
            result_add += number_to_add
        return result_add

    def subtract(self, *args):
        self.check_battery()
        self.battery -= 1
        result_subtract = args[0]

        for number_to_subtract in args[1:]:
            result_subtract -= number_to_subtract
        return result_subtract

    def multiply(self, multiplicand, multiplier):
        self.check_battery()
        self.battery -= 1
        return multiplicand * multiplier

    def divide(self, dividend, divisor):
        self.check_battery()
        self.battery -= 1
        if divisor == 0:
            raise ValueError
        return dividend / divisor

    def square(self, number):
        self.check_battery()
        self.battery -= 1
        return number ** 2

    def n_to_power_of(self, number, power):
        self.check_battery()
        self.battery -= 1
        return number ** power

    def is_even(self, number):
        self.check_battery()
        self.battery -= 1
        return number % 2 == 0


class NoBatteryError(Exception):
    pass




