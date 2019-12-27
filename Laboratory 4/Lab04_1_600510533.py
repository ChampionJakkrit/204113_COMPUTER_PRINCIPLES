#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 04
# Problem 1
# 204113 Sec 02A

def main():
    c, radius = map(str, input().split())
    r, w, h = map(str, input().split())

    for i in range(4):
        inputs = input()
        if inputs == "cp":
            circle = Circle(int(radius))
            print(circle.perimeter())

        if inputs == "ca":
            circle = Circle(int(radius))
            print(circle.area())

        if inputs == "rp":
            rectangle = Rectangle(int(w), int(h))
            print(rectangle.perimeter())

        if inputs == "ra":
            rectangle = Rectangle(int(w), int(h))
            print(rectangle.area())

class Circle(object):

    def __init__(self, r):
        self.r = r

    def perimeter(self):
        perimeter_circle = 2 * 3.14 * self.r
        return perimeter_circle

    def area(self):
        area_circle = 3.14 * self.r * self.r
        return area_circle

class Rectangle(object):

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def perimeter(self):
        perimeter_rectanggle = (self.w + self.h) * 2
        return perimeter_rectanggle

    def area(self):
        area_rectangle = self.w * self.h
        return area_rectangle

if __name__ == '__main__':
    main()