#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("l", "White")
say_my_name("Bob", 2)
try:
    say_my_name(12, mari)
except Exception as e:
    print(e)
