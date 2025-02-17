#creating object and creating instance are the same thing 

class Item:#methods are the function are inside the classes 
    #if we want to give 20% discount for every item
    pay_rate = 0.8 #this is class attribute other were instance attribute 
    all = []
    def __init__(self, name: str, price: float, quantity):#it will run the number of times an instance/object has been created 
       #print(f"An instance is crearted: {name}")
      #we can declare the type we want in your attribute so that there is not error like name : str etc
      '''if we want to apply something that can't never be true for eg. price can never be negative we will use assert function'''
      #Run validations to the recieved arguments
      assert price >= 0, f"Price {price} is not greater than zero" #we can also write a string saying error caused if it not according to assert condtion given
      assert quantity >= 0



      self.name = name  #by creating this inside the function it eases our work as instead of writing attribute in every object we can directly run this attribute using __init__ method 
      self.price = price
      self.quantity = quantity
    
    #Action to execute
      Item.all.append(self)
     
    # #def calculate_total_price(self, x, y):
    # #  return x * y
    #when we have createad __init method instead of the above code we can write 
    def calculate_total_price(self):     #isolated defination with this keyword are called function but when we create those function inside the class it is called as methods   
     return self.price * self.quantity
    ##we need a paramter inside method otherwise it will show an error so we use self inside a method 

    # def apply_discount(self):
    #   self.price = self.price * Item.pay_rate#If you use pay_rate without Item., as class attribute can be accesed by object also Python will look for it in the local scope of the method. Since pay_rate is not defined locally, it will raise a NameError
#By using Item.pay_rate, you explicitly tell Python to use the class attribute pay_rate.

# '''but when we are using Item.pay_rate we can't change the value if we want for one object eg. if we want to give 30% discount for laptop then our apply_discout will be '''
    def apply_discount(self):
        self.price = self.price * self.pay_rate #if we want to change the value of pay
 
    def __repr__(self):
       return f"Item('{self.name}', {self.price}, {self.quantity})"#it should be same as we used below for item1,,3,4,5 and make it same general format








# item1 = Item("Phone",100, 5 )#instance is created and it will called the __init__ method automatically
# item1.apply_discount()#we are applying a method to an object we need to aaply it only inside the object as we can't apply the method outside the object 
# print(item1.price)

'''we can remove the item.name from all  of our instance with help of __init__ method we can pass parameter inside __init__ method '''
##item1.name = "Phone"#we can create an attribute using dot and assign a value to it
##item1.price = 100
##item1.quantity = 5
# print(item1.calculate_total_price(item1.price , item1.quantity))
   


#our instance created should have the same parameter as init method 
# item2 = Item("Laptop",1000, 3)#instance is created and it will called the __init__ method automatically
##item2.name = "Laptop"
##item2.price = 1000
##item2.quantity = 3
# print(item2.calculate_total_price(item2.price , item2.quantity))
'''now if we want to create a seprate discount for each item we can directly write it inside the object but outside it pay_rate would be same for all which is defined in class attrbute'''
# item2.pay_rate = 0.7#write 
# item2.apply_discount()
# print(item2.price)



#print(type(item1)) #this would output <class '__main__.Item'>     

'''to directly use attribute inside the  __init__ method which saves a lot of time as instead of writing one by one in each object we can write it inside __init__ method and write the value inside our object like item1 = Item(“laptop”) then inside our init method __init__(self, name) therefore the laptop is the value for name and we can access it using item1.name directly outside object also '''
# print(item1.name)
# print(item2.name)
# print(item1.quantity)
# print(item2.quantity)
# print(item1.price)
# print(item2.price)
# print(item1.calculate_total_price())#we are using open bracket in this one To execute a method, you need to call it using parentheses (). This tells Python to run the method and return its result.
# print(item2.calculate_total_price())


#To print a class attribute we can do through class or instance/object also

# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)
# print(Item.__dict__) #it will give all the attributes for class level
# print(item1.__dict__) #it will give all the attributes for instance level

item = Item ("Phone", 100, 1)
item2 = Item ("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item ("Mouse",50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)#proper list can only be printed by this function with the help __repr__ otherwise it would be not be possible

## Print the names of all items created 
# for instance in Item.all:
#    print(instance.name)

