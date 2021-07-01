class Vehicle:
    def __init__(self, make, model, year, weight, needsMaintenance = False, tripsSinceMaintenance = 0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.NeedsMaintenance  = needsMaintenance
        self.tripsSinceMaintenance = tripsSinceMaintenance
        self.isDriving = False

    def getMake(self):
        return self.make

    def getmdel(self):
        return self.model

    def getyear(self):
        return self.year

    def getweight(self):
        return self.weight
    def setMake(self, make):
         self.make = make

    def setmdel(self, model):
         self.model = model

    def setyear(self, year):
        self.year = year

    def setweight(self, weight):
        self.weight = weight

    def Repair(self):
     self.NeedsMaintenance  = False
     self.tripsSinceMaintenance = 0

    def print_properties(self):
        print(self.make)
        print(self.model)
        print(self.year)
        print(self.weight)
        print(self.isDriving)
        print(self.tripsSinceMaintenance)
        print(self.NeedsMaintenance)
        print("================")

class Cars(Vehicle):
    def __init__(self, make, model, year, weight, isDriving  = False):
        Vehicle.__init__(self, make, model, year, weight)
        self.isDriving  = isDriving

    def drive(self):
        self.isDriving  = True


    def stop(self):
        self.isDriving  = False
        self.tripsSinceMaintenance += 30
        if self.tripsSinceMaintenance >= 100:
            self.NeedsMaintenance = True



Maruti = Cars("Maruti", "alto", 1998, 200)
BMW = Cars("BMW", "BMW X1", 2018, 180)
Audi = Cars("Audi", "Audi A8 L", 1950, 300)

Maruti.drive()
Maruti.stop()
Maruti.print_properties()
Maruti.drive()
Maruti.stop()
Maruti.print_properties()
Maruti.drive()
Maruti.stop()
Maruti.print_properties()
Maruti.drive()
Maruti.print_properties()
Maruti.stop()
Maruti.print_properties()
Maruti.Repair()

BMW.drive()
BMW.stop()
BMW.print_properties()
BMW.drive()
BMW.stop()
BMW.print_properties()
BMW.drive()
BMW.stop()
BMW.print_properties()
BMW.drive()
BMW.print_properties()
BMW.stop()
BMW.print_properties()
BMW.Repair()

Audi.drive()
Audi.stop()
Audi.print_properties()
Audi.drive()
Audi.stop()
Audi.print_properties()
Audi.drive()
Audi.stop()
Audi.print_properties()
Audi.drive()
Audi.print_properties()
Audi.stop()
Audi.print_properties()
Audi.Repair()



