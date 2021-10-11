import math

def cube():
    while True:
        try:
            cubeside = eval(input("Insert cube side length in meters:"))
            cubevolume = cubeside ** 3
            print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\nThe volume of the cube is {cubevolume}m^3\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            break
        except NameError:
            print("Please insert number values, for example 10, 25.5 , 100 etc.")

def octagon_area():
    octagon_side = eval(input(f'\nInsert octagon side length in centimeters '))
    octagon_area = 2*octagon_side*2(1+math.sqrt(2))

    octagon_output = f'\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\nThe area of your octagon is {octagon_area} cm^2\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    return octagon_output

#Här under hittar ni era namn där ni ska ange funktionen ni vill anropa som ni får definiera här ovanför.
#ändra choice text strängen med er valda objekt.

while True:
    try:
        choice = eval(input("1: Cube\n2:Carl\n3:Octagon\n4:Ian\n5:Erik\nVolume calculator, input choice:"))
        if choice == 1:
            cube()
        elif choice == 2:
            Carl()
        elif choice == 3:
            print(octagon_area())
        elif choice == 4:
            Ian()
        elif choice == 5:
            Erik()
    except NameError:
        print("Error! Error! Error! Invalid input, try again.")