from _2020_2021.Classworks._8_24_10_2020._2 import Passenger, Person
import sqlite3

conn = sqlite3.connect('customers.sqlite3')
cursor = conn.cursor()


class Customer:
    @staticmethod
    def find_customer(id):
        sql = f"SELECT * FROM customers WHERE id LIKE ?"
        data = cursor.execute(sql, (id,)).fetchall()
        if len(data) == 0:
            return 'No customer with this ID !'
        else:
            data = data[0]
        customer = Passenger
        print(customer)
        customer.insert_data(id=data[0],
                             name=data[1],
                             birth_year= data[2],
                             start_location=data[3],
                             end_location=data[4],
                             distance=data[5])
        return customer

    @staticmethod
    def insert_cost(customer: Passenger):
        sql = '''INSERT INTO customers (customer_id, cost) VALUES (?,?)'''
        val = (customer.id, customer.price_for_km())
        cursor.execute(sql, val)
        conn.commit()


if __name__ == '__main__':
    test = Customer()

    customer1 = test.find_customer(2)
    print(cust)
    test.insert_cost(customer1)

cursor.close()
conn.close()
