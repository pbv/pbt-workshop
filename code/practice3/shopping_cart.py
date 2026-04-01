# ------------------------------------------------------------------------
# A shopping cart example
#
# Pedro Vasconcelos, 2026
# ---------------------------------------------------------------------

class ShoppingCart:
    def __init__(self, prices):
        self.prices = prices  
        self.quantity = dict()

    # override contains method
    def __contains__(self, item):
        return item in self.quantity
        
    def add(self, item:str):
        """Add an item to the current current."""
        if item not in self.prices:
            raise ValueError("invalid item")

        if item in self.quantity:
            self.quantity[item] += 1
        else:
            self.quantity[item] = 1

    def remove(self, item:str):
        """Remove an item in the current cart."""
        if item not in self.quantity:
            raise ValueError("invalid item")
        if self.quantity[item] > 0:
            self.quantity[item] -= 1
        else:
            del self.quantity[item]


    def get_subtotal(self):
        """Compute the subtotal for the cart."""
        total = 0
        for item in self.quantity.keys():
            total += self.quantity[item]*self.prices[item]
        return total

    def save(self) -> str:
        """Save the current cart into a string."""
        rows = [(item,quant) for item,quant in self.quantity.items()]
        return str(rows)
    
    def load(self, txt: str):
        """Load the shopping cart from a string."""
        self.quantity = dict()
        for item,quant in eval(txt):
            self.quantity[item] = quant
        
        
