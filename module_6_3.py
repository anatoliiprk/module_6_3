print(f'------\nЗадача "Мифическое наследование"\n------')

class Horse:
    def __init__(self, x_distance = 0, y_distance = 0, sound = 'Frrr', dy = 0):
        self.x_distance = x_distance
        self.sound = sound
        super().__init__(y_distance)

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance

class Eagle:
    def __init__(self, y_distance = 0, sound = 'I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance

class Pegasus(Horse, Eagle):
    def __init__(self, x_distance = 0, y_distance = 0, sound = '', dx = 0, dy = 0):
        super().__init__(x_distance, y_distance, sound)
        super().run(dx)
        super().fly(dy)

    def move(self, dx: int, dy: int):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        coordinates = (self.x_distance, self.y_distance)
        return coordinates

    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(2, 12)
print(p1.get_pos())

p1.voice()

print('------')