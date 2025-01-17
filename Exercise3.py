class Location:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.stock_at_locations = {}

    def __repr__(self):
        return f"Location(name={self.name}, code={self.code})"

    def add_stock(self, product, quantity):
        if product not in self.stock_at_locations:
            self.stock_at_locations[product] = 0
        self.stock_at_locations[product] += quantity

    def display_stock(self):
        print(f"\n{self.name} stock:")
        for product, stock in self.stock_at_locations.items():
            print(f"{product.name}: {stock}")

    @staticmethod
    def display_all_stocks(locations):
        print("\nStock at various locations:")
        for location in locations:
            location.display_stock()

    @staticmethod
    def display_product_list_by_location(locations):
        print("\nProduct list by location:")
        for location in locations:
            products = [product.name for product in location.stock_at_locations.keys()]
            print(f"{location.name}: {', '.join(products)}")


class Product:
    products = []

    def __init__(self, name, code):
        self.name = name
        self.code = code
        Product.products.append(self)

    def __repr__(self):
        return f"Product(name={self.name}, code={self.code})"

    def display_movements(self):
        movements = Movement.movements_by_product(self)
        for movement in movements:
            print(f"From {movement.from_location.name} to {movement.to_location.name}, Quantity: {movement.quantity}")


class Movement:
    movements = []

    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
        self._process_movement()

    def _process_movement(self):
        if self.from_location.stock_at_locations.get(self.product, 0) >= self.quantity:
            self.from_location.stock_at_locations[self.product] -= self.quantity
            self.to_location.add_stock(self.product, self.quantity)
            Movement.movements.append(self)
        else:
            raise ValueError(f"Not enough stock of {self.product} at {self.from_location.name}")

    @staticmethod
    def movements_by_product(product):
        return [movement for movement in Movement.movements if movement.product == product]

    @staticmethod
    def display_movements_by_product():
        for product in Product.products:
            print(f"\nMovements for {product.name}:")
            product.display_movements()



loc1 = Location("Warehouse A", "A001")
loc2 = Location("Warehouse B", "B001")
loc3 = Location("Store X", "X001")
loc4 = Location("Store Y", "Y001")


prod1 = Product("Product A", "P001")
prod2 = Product("Product B", "P002")
prod3 = Product("Product C", "P003")
prod4 = Product("Product D", "P004")
prod5 = Product("Product E", "P005")


loc1.add_stock(prod1, 100)
loc1.add_stock(prod2, 50)
loc2.add_stock(prod3, 75)
loc3.add_stock(prod4, 200)
loc4.add_stock(prod5, 150)
loc3.add_stock(prod1, 20)
loc4.add_stock(prod2, 30)
loc2.add_stock(prod5,80)


try:
    Movement(loc1, loc2, prod1, 30)  
    Movement(loc2, loc3, prod1, 20) 
    Movement(loc4, loc1, prod2, 30)  
    Movement(loc2, loc3, prod3, 75)  
    Movement(loc3, loc4, prod4, 200) 
    Movement(loc2, loc3, prod5, 80)
except ValueError as e:
    print(f"Error: {e}")


Movement.display_movements_by_product()


Location.display_all_stocks([loc1, loc2, loc3, loc4])


Location.display_product_list_by_location([loc1, loc2, loc3, loc4])