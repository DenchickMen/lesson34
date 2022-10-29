import random
class Human:
    def __init__(self, name = "Денис", job = None,home = None, car=None):
        self.name=name
        self.job=job
        self.car=car
        self.money=1000000000
        self.gladness = 50
        self.satiety = 50
    def get_home(self):
        pass
    def get_car(self):
        pass
    def get_job(self):
        pass
    def food(self):
        pass
    def work(self):
        pass
    def shopping(self):
        pass
    def chill(self):
        pass
    def clean(self):
        pass
    def day_indexes(self, day):
        pass
    def is_alive(self):
        pass
    def live(self, day):
        pass

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.strenght = brand_list[self.brand]['strenght']
        self.fuel = brand_list[self.brand]['fuel']
        self.consumption = brand[self.brand]['consumption']