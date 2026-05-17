import uuid

class Menu:
    def __init__(self):
        self.menu = []
    
    def add_dish(self, Dish):
        self.menu.append(Dish)
    
    def is_exist(self, name):
        for dish in self.menu:
            if dish.name == name:
                return True
        return False
    
    def update(self, Dish):
        for i, dish in enumerate(self.menu):
            if dish.name == Dish.name:
                self.menu[i].amount = Dish.amount

    def delete_dish(self, name):
        for i, dish in enumerate(self.menu):
            if dish.name == name:
                self.menu.pop(i)

    def get_dish(self, id):
        for dish in self.menu:
            if dish.id == id:
                return (dish, None)
        return (None, "Dish not Found")

    def __str__(self):
        menu = 'SS Restaurant 💕\n'
        for dish in self.menu:
            menu += "-----------------------------------------\n"
            menu += dish.__str__()
        menu += "-----------------------------------------\n"
        return menu
    
    def json(self):
        menu = []
        for dish in self.menu:
            menu.append({"dish_id": dish.id, "name": dish.name, "amount": dish.amount})
        return menu
    
            
    
class Dish:
    def __init__(self, name, amount):
        self.id = str(uuid.uuid4())
        self.name = name
        self.amount = amount
    
    def __str__(self):
        return f'{self.name}:\t{self.amount}\n'
    
    def json(self):
        return {"id":self.id, "name":self.name, "amount":self.amount}
    
    
    
# fish_fry = Dish('Fish Fry', 50)
# chicken_rice = Dish('Chicken Rice', 100)

# menu = Menu()
# menu.add_dish(fish_fry)
# menu.add_dish(chicken_rice)

# print(menu)
# print(menu.json())