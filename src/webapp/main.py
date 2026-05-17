from flask import Flask, request, url_for, redirect
import src.webapp.menu as menu
import json
import customer
 
app = Flask("SS Restaurant")

menus = menu.Menu()
customers = customer.Customers()
orders = customer.Orders()


@app.route("/menu", methods=['GET', 'POST', 'DELETE'])
def menu_route():
    if request.method == 'GET':
        return menus.json()
    if request.method == 'POST':
        try:
            body = json.loads(request.data)
            if menus.is_exist(body['name']):
                menus.update(menu.Dish(body['name'], int(body['amount'])))
            else:
                menus.add_dish(menu.Dish(body['name'], int(body['amount'])))
            return menus.json()
        except Exception as e:
            return {'error': 'Invalid Data'}
            
    if request.method == 'DELETE':
        body = json.loads(request.data)
        menus.delete_dish(body['name'])
        return menus.json()
    
@app.route("/customers", methods=["GET"])
def customer_route():
    return customers.list()

@app.route("/create/customer", methods=["POST"])
def create_customer():
    body = json.loads(request.data)
    cust = customer.Customer(body['name'], body['phone_no'])
    customers.add(cust)
    return redirect(url_for('get_customer', id=cust.id))

@app.route("/delete/customer", methods=['POST'])
def delete_customer():
    body = json.loads(request.data)
    if customers.delete(body['id']):
        return "Successfully Deleted" , 201
    else:
        return "User not Found", 404
    
@app.route("/get/customer/<id>", methods=['GET'])
def get_customer(id):
    response = customers.get(id)
    if response:
        return response.json(), 200
    else:
        return "User not Found", 404
    
@app.route("/customer/<id>/orders", methods=['GET'])
def list_orders(id):
    cust = customers.get(id)
    return cust.orders

@app.route("/customer/<id>/create/order",  methods=['POST'])
def create_order(id):
    try:
        body = json.loads(request.data)
        cust = customers.get(id)
        order = customer.Order()
        dishes, invalid_dishes = order.add_dishes(body, menus)
        orders.add(order)
        cust.add_order(order.id)
        if invalid_dishes:
            return {"response": order.json(), "invalid_dishes": invalid_dishes}
        return order.json()
    except Exception as e:
        print(e)
        return {'error': 'Invalid Data'}
    
@app.route("/customer/<cust_id>/order/<order_id>", methods=['GET'])
def get_order(cust_id, order_id):
    cust = customers.get(cust_id)
    if order_id in cust.orders:
        return orders.get_order(order_id).json()
    return "Order not Found", 404

@app.route("/customer/<cust_id>/order/<order_id>/update", methods=['POST'])
def update_order(cust_id, order_id):
    body = json.loads(request.data)
    cust = customers.get(cust_id)
    if order_id in cust.orders:
        order, (updated_dishes, invalid_dishes) = orders.update_order_dish(order_id, body , menus)
        return {"dishes": order.json() , "invalid_dishes": invalid_dishes}
    return "Order not Found", 404

@app.route("/customer/<cust_id>/order/<order_id>/cancel", methods=['POST'])
def delete_order(cust_id, order_id):
    cust = customers.get(cust_id)
    if order_id in cust.orders:
        if orders.update_status(order_id, "cancelled"):
            return redirect(url_for('get_order', cust_id=cust_id, order_id=order_id)), 200
        else:
            return redirect(url_for('get_order', cust_id=cust_id, order_id=order_id)), 400

app.run(port='8080', debug=True)
