import os
import math

function = input("Function to be integrated? (x should be the only variable)\n").replace(" ", "").replace("^", "**").replace("sqrt", "math.sqrt")
a = float(input("Lower bound of integration?\n").replace(" ", "").replace("sqrt", "math.sqrt"))
b = float(input("Upper bound of integration?\n").replace(" ", "").replace("sqrt", "math.sqrt"))
p = int(input("Number of partitions?\n").replace(" ", ""))
m = str(input("What method should be used? [L]RAM, [M]RAM, [R]RAM, [T]rapezoidal\n").replace(" ", "").replace("L", "l").replace("M", "m").replace("R", "r").replace("LRAM", "l").replace("MRAM", "m").replace("RRAM", "r").replace("lram", "l").replace("mram", "m").replace("rram", "r").replace("[L]RAM", "l").replace("[M]RAM", "m").replace("[R]RAM", "r").replace("[l]ram", "l").replace("[m]ram", "m").replace("[r]ram", "r").replace("[L]", "l").replace("[M]", "m").replace("[R]", "r").replace("[l]", "l").replace("[m]", "m").replace("[r]", "r").replace("T", "t").replace("Trapezoidal", "t").replace("trapezoidal", "t").replace("[T]", "t").replace("[t]", "t"))
delta_x = (b-a)/p

def f(x):
    return eval(function)

def main():
    temp = 0
    if m == "l":
        for n in range(p):
            temp = temp + ((delta_x*f(a+n*delta_x)))
            print("Iterations left: " + str(p-n))
    if m == "m":
        for n in range(p):
            temp = temp + ((delta_x*f(a+n*delta_x+0.5*delta_x)))
            print("Iterations left: " + str(p-n))
    if m == "r":
        for n in range(p):
            temp = temp + ((delta_x*f(a+n*delta_x+delta_x)))
            print("Iterations left: " + str(p-n))
    if m == "t":
        for n in range(p):
            temp = temp + ((((delta_x*f(a+n*delta_x))))+(((delta_x*f(a+n*delta_x+delta_x)))))/(2)
            print("Iterations left: " + str(p-n))
    return temp

ans = main()

os.system('cls' if os.name == 'nt' else 'clear')
print("\nAnswer: " + str(ans) + "\n")
