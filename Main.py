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
        


my_room = Room()

my_room.add_chunk(23, 78, 12)
my_room.add_chunk(12, 88, 123)

my_room.describe()

input("")