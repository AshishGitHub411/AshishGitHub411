class Parrot:
 
 # class attribute
 species = "bird"

# instance attribute
 def __init__(self, name, age):
    self .name = name
    self . age = age

# instance method 
def sing(self, song):
    return "{} is now dancing" .format(self.name, song)

def dance(self):
   return "{} is now dancing" .format(self.name)

# instantiat the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())