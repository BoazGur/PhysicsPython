
import math

class Shape(object):
    def __init__(self, points):
        self.points = points # tuples

    def perimeter(self):
        perimeter = 0
        for i in range(len(self.points) - 1):
            perimeter += math.dist(self.points[i], self.points[i + 1])    
        perimeter += math.dist(self.points[0], self.points[-1])
        
        return perimeter
    
class Quadrilateral(Shape):
    def __init__(self, points):
        assert len(points) == 4, 'Should have 4 points'

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    raise Exception('Cannot have same points')

        super().__init__(points)

class Parallelogram(Quadrilateral):
    def __init__(self, points):
        super().__init__(points)

        up_down_equal = math.dist(self.points[0], self.points[1]) == math.dist(self.points[2], self.points[3])
        right_left_equal = math.dist(self.points[0], self.points[2]) == math.dist(self.points[1], self.points[3])

        assert up_down_equal and right_left_equal, 'Not a parallelogram' 
    
class Rectangle(Parallelogram):
    def __init__(self, points):
        super().__init__(points)

        a = math.dist(self.points[0], self.points[1])
        b = math.dist(self.points[1], self.points[2])
        c = math.dist(self.points[0], self.points[2])

        assert a**2 + b**2 != c**2, 'Not a rectangle'

    def area(self):
        a = math.dist(self.points[0], self.points[1])
        b = math.dist(self.points[1], self.points[2])

        return a * b

class Rhombus(Parallelogram):
    def __init__(self, points):
        super().__init__(points)

        is_rhombus = math.dist(self.points[0], self.points[1]) == math.dist(self.points[1], self.points[2])
        assert not is_rhombus, 'Not a rhombus'

class Square(Rectangle, Rhombus):
    def __init__(self, points):
        super(Square, self).__init__(points)

# s = Shape([(0, 0), (1, 0), (0, 1)])
# print(s.perimeter())  # 3.414

# q = Quadrilateral([[0, 0], [1, 0], [1, 1]])  # error

# q = Quadrilateral([[0, 0], [1, 0], [1, 1], [0, 1]])
# print(q.perimeter())  # 4

# p = Parallelogram([(0, 0),(2, 0),(1, 1),(0, 1)])

# r = Rectangle([(0, 0), (1, 0), (1, 1), (0, 1)])
# print(r.area())  # 1