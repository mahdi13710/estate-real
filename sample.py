from user import User
from random import choice
from estate import Apartment, House, Store
from region import Region
from advertisment import ApartmentSell, HouseSell


FIRST_NAME = ['Mahdi', 'Naser', 'Ali']
LAST_NAME = ['Salehi', 'Karami', 'Alavi']
PHONE_NUMBER = [
       '09123459081', '09123456780', '09123214590',
        '0912453213', '09129080701']
       
       
       
def create_samples():
    for mobil in PHONE_NUMBER:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobil)
    #print(len(User.object_list))
    
    
    #for user in User.object_list:
    
        #print(f"{user.id}\t {user.fullname}")
        
     
    rg1 = Region(name='Rg1')    
    apartment = Apartment(
        user=User.object_list[0], area=80, rooms_count=2,
        built_year=1396, region=rg1, address='Some text',
        has_elevator=True, has_parking=True, floor=2)
                          
    #apartment.show_description()
    
    
    house = House(
        has_yard=True, floor_count=1, user=User.object_list[2],
        address="Some text", area=400, rooms_count=4,
        built_year=1379, region=rg1)
        
    
    #house.show_description()
    
    
    
    store = Store(
        address="Some text", area=30, built_year=1398,
        user=User.object_list[-1], rooms_count=0, region=rg1)
                  
    #store.show_description()
    
    
    
    apartment_sell = ApartmentSell(
        user=User.object_list[0], area=80,
        rooms_count=2,built_year=1396, region=rg1,
        address='Some text',has_elevator=True,
        has_parking=True, floor=2,
        price_per_meter=10, discountable=True,
        convertable=False)
        
                                
    #apartment_sell.show_detail()
    
    
    #print("##"*40,'\n')
    
    house_sell = HouseSell(
        has_yard=True, floor_count=1, user=User.object_list[2],
        address="Some text", area=400, rooms_count=4,
        built_year=1379, region=rg1, price_per_meter=20,
        discountable=False, convertable=True)
    
    #house_sell.show_detail()
    
    #print("##"*40,'\n')
    
    
    #print(ApartmentSell.manager.search(region=rg1))
    #print(HouseSell.manager.get(region=rg1))
    
    #print(ApartmentSell.manager.search(price_per_meter__max=20))
    #print(ApartmentSell.manager.search(area__max=81))
    
    
    
    #print(ApartmentSell.object_list)
    #print(HouseSell.object_list)
    
    
    print('#' * 20, "\tsample create\t", '#' * 20)

