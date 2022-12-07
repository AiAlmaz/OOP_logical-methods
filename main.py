class Teacher:
    def __init__(self, rate, hour):
        self.rate = rate
        self.hour = hour

    def get_total(self):
        return self.rate * self.hour

    def __str__(self):
        return f"the Teacher's salary per week is"

class Taxi_driver:

    def __init__(self, order, percentage, price):
        self.order = order
        self.percentage = percentage
        self.price = price

    def get_total(self):
        return self.price * self.percentage * self.order

    def __str__(self):
        return f"Taxi_Driver's salary per week is"

class Baker:

    def __init__(self, ingredients, price):
        self.ingredients = ingredients
        self.price = price

    def get_total(self):
        return self.price - self.ingredients

    def __str__(self):
        return f"The salary for Baker per order is"

teacher = Teacher(14, 5)
driver = Taxi_driver(25, 0.70, 120)
baker = Baker(2000, 1300)

professions = [teacher, driver, baker]

for profession in professions:
    print(profession, profession.get_total())

