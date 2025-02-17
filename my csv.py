import csv

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @classmethod#converting the below function into a class function
    def instantiate_from_csv(cls):#when we call our class method class itself is passed as the first argument instead of the self which we use for instance 
        """
        Instantiate items from a CSV file.

        Returns:
            list: A list of Item objects.
        """
        items = []
        try:
            with open('items.csv', 'r') as file:#as we are  reading the file we use r and we will write the th name of file to read from 
                reader = csv.DictReader(file)#this method should go and read our content as list of dictionaries 
                for row in reader:
                    item = cls(row['name'], row['price'], row['quantity'])
                    items.append(item)
                    print(item)
        except FileNotFoundError:
            print("File item.csv not found.")
        except csv.Error as e:
            print(f"Error reading CSV file: {e}")
        return items

    def __str__(self):
        """
        Return a string representation of the item.
        """
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

# Usage
Item.instantiate_from_csv()
        
        













#as this method is designed for instiate object.so this means it cannot be called from an instance
#so this can be solved by converting this method into classmethod
#cls is used as when use classmethod we call class to pass as first parameter so instead of self we