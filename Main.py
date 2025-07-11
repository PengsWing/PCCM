import random

class fRoom:
    def __init__(self):
        self.room = [] #each is a room object
        
    def add_room(self, room):
        self.room.append(room)
        
    def total_volume(self):
        return sum(room.volume() for room in self.room)
        
    def total_floor_area(self):
        return sum(room.floor_area() for room in self.room)
        
    def describe(self):
        print(f"FRoom has {len(self.room)} Room(s):")
        for i, room in enumerate(self.room, 1):
            print(f"Room {i}:")
            room.describe()
        print(f"\n==> Total FRoom Volume: {self.total_volume()} units^3")
        print(f"==> Total FRoom Floor Area: {self.total_floor_area()} units^2")

class Room:
    def __init__(self):
        self.chunk = [] #each chunk is define with xyz
        
    def add_chunk(self, x, y, z):
        self.chunk.append({'x': x, 'y': y, 'z': z})
        
    def volume(self):
        return sum(chunk['x'] * chunk['y'] * chunk['z'] for chunk in self.chunk)
        
    def floor_area(self):
        return sum(chunk['x'] * chunk['z'] for chunk in self.chunk)
        
    def describe(self):
        print(f"Room has {len(self.chunk)} chunk(s):")
        for i, chunk in enumerate(self.chunk, 1):
            x, y, z = chunk['x'], chunk['y'], chunk['z']
            volume = x * y * z
            area = x * z
            print(f" Chunk{i}: {x} x {y} x {z} = {x * y * z} units^3 (Floor Area: {area}units^2)")
        print(f"Total Volume: {self.volume()} units^3")
        print(f"Total Floor Area: {self.floor_area()} units^2")
        


def generate_random_room(max_chunks=3):
    room = Room()
    for _ in range(random.randint(1, max_chunks)):
        x = random.randint(2,10)
        y = random.randint(2,10)
        z = random.randint(2,10)
        room.add_chunk(x, y, z)
    return room
    
def generate_random_froom(max_rooms=3):
    froom = fRoom()
    for _ in range(random.randint(1, max_rooms)):
        froom.add_room(generate_random_room())
    return froom

froom1 = generate_random_froom()
froom2 = generate_random_froom()

froom1.describe()
print("\n---\n")
froom2.describe()

input("")