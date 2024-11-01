"""
Codes: guitar_test.py and guitar.py
Coder: Hein Htet
Started at: 11:15
Ended:11:33
"""
from Codes.Practical.Week6.prac_06.guitar import Guitar
guitar1 = Guitar("Gibson L-5 CES", 1924, 401294.52)
guitar2 = Guitar("Guitar 2", 1974)
guitar3 = Guitar("Guitar 3", 2000)
print(guitar1)
print(f"Gibson L-5 CES, expect 100 years, and vintage. Result:{guitar1.get_age()},Vintage = {guitar1.is_vintage()}")
print(f"guitar2, expect 50 years, and vintage. Result:{guitar2.get_age()},Vintage = {guitar2.is_vintage()}") #Got me stumpted why 100 yrs was showing, turns out I forgot to switch guitar1 to guitar2 XD
print(f"guitar3, expect 24 years, and not vintage. Result: {guitar3.get_age()}, Vintage = {guitar3.is_vintage()}")