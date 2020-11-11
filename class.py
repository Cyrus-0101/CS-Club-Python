#!/usr/bin/env python3
# Copyright 2018-2020 GCN http://www.0101solutions.consulting/

# We begin by defining the class, and then defining the methods, and class variables.
class Duck:
    # The 'self' arguement, is a refrence to the object. 
    # And we use this to reference the object itself.

    sound = 'Quaack!'
    walking = 'Walking like a duck'
    age = 'Five'
    
    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walking)

    def age(self):
        print(self.age)

def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    donald.age() # Refer to docs

if __name__ == '__main__': main()
