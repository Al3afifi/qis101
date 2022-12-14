#!/usr/bin/env python3
# fahrenheit_to_celsius.py

for fahrenheit in range(-44, 217, 4):
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit:>6.2f} F = {celsius:>6.2f} C")
