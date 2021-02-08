import math


class Fungi1:  # Middle temperature most fast decomposition rate
    c1 = 2.123
    c2 = -0.4249

    def __init__(self, extension_rate, environment):
        self.extension_rate = extension_rate
        self.moisture = environment.moisture
        self.dr = 0.0  # decomposition rate
        self.number = 1.0  # The total number

    def set_number(self, time_interval):
        self.number = self.number + self.extension_rate * time_interval

    def set_dr(self, environment):
        self.dr = self.c1 * self.extension_rate * math.exp(self.c2 * self.moisture)

        if 40 > environment.temperature > 25:
            self.dr = self.dr * 0.8
        elif 15 < environment.temperature <= 25:
            self.dr = self.dr * 1.0
        elif 10 <= environment.temperature < 15:
            self.dr = self.dr * 0.6
        elif 0 < environment.temperature < 10:
            self.dr = self.dr * 0.35
        elif 0 >= environment.temperature:
            self.dr = self.dr * 0.1
        elif environment.temperature > 40:
            self.dr = self.dr * 0.4

        if environment.wood_number < self.number:
            self.dr = self.dr * (environment.wood_number / self.number)


class Environment:
    def __init__(self, moisture, temperature, wood_number):
        self.moisture = moisture
        self.temperature = temperature
        self.wood_number = wood_number

    def set_wood_number(self, fungi, time_interval):
        self.wood_number = self.wood_number - fungi.dr * time_interval
