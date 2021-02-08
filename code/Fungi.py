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

        self.dr = self.dr * math.log2(self.number)

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

        if environment.wood_number < (self.number * 2):
            self.dr = self.dr * (environment.wood_number / (self.number * 2))


class Fungi2:  # High temperature most fast decomposition rate
    c1 = 1.877
    c2 = 0.5152

    def __init__(self, extension_rate, environment):
        self.extension_rate = extension_rate
        self.moisture = environment.moisture
        self.dr = 0.0  # decomposition rate
        self.number = 1.0  # The total number

    def set_number(self, time_interval):
        self.number = self.number + self.extension_rate * time_interval

    def set_dr(self, environment):
        self.dr = self.c1 * self.extension_rate * math.exp(self.c2 * self.moisture)

        self.dr = self.dr * math.log2(self.number)

        if 35 > environment.temperature > 25:
            self.dr = self.dr * 1.0
        elif 15 < environment.temperature <= 25:
            self.dr = self.dr * 0.85
        elif 10 <= environment.temperature < 15:
            self.dr = self.dr * 0.6
        elif 0 < environment.temperature < 10:
            self.dr = self.dr * 0.3
        elif 0 >= environment.temperature:
            self.dr = self.dr * 0.1
        elif environment.temperature > 35:
            self.dr = self.dr * 0.8

        if environment.wood_number < (self.number * 2):
            self.dr = self.dr * (environment.wood_number / (self.number * 2))


class Fungi3:  # Low temperature most fast decomposition rate
    c1 = 3.553
    c2 = 0.7636

    def __init__(self, extension_rate, environment):
        self.extension_rate = extension_rate
        self.moisture = environment.moisture
        self.dr = 0.0  # decomposition rate
        self.number = 1.0  # The total number

    def set_number(self, time_interval):
        self.number = self.number + self.extension_rate * time_interval

    def set_dr(self, environment):
        self.dr = self.c1 * self.extension_rate * math.exp(self.c2 * self.moisture)

        self.dr = self.dr * math.log2(self.number)

        if 40 > environment.temperature > 25:
            self.dr = self.dr * 0.65
        elif 15 < environment.temperature <= 25:
            self.dr = self.dr * 0.85
        elif 10 <= environment.temperature < 15:
            self.dr = self.dr * 1.0
        elif 0 < environment.temperature < 10:
            self.dr = self.dr * 0.8
        elif 0 >= environment.temperature:
            self.dr = self.dr * 0.3
        elif environment.temperature > 40:
            self.dr = self.dr * 0.4

        if environment.wood_number < (self.number * 2):
            self.dr = self.dr * (environment.wood_number / (self.number * 2))


class Environment:
    def __init__(self, moisture, temperature, wood_number):
        self.moisture = moisture
        self.temperature = temperature
        self.wood_number = wood_number
        self.fungi1_density = self.fungi2_density = self.fungi3_density = 1 / 3

    def set_moisture(self, new_moisture):
        self.moisture = new_moisture

    def set_temperature(self, new_temperature):
        self.temperature = new_temperature

    def set_fungi_density(self, fungi1, fungi2, fungi3):
        total = fungi1.number + fungi2.number + fungi3.number
        self.fungi1_density = fungi1.number / total
        self.fungi2_density = fungi2.number / total
        self.fungi3_density = fungi3.number / total

    def set_wood_number(self, fungi1, fungi2, fungi3, time_interval):
        self.wood_number = self.wood_number - fungi1.dr * time_interval - fungi2.dr * time_interval - fungi3.dr * time_interval
