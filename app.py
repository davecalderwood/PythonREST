from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

expenses = []

class Expense(Resource):
    def get(self, id):
        for expense in expenses:
            if expense['id'] == id:
                return expense
        return {'expense': None}, 404

    def post(self, id):
        data = request.get_json()
        expense = {'id': id, 'price': data['price']}
        expenses.append(expense)
        return expense, 201

class ExpenseList(Resource):
    def get(self):
        return {'expenses': expenses}

api.add_resource(Expense, '/expense/<string:id>')
api.add_resource(ExpenseList, '/expenses')

app.run(port=5000, debug=True)