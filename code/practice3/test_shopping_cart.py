# -----------------------------------------------------------------------
# Hypothesis state machine for testing the shopping cart
#
# Pedro Vasconcelos, 2026
# ----------------------------------------------------------------------

from shopping_cart import ShoppingCart
from hypothesis import strategies as st, assume
from hypothesis.stateful import RuleBasedStateMachine, precondition, \
    initialize, rule

class ShoppingCartMachine(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.prices = dict() # empty price dictionary 
        self.cart = None     # no shopping cart defined

    #
    # Strategies for items, prices and dictionaries of prices
    #
    all_items = "ABCDEF"
    items = st.text(alphabet=all_items, min_size=1, max_size=1)
    prices = st.integers(min_value=1, max_value=9999)
    price_dicts = st.dictionaries(items, prices,
                                  min_size=len(all_items),
                                  max_size=len(all_items))
        
    # @initialize rules run before any other rule;
    # we use this setup item prices using a strategy
    @initialize(price_dict = price_dicts)
    def start(self, price_dict):
        self.prices = price_dict
        self.cart = ShoppingCart(price_dict)
        
    @rule(item = items)
    def add(self, item):
        total_before = self.cart.get_subtotal()
        self.cart.add(item)
        total_after = self.cart.get_subtotal()
        assert total_after == total_before + self.prices[item]
    
    @rule(item = items)
    def remove(self, item):
        assume(item in self.cart)
        total_before = self.cart.get_subtotal()
        self.cart.remove(item)
        total_after = self.cart.get_subtotal()
        assert total_after == total_before - self.prices[item]
      
TestShoppingCart = ShoppingCartMachine.TestCase
