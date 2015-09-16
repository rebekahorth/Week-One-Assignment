__author__ = 'rebekah.orth'
#Chaos.py
#Rebekah Orth
#CIS 125 Fall 2015

# File: chaos.py
# A simple program illustrating chaotic behavior.
multiplier = 2.0
loopcounter = 10
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(loopcounter):
        x = multiplier * x * (1 - x)
        print(x)

main()
