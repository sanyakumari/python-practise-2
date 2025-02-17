import csv


class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod##converting the below function into a class function
    def instantiate_from_csv(cls):##when we call our class method class itself is passed as the first argument instead of the self which we use for instance 
        with open('items.csv', 'r') as f:##as we are  reading the file we use r and we will write the th name of file to read from f is used for file you can write file directly also
            reader = csv.DictReader(f)##this method should go and read our content as list of dictionaries 
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
#staticmethod to check whether the recieved  number is integer or not 
    @staticmethod#in static method we never send the object as the first argument
    def is_integer(num):#as it should check if the recieved is a number or not 
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):#this function is going to check if the recieved parameter is an instance of float or an integer 
            # Count out the floats that are point zero
            return num.is_integer()#it check by as When we call is_integer() on a float, Python checks if the binary fraction has any non-zero bits in the fractional part.In the case of floats that are point zero (e.g., 5.0, 10.0), the fractional part is zero, so is_integer() returns True.
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    


print(Item.is_integer(7.0))