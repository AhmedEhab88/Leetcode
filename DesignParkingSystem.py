class ParkingSystem:
    big, medium, small = None, None, None

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1: 
            #big
            if(self.big > 0):
                self.big -= 1
                return True 
            else: 
                return False
        elif carType == 2:
            #medium
            if(self.medium > 0):
                self.medium -= 1
                return True 
            else: 
                return False   
        elif carType == 3:
            #small
            if(self.small > 0):
                self.small -= 1
                return True 
            else: 
                return False