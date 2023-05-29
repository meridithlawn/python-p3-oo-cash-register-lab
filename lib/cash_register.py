#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, product_name, price, quantity=1):
    self.items.append({"item": product_name, "price": price, "quantity": quantity})
    self.total += price * quantity

  def apply_discount(self):
    if self.discount:
      self.total *= ((100 - self.discount)/100)
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.items[-1].get("price") * self.items[-1].get("quantity")
    self.items.pop()