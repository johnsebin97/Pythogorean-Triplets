
import math
import time

def Theorem():
    WhichSide = input("Which side are you trying to calculate, the Hypotenuse(H) or an other side(O) ?")
    if WhichSide == "H":
        time.sleep(0.5)
        print("Ok...")
        time.sleep(0.2)
        a = input("What is the length of one of the sides in the triangle ?")
        b = input("What is the length of the other side in the triangle ?")
        c = int(a)**2
        d = int(b)**2
        e = int(c) + int(d)
        f = int(e)**(0.5)
        print("The length of the Hypotenuse is",f,"cm")
    elif WhichSide == "O":
        print("Ok...")
        a = input("What is the length of the Hypotenuse in the triangle ?")
        b = input("What is the length of the other side in the triangle ?")
        c = int(a) * int(a)
        d = int(b) * int(b)
        e = int(c) - int(d)
        f = int(e)**(0.5)
        print("The length of the other side is",int(f),"cm")
    else:
        exit(0)
Theorem()
input("")
