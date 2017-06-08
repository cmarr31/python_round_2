from pprint import pprint

class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if (price > 10000):
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.display_all()

	def display_all(self):
		price_str = str(self.price)
		tax_str = str(self.tax)
		#instance_info = self.__dict__
		pprint (vars(self))

mustang = Car(17000, "160mph", "full", "14mpg")
camaro = Car(23000, "180mph", "three quarter tank", "12mpg")
f150 = Car(17000, "140mph", "empty", "10mpg")
ferrari = Car(17000, "220mph", "empty", "15mpg")
lamborghini = Car(17000, "250mph", "half tank", "16mpg")
challenger = Car(17000, "180mph", "quarter tank", "12mpg")