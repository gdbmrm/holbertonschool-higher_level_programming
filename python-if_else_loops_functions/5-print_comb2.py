#!/usr/bin/python3

for num in range(0, 100):
    if num == 99:
        print(f"{num}")
    elif 0 <= num <= 9:
        print(f"0{num}, ", end="")
    else:
        print(f"{num}, ", end="")