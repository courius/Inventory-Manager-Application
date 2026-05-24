# inventory.py
# Name: Sandu Stati Suman
# Date: 20/03/2026
# inventory.py
# Description: This module contains the Inventory class which manages a collection of 
# Product objects and provides methods for searching, reporting, and maintenance.


from product import Product

class Inventory:
    """
    Manages a collection of Product objects using a dictionary for storage.

    Attributes:
        _products (dict).
    """

    def __init__(self):
        """Initialises an empty inventory with no products."""
        self._products = {}


    def add_product(self, name, category, price, quantity, min_stock):
        """
        Creates and adds a new product to the inventory.
        
        Returns:
            The newly generated product_id.
        """
        product_id = self._generate_id()
        self._products[product_id] = Product(product_id, name, category, price, quantity, min_stock)

        return product_id


    def remove_product(self, product_id):
        """Removes a product by ID. Returns the removed Product or None if not found."""
        if product_id not in self._products:
            return None
        removed_item = self._products[product_id]
        del self._products[product_id]

        return removed_item
    

    def get_product(self, product_id):
        """Retrieves a Product object by its ID."""
        if product_id not in self._products:
            return None
        
        return self._products[product_id]

    
    def get_all_products(self):
        """Returns a list of all Product objects currently in the inventory."""
        return list(self._products.values())
    

    def find_by_name(self, name):
        """Performs a case-insensitive exact name match. 
        
        Returns product_id or None.
        """
        for product_id, product in self._products.items():
            if name.lower() == product.name.lower():
                return product_id
        return None
    

    def search_by_name(self, search_term):
        """Returns a list of Product objects with names containing the search term."""
        matches = list()
        search_term_lower = search_term.lower()

        for product in self._products.values():
            if search_term_lower in product.name.lower():
                matches.append(product)

        return matches
    

    def search_by_category(self, category):
        """Returns a list of all Product objects within a specific category."""
        matches = list()
        category_lower = category.lower()

        for product in self._products.values():
            if category_lower == product.category.lower():
                matches.append(product)

        return matches
    

    def get_low_stock_products(self):
        """Returns a list of Product objects currently at or below minimum stock."""
        low_stock_products_list = list()

        for product in self._products.values():
            if product.is_low_stock():
                low_stock_products_list.append(product)
        
        return low_stock_products_list


    def generate_category_report(self):
        """
        Calculates count and total value statistics grouped by category.
        
        Returns:
            Statistics Dictionary for each category.
        """
        category_statistics = dict()

        for product in self._products.values():
            category = product.category

            if category not in category_statistics:
                category_statistics[category] = {"count": 0, "value": 0}

            category_statistics[category]['count'] += 1
            category_statistics[category]['value'] += product.get_value()

        return category_statistics


    def calculate_total_value(self):
        """Calculates the total monetary value of all items in the inventory."""
        inventory_value = 0

        for product in self._products.values():
            product_value = product.get_value()
            inventory_value += product_value
        
        return inventory_value


    def _generate_id(self):
        """Private method to generate a unique, incremental product ID (e.g., P001)."""
        if not self._products:
            product_id = "P001"
            return product_id
        
        # Find current highest ID
        max_num = 0
        for p_id in self._products.keys():
            num = int(p_id[1:])
            if num > max_num:
                max_num = num

        # Generate next ID
        next_num = max_num + 1
        product_id = f"P{next_num:03d}"

        return product_id
    

    def __len__(self):
        """Returns the total number of products in the inventory."""
        return len(self._products)