import csv


class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []#This is a class variable initialized as an empty list. It will store all instances of the Item class
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.__name = name #Purpose: These lines assign the passed arguments (name, price, quantity) to the instance attributes.
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)#This line appends the current instance (self) to the all list, which keeps track of all Item instances.
#if we are using all[] in our code we need to write the above line
    
        @property#are the decorators-they are the functions that you can pre execute before another function 
    # Property Decorator = Read-Only Attribute
        def name(self):#By using @property with a read-only attribute, you can ensure that the attribute can only be accessed, not modified.
                    #Getter Method: The @property decorator defines a getter method that returns the value of the attribute.
            return self.__name
    
        @name.setter
        def name(self,value):
            self.__name = value
    
    
    
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    '''When reading data from a CSV file, some keys might be missing or have unexpected values. Using get() ensures your code doesn't crash if a key is missing.'''

    '''This static method checks if a number is an integer (including floats like 5.0).'''
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()#checks if there is an integer in the fraction part of number eg.2.6 6 is the fractional part
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):#This is a special method in Python classes that returns a string representation of the object.method is used to provide a human-readable representation of the object, which can be useful for debugging or logging.

        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
#Example Output: For an Item object with name='Laptop', price=1000, and quantity=5, the __repr__ method would return the string 'Item('Laptop', 1000, 5)'.

# '''to set up a read only attribute so that no user can change the value of an attribute if you want to keep it private '''
#By using @property with a read-only attribute, you can ensure that the attribute can only be accessed, not modified.
# Getter Method: The @property decorator defines a getter method that returns the value of the attribute.
 
   
   
   



'''phone is child class and item is parent class'''
class Phone(Item):#as we are inherting the class phone from item
    #Inheritance allows the Phone class to reuse the attributes and methods of the Item class.

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):#as broken phone is a unique category which can be only be applied to pones
        # Call to super function to have access to all attributes / methods
        super().__init__(  #super allows to have full access to all the attributes of the parent class and by using the super function we don't really need to hardcore in the attribute assignment like we have done with the name
            name, price, quantity#we don't need to do self.nane = name etc.
        )

        # Run validations to the received arguments
        
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"

        # Assign to self object
        #as broken phone is unique for phone we need to hardcore the assignment class for the operators
        self.broken_phones = broken_phones

phone1 = Phone("jscPhonev10", 500, 5, 1)

print(Item.all)
'''The output is a list because the script is printing the Item.all list, which contains all instances of the Item class and its subclasses. In this case, the list contains only one instance, which is the Phone instance created in the script.'''











'''Purpose of all[]
Tracking Instances: The all[] list is used to store all instances of the Item class. This allows you to easily access and manage all items created during the program's execution.
Example Use Case: If you need to perform operations on all items (e.g., calculating total inventory value, applying discounts globally, or printing all items), all[] provides a convenient way to do so.
'''

'''When to Avoid all[]
Small Programs: If your program creates only a few instances and doesn't need to track them, all[] is unnecessary.
Memory Constraints: If memory usage is a concern, avoid using all[] to prevent storing unnecessary data.
No Bulk Operations: If you don't need to perform operations on all instances at once, all[] is not required.'''