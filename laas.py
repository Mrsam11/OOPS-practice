class RailwayForm:
    formtype = "Railway form"
    def Printdata(self):
        print(f"Name is {self.name}")
        print(f"train is {self.train}")
        
applicationform = RailwayForm()
applicationform.name = 'Sameer'
applicationform.train = 'Express'
applicationform.Printdata()