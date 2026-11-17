def calculate_discount(price, discount_percent):
    assert price >= 0, "Error: Price cannot be negative!"
    assert 0 <= discount_percent <= 100, "Error: Discount must be between 0 and 100!"
    
    final_price = price - (price * (discount_percent / 100))
    return final_price

print("--- Valid Input ---")
print("Final Price:", calculate_discount(200, 20))

print("\n--- Invalid Input ---")
try:
    calculate_discount(-50, 10)
except AssertionError as e:
    print("Assertion Failed:", e)