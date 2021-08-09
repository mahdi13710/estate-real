from sample import create_samples
from advertisment import ApartmentSell, ApartmentRent, HouseSell, HouseRent
from manager import Manager


class Handler:

    ADVERTISMENT_TYPE ={
        1: ApartmentSell, #2: ApartmentRent,
        3: HouseSell, #4: HouseRent,
        #5: StoreSell, 6: StoreRent,
    }
    
    SWITCHES = {
        'r': 'get_report',
        's': 'show_all',
    }
    
    
    def get_report(self):
        for adv in self.ADVERTISMENT_TYPE.values():
            print(adv, adv.manager.count())
    
    
    def show_all(self):
        for adv in self.ADVERTISMENT_TYPE.values():
            #print(adv, adv.manager.count())
            for obj in adv.object_list:
                print(obj.show_detail())
    
    def run(self):
        print("Hello, world!")
        for key in self.SWITCHES:
            print(f"press {key} for {self.SWITCHES[key]}")   
        user_input = input("Enter your choices: ")
        switch = self.SWITCHES.get(user_input, None)
        if switch is None:
            print("Invalid input")
            self.run()
        choice = getattr(self, switch, None)
        choice()
        self.run()
            
        
        
if __name__ == '__main__':
    create_samples()
    handler = Handler()
    handler.run()
    
           
