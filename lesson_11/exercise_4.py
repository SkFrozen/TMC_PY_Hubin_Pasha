class Sphere:

    def __init__(self, radius=1, Ox=0, Oy=0, Oz=0):
        self.radius = radius
        self.Ox = Ox
        self.Oy = Oy
        self.Oz = Oz

    def get_volume(self):
        return f"{(4 / 3) * 3.14 * pow(self.radius, 3):.2f}"

    def get_square(self):
        return f"{4 * 3.14 * pow(self.radius, 2):.2f}"

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.Ox, self.Oy, self.Oz

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, Ox, Oy, Oz):
        self.Ox, self.Oy, self.Oz = Ox, Oy, Oz

    def is_point_inside(self, Ox, Oy, Oz):
        dot = pow(Ox - self.Ox, 2) + pow(Oy - self.Oy, 2) + pow(Oz - self.Oz, 2)
        return dot < self.radius**2


first_sphere = Sphere()

print(first_sphere.get_volume())
print(first_sphere.get_square())
print(first_sphere.get_radius())
print(first_sphere.get_center())

first_sphere.set_radius(5)
first_sphere.set_center(4, 3, 4)
print(first_sphere.get_volume())
print(first_sphere.get_square())
print(first_sphere.get_radius())
print(first_sphere.get_center())
print(first_sphere.is_point_inside(6, 5, 8))
