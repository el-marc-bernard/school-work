# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 08:21:09 2022

@author: marc_
"""

#%%TDn°4
#%%Partie 1: Le problème des 8 reines 

import numpy as np 

import random
echec_dim=8


class create_rand_pop(count):
    for i in range count:
        
         

class individu :
    def __init__(self,val=None):
        if val == None :
            self.val=random.sample(str)
        else:
            self.val=val
    
    def confllict (p1,p2):
        #retourne true si la reine à la position p1 est en conflit avec la reine en position p2
        if p1[1]==p2[1] or p1[0]==p2[0] or abs(p1[0]) - p2[0] == abs(p2[0]) - p1[0]:
            return True 
        else: 
            return False
        
    def fitness(self):
        #évaluer l'individu c'est connaitre le notre de conflit 
        self.nbconflict = 0
        for i in ....:
            for j in ....:
                if(individu.conflict([i,...],[j,....])):
                    self.nbconflict=self.nbconflict+1
        return self.nbconflic1
        
    def evaluate(pop):
        liste_pop = sorted(pop, lambda x: x.nbconflict, reverse=True)
        
    
    def selection(pop,hcount,lcount):
        v1 = np.array([1,2,3,4,5])
        v2 = np.array([2,3,4,5,6])
        v3 = v1+v2
        
    def croisement(ind1,ind2):
    
    def mutation(ind):
            individu = np.random.randn(ind[i]==np.random.randn(value))
    def algoloopSimple():
        pop=create_rand_pop(25)
        solutiontrouvee=False
        nbriteration=0
        while not solutiontrouvee:
            print("itération numéro n°:",nbriteration)
            nbriteration+=1
            evalution=evalution(pop)
            if evalution[0].fitness()==0:
                solutiontrouvee=True
            else:
                select=selection(evaluation,10,4)
                croises=[]
                for i in range (0,len(select),2):
                    croises+=croisement(select[i],select[i+1])
                mutes=[]
                for i in select: 
                    mutes.append(mutation(i))
                newalea=create_rand_pop(5)
                pop=select[:]+croises[:]+mutes[:]+newalea[:]
    print(evaluation[0])
    
    
#%%Partie 2

import numpy as np

data = np.random.randn(500,3)
print(data)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(10,10))
# choose projection 3d for creating a 3d graph
axis = fig.add_subplot(111, projection='3d')
axis.scatter(
data[:,0],
data[:,1],
data[:,2],
cmap='plasma')

column_mean_0 = np.mean(data[:,0]) 
print (column_mean_0)
column_mean_1 = np.mean(data[:,1]) 
column_mean_2 = np.mean(data[:,2])
print (column_mean_1)
print (column_mean_2)

écart_type_0= np.std(data[:,0])
print(écart_type_0)
écart_type_1= np.std(data[:,1])
print(écart_type_1)
écart_type_2= np.std(data[:,2])
print(écart_type_2)


#%%
#Q10


#%%
#Q11
projecteddata = datanorm*pca
#%%
#Q12

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(10,10))
plt.scatter(
projecteddata[:,0],
projecteddata[:,1]
cmap='plasma'
)
 

        