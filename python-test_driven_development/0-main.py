#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(4, 4))
print(add_integer(3.2, 6))
print(add_integer("l", 3))
print(add_integer(100.3, -2))
f = float('-inf')
print(add_integer(f, 6))
print(add_integer(3, "b"))
print(add_integer(2))



try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
