from Graphics.RectFunction import*
from Graphics.CircleFunction import*
from Graphics.DGraphics.SphereFunction import*
from Graphics.DGraphics.CuboidFunction import*
l = int(input("Enter length:"))
b = int(input("Enter breadth:"))
print("Rectangle Area =", RectArea(l,b))
print("Rectangle Perimeter =",RectPerimeter(l,b))
r = int(input("Enter radius of circle: "))
print("Circle Area =",CirArea(r))
print("CirclePerimeter =",CirPerimeter(r))
r = int(input("Enter radius of Sphere: "))
print("Sphere Area =",SpArea(r))
print("Sphere Volume =",SpPerimeter(r))
l = int(input("Enter cuboid length:"))
b = int(input("Enter cuboid breadth:"))
h = int(input("Enter cuboid height:"))
print("Cuboid Area =", CubArea(l,b,h))
print("Cuboid Perimeter =",CubPerimeter(l,b,h))
