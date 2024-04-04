import os
import math

function = input("Function to be integrated? (x should be the only variable)\n").replace(" ", "").replace("^", "**").replace("sqrt", "math.sqrt")
a = float(input("Lower bound of integration?\n").replace(" ", ""))
b = float(input("Upper bound of integration?\n").replace(" ", ""))
p = int(input("Number of partitions?\n").replace(" ", ""))
delta_x = (b-a)/p

def f(x):
    return eval(function)

def main():
    temp = 0
    for n in range(p):
        temp = temp + ((delta_x*f(a+n*delta_x)))
        print("Iterations left: " + str(p-n)) 
    return temp

ans = main()

os.system('cls' if os.name == 'nt' else 'clear')
print("\nAnswer: " + str(ans) + "\n")
