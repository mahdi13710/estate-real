from abc import ABC


class Sell(ABC):

    def __init__(
                self, price_per_meter, discountable,
                convertable, *args, **kwargs,
                ):
        
        self.price_per_meter = price_per_meter
        self.discountable = discountable
        self.convertable = convertable
        super().__init__(*args, **kwargs)
        
    def show_price(self):
        print(
        f"price_per_meter: {self.price_per_meter}\tdiscountable: {self.discountable}      \tconvertable: {self.convertable}")
    
    
    
    
class Rent(ABC):

    def __init__(
        self, initial_price, montly_price, discountable,
        convertable, *args, **kwargs,
    ):
                
     
        self.initial_price = initial_price
        self.montly_price = montly_price
        self.discountable = discountable
        self.convertable = convertable
        super().__init__(*args, **kwargs)
        
    def show_price(self):
        print(
        f"{self.initial_price}\t{self.montly_price}\t{self.discountable}\t{self.convertable}"
   )
              
        
                
