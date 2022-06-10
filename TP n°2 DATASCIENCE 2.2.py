# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 15:10:11 2022

@author: marc_
"""

#%%
#Exo1
ch="12 13 10 8 20"
my_list = [int(i) for i in ch.split()]
print(my_list)

results = list(map(int, ch.split()))
print(results)

#%%
#Exo2
test = [1,2,3,4,6]
values1 = ['a', 'b', 'c', 'd', 'e']
values2 = ['A', 'B', 'C', 'D', 'E']

result = tuple(map(lambda a,b,c : a if c%2 else b,values1,values2,test))

print(result)
#%%
#Exo3
N=10
my_list = [2**x for x in range (N)]
print(my_list)
#%%
#Exo4
numbers=[-1,-2,-3,4,5,10,-5,3]

my_list = [x**2 for x in numbers if x < 0]
print(my_list)
#%%
#Exo5
n=10
x=7
X=2
my_list = [x for x in range (n + 1) if x%X != 0]
print(my_list)
#%%
#Exo6
Sentence ="Salut les gens de la Street"
revert = " ".join ([x[::-1] for x in Sentence.split()])
print(revert)
#%%
#Exo7
Sentence ="Salut les gens de la Street - 12"
word = " ".join([x for x in Sentence.split() if x.isalpha() and x.islower()])
print(word)

#%%
#Exo8

s1 = "Hello World"
s2 = "Hello kitty"
print("Nous avons comme premiere string au départ: ",s1)
print("Nous avons comme seconde string au départ : ",s2)
s1 = s1.lower()
s2 = s2.lower()
s1_list = s1.split()
s2_list = s2.split()
for word in s1_list:
    for i in range(0 , len(s2_list)):
        if word == s2_list[i]:
            s1_list[s1_list.index(word)] = word.upper()
            s2_list[i] = word.upper()
s1 = " ".join(s1_list)
s2 = " ".join(s2_list)
print("\ns1 Nous avons comme seconde string à la fin : ",s1)
print("s2 Nous avons comme seconde string à la fin  : ",s2)    

#%%
#Exo9
dico={'b':1, 'a':2, 'd':5}
dico = {value:key for key, value in dico.items()}
print(dico)
    
#%%
#Exo10
my_dict = {"a":"b", "b":"c", "c":"a"}
correspondances = {"a":"A", "b":"B", "c":"C"}
dico = dict((key,correspondances[value]) for key, value in my_dict.items())
print(dico)
    
#%%
#Exo11
l=[5,3,10,4,8,20,2]
l.sort()
print(l)

l=["bonjour","tout","le","monde"]
l.sort(key=lambda v: len(v))
print(l)

l=[ [1,0,5],[1,2,3], [8,5] ]
l.sort(key=len)
print(l)

l=[('Luc',22),('Lea',18),('Alice',23),('Luca',21), ('Max',20) ]
l.sort()
print(l)
l.sort(key = lambda x: x[1]) 
print(l)


#%%
#Exo12
def boomerang(l):
    for i in l+l[::-1]:
        yield i
    
l = [1,2,3]
for x in boomerang(l):
    print(x)
    
#%%
#Exo partie 2
#le contructeur est le __init__() et est toujours appelé quand un objet et crée. 
#les variables d'instances sont self.nomClient, self.iban, et le self.solde . 
#les variables de classes sont cb_Count
#c'est class CompteBancaire() qui a permis l'utilisation de la classe print(c2).
#c'est ... qui a permis le test == .
    
from math import sqrt 
  
class Vector: 
  
    
    def __init__(self, x, y, z): 
        self.x = x 
        self.y = y 
        self.z = z 
  
    
    def magnitude(self): 
  
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2) 
  
    
    def __add__(self, V): 
  
        return Vector(self.x + V.x, self.y + V.y, self.z + V.z) 
  
    
    def __sub__(self, V): 
  
        return Vector(self.x - V.x, self.y - V.y, self.z - V.z) 
  
    
    def __xor__(self, V): 
  
        return self.x * V.x + self.y * V.y + self.z * V.z 
    
    def __mul__(self, V): 
  
        return Vector(self.y * V.z - self.z * V.y, 
                      self.z * V.x - self.x * V.z, 
                      self.x * V.y - self.y * V.x) 
  
    
    def __repr__(self): 
  
        out = str(self.x) + "i "
  
        if self.y >= 0: 
            out += "+ "
        out += str(self.y) + "j "
        if self.z >= 0: 
            out += "+ "
        out += str(self.z) + "k"
  
        return out 
  
  
if __name__ == "__main__": 
  
    vec1 = Vector(1, 2, 2) 
    vec2 = Vector(3, 1, 2) 
  
    
    
    print("Addition of vector1 and vector2: " + str(vec1 + vec2)) 
  
    
    print("Subtraction of vector1 and vector2: " + str(vec1 - vec2)) 
  
    
    print("Dot Product of vector1 and vector2: " + str(vec1 ^ vec2)) 

    
