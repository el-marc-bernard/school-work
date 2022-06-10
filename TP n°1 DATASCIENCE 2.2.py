# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 08:44:55 2022

@author: marc_
"""
#%%
#exo1
temps=6.892
distance=19.7
vitesse= distance/temps
print("question 1:",vitesse)
print ("question 2:","%.2f" % vitesse)

#%%
#exo2 version 1
nb1=32
nb2=42
if nb1 > nb2:
    nbmax=nb1
    nbmin=nb2
else: 
    nbmax=nb2
    nbmin=nb1
print("the max between" ,nb1, "and", nb2, "is", nbmax)
print("the min between" ,nb1, "and", nb2, "is", nbmin)


#%%
#exo2 version 2
a=32
b=42
print()
if a > b:
 print("version 1: the max bewtween a and b is a which value is",a)
else:
  print("version 1: the max bewtween a and b is b which value is",b)
print("version 2: the max between the two values is " ,(max(a,b)))
print("version 3: ",(a if a>b else b))
#%%
#exo3
def volBoite(*x):
    if (len(x) == 0):
        print(-1)
    elif (len(x) == 1):
        print(x[0]**3)
    elif (len(x) == 2):
        print(x[0]*x[0]*x[1])
    elif (len(x) == 3):
        print(x[0]*x[1]*x[2])

print("Combien d'arguments voulez-vous entrer ? ")
n = int(input())
if (n == 0):
    volBoite()
elif (n == 1):
    volBoite(5.2)
elif (n == 2):
    volBoite(5.2,3)
elif (n == 3):
    volBoite(5.2 , 3 , 7.4)

#%%
#exo4

def eleMax(liste, *range):
    if (len(range) == 0):
        return max(liste)
    elif (len(range) == 1):
        return max(liste[range[0]:])
    elif (len(range) == 2):
        return max(liste[range[0]:range[1]])

# Will return 12 because we start from the sixth element
eleMax([3,4,1,18,34,21,9,12],6)

# Return the maximum value of the list 34 because wi didn't define a debut and end
eleMax([3,4,1,18,34,21,9,12])

# Return the max between 5 and 7 element
eleMax([3,4,1,18,34,21,9,12],5,7)
#%%
#exo5
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre',
'Décembre']
t3 = [None]*(len(t1) + len(t2))
t3[::2] = t2
t3[1::2] = t1
print(t3)
#%%
#exo6
print("Entrer une chaine de caractere : ")
char = input()
char2 = char[::-1]
print(char2)
#%%
#exo7
def mafonction(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [10, 1, 30, 3, 4, 62, 6, 7, 90, 9, 10, 11]
print(mafonction(arr))

#Cette fonction va vous permettre de trier un tableau dans l'order croissant
#%%
#exo8
starting_point = 3

# display a countdown from start to 0 in one line
for i in range(starting_point, 0, -1):
    print(i, end=" ")
print("GO!")
#%%
#exo9
word = input("Entrez un mot svp :\n")
if str(word) == str(word)[::-1] :
    print(f"{word} is palindrome indeed")
else:
    print(f"{word} is not palindrome indeed")
#%%
#exo10
my_list = [0 , 1 , 2 , 3 , 4]

l1 = my_list + my_list[::-1]

l2 = my_list[:3] * 3

l3 = [my_list[i] for i in range(len(my_list)) if i % 3 == 0]

print(l1)
print(l2)
print(l3)
#%%
#exo11
x = int(input("Entrez un chiffre :\n"))
print("pair") if (x % 2) == 0 else print("impair")

my_list = [12, 2, 31, 4, 5, 63, 7, 8, 91, 10, 11, 22]
l3 = my_list[2::3]
print(l3)
#%%
#exo12
print("Enter a phrase : ")
phrase = input()

if (len(phrase) == 0):
    print("Empty string")

def get_capital_letters(phrase):
    return "".join([c for c in phrase if c.isupper()])

print(get_capital_letters(phrase))
#%%
#exo13
chaine = "Hi people"
c = "e"
print(f"{c} apparaît {chaine.count(c)} fois dans {chaine}")
#%%
#exo14
def vowel_count(phrase):
    return len([c for c in phrase if c.lower() in "aeiouy"])

vowel_count("Hier je suis allé au batiment Tour mais il n'y avait pas de prises dans les salles.")

#%%
#exo15
my_dict=dict({'pi':3.14,'mot':"mot",'nombre':42,'liste':[1,2,3]})
print("my dictionnary contain",my_dict)

#%%
#exo 16
my_dict=dict({'pi':3.14,'mot':"mot",'nombre':42,'liste':[1,2,3]})
x = input("Entrez une key :\n")
if x in my_dict :
    print (x,"vaut",my_dict[x],"dans my_dict")
else:
    print (x,"n'est pas une clé standard de my_dict")
    
#%%
#exo 17

my_dict = dict({'pi':3.14,'mot':"mot",'nombre':42,'liste':[1,2,3]})

my_dict["hello"] = "world"
my_dict["nombre"] = "0"
my_dict.pop("pi")

print(my_dict)
#%%
#exo 18
values = [10,20,30,40,10,2,40]

s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
print("the set s1 has the values",s1)
s2 = set()
s2.update(["Hello Wold"])
print("the set s2 contain this message",s2)
s3 = set(values)
print("the set s3 has the values", s3)
s4 = set()
s4.update(range(5,16))
print("the set s4 has values",s4)




