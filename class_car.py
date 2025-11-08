class car:
  def __init__(self,make,model,year):
    self.make = make
    self.model = model
    self.year = year
  def start(self):
    print(f"The {self.make} {self.model} {self.year} is starting")
  def stop(self):
    print(f"The {self.make} {self.model} {self.year} is stopping")
car1 = car("Toyota","Camry",2022)
car2 = car("Toyota","camry",2032)
car1.start()
car2.stop()
  
