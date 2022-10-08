print('hello world')
class Plane:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_free_places = self.capacity

    def make_reservation(self, num):
        if num > self.current_free_places:
            raise ValueError(f'OVerbookin Error!!! Current free places value is {self.current_free_places}')
        self.current_free_places -= num

plane1 = Plane(10)
plane2 = Plane(20)
plane3 = Plane(220)
print(plane3.current_free_places)
try:
    plane3.make_reservation(221)
except Exception as err:
    print(err)
print(plane3.current_free_places)
print(plane3.temp)