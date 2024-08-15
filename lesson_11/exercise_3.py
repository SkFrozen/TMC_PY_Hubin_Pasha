class Car:
    
    def __init__(self, color, body_type, year):
        self.color = color
        self.body_type = body_type
        self.year = year

    def started_car(self):
        return "The car is started"
    
    def turned_off_car(self):
        return "The car is turned off"
    
    def set_color(self, color):
        self.color = color
    
    def set_body_type(self, body_type):
        self.body_type = body_type

    def set_year(self, year):
        self.year = year


audi = Car('red', 'wagon', '1996')

print(audi.year, audi.body_type, audi.color, sep=' : ')
print(audi.started_car())
print(audi.turned_off_car())
audi.set_color("orange")
audi.set_body_type("coupe")
audi.set_year("2024")
print(audi.year, audi.body_type, audi.color, sep=' : ')