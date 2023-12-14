import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx**2 + dy**2)

#
point1 = Point(1, 2)
point2 = Point(4, 6)


print("Point 1:", point1)
print("Point 2:", point2)

# Calculate and print the distance between the points
distance_between_points = point1.distance(point2)
print(f"Distance between Point 1 and Point 2: {distance_between_points}")
