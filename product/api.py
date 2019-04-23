
# Product Service

# Import framework
from flask import Flask
from flask_restful import Resource, Api
import pymysql
# Instantiate the app
app = Flask(__name__)
api = Api(app)
class Database:
    def __init__(self):
        host = "pydb"
        port= 3306
        user = "admin"
        password = "admin"
        db = "productdb"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db,port=port,cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()
    def list_employees(self):
        self.cur.execute("SELECT * from productdb;")
        result = self.cur.fetchall()
        return result

class Product(Resource):
    def get(self):
        #return {
        #    'products': ['Ice cream', 'Chocolate', 'Fruit', 'Eggs']
        #}
        db = Database()
        emps = db.list_employees()
        return emps
        
class ProductSlow(Resource):
    def get(self):
        #return {
        #    'products': ['Ice cream', 'Chocolate', 'Fruit', 'Eggs']
        #}
        entero = 0
        while entero < 7777777:
            entero+=1
        db = Database()
        emps = db.list_employees()
        return emps
# Create routes
api.add_resource(Product, '/')
api.add_resource(ProductSlow, '/slow/')
# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)