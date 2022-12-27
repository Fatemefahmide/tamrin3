import math

def moadele_daraje_do():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    delta = b*b-4*a*c

    if delta == 0:
        x=(-b+math.sqrt(delta))/(2*a)
        print("moadele yek gavab darad\n x= ")

    elif delta < 0:
        print("moadele gavab nadarad")

    elif delta > 0:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b+math.sqrt(delta))/(2*a)
        print("moadele do gavab darad \n x1=",x1 ,"\n x2= ",x2)


moadele_daraje_do()