# class Animal:
#     def __init__(self):
#         num_of_eyes = 2
#
#     def breathe(self):
#         print("Inhale, Exhale.")
#
#     def move(self):
#         print("move method is called")
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#     def breathe(self):
#         super().breathe()
#         super().move()
#         print("Fish Breathe beneath the water.")
#
#     def swim(self):
#         print("Moving in water")
#
# nemo = Fish()
# nemo.swim()
# nemo.breathe()

# SLCING
piano_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(piano_keys[2:7:3])