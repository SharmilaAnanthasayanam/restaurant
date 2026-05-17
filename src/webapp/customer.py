import uuid


class Customers:
    def __init__(self):
        self.customers = []

    def add(self, Customer):
        self.customers.append(Customer)

    def update(self, id, name=None, phone_no=None ):
        for i, customer in enumerate(self.customers):
            if customer.id == id:
                if name: 
                    self.customers[i].name = name
                if phone_no:
                    self.customers[i].phone_no = phone_no
                return True
        return False
        
    def delete(self, id):
        for i, customer in enumerate(self.customers):
            if customer.id == id: 
                self.customers.pop(i)
                return True
        return False

    def get(self, id):
        for customer in self.customers:
            if customer.id == id:
                return customer
        return None

    def list(self):
        cust_list = []
        for cust in self.customers:
            cust_list.append({'id': cust.id, 'name': cust.name, 'phone_no': cust.phone_no})
        return cust_list
    
class Customer:
    def __init__(self, name, phone_no):
        self.id = str(uuid.uuid4())
        self.name = name
        self.phone_no = phone_no
        self.orders = []

    def add_order(self, order_id):
        self.orders.append(order_id)

    def list_orders(self):
        return self.orders

    def json(self):
        return {'id': self.id, 'name': self.name, 'phone_no': self.phone_no, 'orders': self.orders}
    
class Orders:
    def __init__(self):
        self.orders = []

    def add(self, Order):
        self.orders.append(Order)
        
    def update_status(self, order_id, status):
        for order in self.orders:
            if order.id == order_id:
                order.update_status(status)
                return True
        return False

    def get_order(self, order_id):
        for order in self.orders:
            if order.id == order_id:
                return order
        return None
    
    def update_order_dish(self, order_id, dishes, menus):
        order = self.get_order(order_id)
        if order:
            return order, order.add_dishes(dishes, menus)
        return (False, "Order not Found")


class Order:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.dishes = []
        self.status = 'pending'
    
    def total_money(self, menu):
        total_amount = 0
        for dish in self.dishes:
            menu_dish, msg = menu.get_dish(dish.id)
            if menu_dish:
                total_amount += menu_dish.amount * dish.quantity
            else:
                print(f"{msg}: {dish.id}")
        return total_amount
    
    def add_dishes(self, dishes, menus):
        valid_dishes = []
        invalid_dishes = {}
        for dish_id in dishes.keys():
            dish, msg = menus.get_dish(dish_id)
            if dish:
                valid_dishes.append({"dish": dish, "quantity": dishes[dish_id]})
            else:
                invalid_dishes[dish_id] = dishes[dish_id]
        self.dishes =  valid_dishes
        return (self.dishes, invalid_dishes)
    
    def delete_dishes(self, dish_id):
        if self.dishes.get(dish_id, None):
            self.dishes.pop(dish_id)
            return True
        return False
    
    def update_status(self, status):
        self.status = status

    def json(self):
        dishes = self.json_dishes()
        return {'id': self.id, 'dishes': dishes, 'status': self.status}
    
    def json_dishes(self):
        dishes = []
        for dishes_dict in self.dishes:
            dishes.append({"dish": dishes_dict.get("dish").json(), "quantity": dishes_dict.get("quantity")})
        return dishes
    



    
    

        

        





