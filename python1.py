#list based programms 

class Pen:
    
    def __init__(self,Brand,Price,Color):
        self.brand=Brand
        self.price=Price
        self.color=Color
        
    def details(self):
        print("pen[Brand:{},Price RS:{},Color:{}]".format(self.brand,self.price,self.color))
        
    print("_"*50)
    
            