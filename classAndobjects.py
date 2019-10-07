# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 22:59:53 2018

@author: Carlos Isaac
"""
#class Clock(object):
#    def __init__(self, time):
#        self.time = time
#    def print_time(self):
#        time = '6:30'
#        print(self.time)
#
#clock = Clock('5:30')
#clock.print_time()

#class Weird(object):
#    def __init__(self, x, y): 
#        self.y = y
#        self.x = x
#    def getX(self):
#        return x 
#    def getY(self):
#        return y
#
#class Wild(object):
#    def __init__(self, x, y): 
#        self.y = y
#        self.x = x
#    def getX(self):
#        return self.x 
#    def getY(self):
#        return self.y
#
#X = 7
#Y = 8

#class intSet(object):
#    """An intSet is a set of integers
#    The value is represented by a list of ints, self.vals.
#    Each int in the set occurs in self.vals exactly once."""
#
#    def __init__(self):
#        """Create an empty set of integers"""
#        self.vals = []
#
#    def insert(self, e):
#        """Assumes e is an integer and inserts e into self""" 
#        if not e in self.vals:
#            self.vals.append(e)
#
#    def member(self, e):
#        """Assumes e is an integer
#           Returns True if e is in self, and False otherwise"""
#        return e in self.vals
#
#    def remove(self, e):
#        """Assumes e is an integer and removes e from self
#           Raises ValueError if e is not in self"""
#        try:
#            self.vals.remove(e)
#        except:
#            raise ValueError(str(e) + ' not found')
#    
#    def intersect(self, other):
#        res = intSet()
#        for val in self.vals:
#            if val in other.vals:
#                res.insert(val)
#        return res
#
#    def __str__(self):
#        """Returns a string representation of self"""
#        self.vals.sort()
#        return '{' + ','.join([str(e) for e in self.vals]) + '}'
#    
#    def __len__(self):
#        count = 0
#        for val in self.vals:
#            count += 1
#        return count
#
#setA = intSet()
#print(setA)
#setB = intSet()
#print(setB)

#class Spell(object):
#    def __init__(self, incantation, name):
#        self.name = name
#        self.incantation = incantation
#
#    def __str__(self):
#        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
#              
#    def getDescription(self):
#        return 'No description'
#    
#    def execute(self):
#        print(self.incantation)
#
#
#class Accio(Spell):
#    def __init__(self):
#        Spell.__init__(self, 'Accio', 'Summoning Charm')
#
#class Confundo(Spell):
#    def __init__(self):
#        Spell.__init__(self, 'Confundo', 'Confundus Charm')
#
#    def getDescription(self):
#        return 'Causes the victim to become confused and befuddled.'
#
#def studySpell(spell):
#    print(spell)
#
#spell = Accio()
#spell.execute()
#studySpell(spell)
#studySpell(Confundo())


class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")
        
obj = D()
print(obj.a)