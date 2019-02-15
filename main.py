from Circle import *
from Triangle import *
from Square import *
from sort_2 import *

shape_list = []

circle1 = Circle(3,4,5)
shape_list.append(circle1)
        
square = Square(1,10,-4)
shape_list.append(square)
        
circle2 = Circle(10,6,3)
shape_list.append(circle2)
        
triangle = Triangle(5,-7,3)
shape_list.append(triangle)
        
square2 = Square(7,15,1)
shape_list.append(square2)

sort = SortShape()
sort.sortShape(shape_list)

print("The shape list database contains "+str(len(shape_list))+" shapes.")

for item in shape_list:
    item.display(item.order,item.x_location,item.y_location)

