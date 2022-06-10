# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:09:25 2022

@author: marc_
"""

# %%
import random
import numpy as np
echec_dim = 8

class individu:
    def __init__(self , val = None):
        if val == None:
            self.val = random.sample(range(echec_dim),echec_dim)
        else:
            self.val = val
        self.nbconflict = self.fitness()
    
    def __str__(self):
        return str(self.val)
    
    def conflict(p1 , p2):
        #? Retourne TRUE si la reine à la position p1 est en conflit
        #? avec la reine à la position p2
        return p1[0] == p2[0] or p1[1] == p2[1] or abs(p1[0]-p2[0]) == abs(p1[1]-p2[1])
    
    def fitness(self):
        #? Evaluer l'individu c'est connaitre le nombre de conflit
        self.nbconflict = 0
        for i in range(echec_dim):
            for j in range(i+1 , echec_dim):
                if (individu.conflict ([i , self.val[i] ] , [j , self.val[j]])):
                    self.nbconflict += 1
        return self.nbconflict

# %%
def create_rand_pop(count):
    #? Créer une population de taille count
    return [individu() for i in range(count)]

# %%
def evaluate(pop):
    #? Retourne une liste des individus triés selon le nombre de conflit de chacun
    return sorted(pop , key = lambda x: x.nbconflict)

# %%
def selection(pop , hcount , lcount):
    #? Retourne une sous population avec les "hcount" premiers éléments
    #? et les "lcount" derniers éléments de la liste pop.
    return pop[:hcount] + pop[-lcount:]

# %%
def croisement(ind1 , ind2):
    #? Retourne une liste de deux individus à partir de deux individus ind1 et ind2
    #? (4 premieres données de ind1 suivies des 4 dernieres de ind2 puis 4 premieres
    #? de ind2 suivies des 4 dernieres de ind1)
    return [individu(ind1.val[:4] + ind2.val[4:]) , individu(ind2.val[:4] + ind1.val[4:])]

# %%
def mutation(ind):
    #? Retourne un individu ind muté
    #? (Choisi un indice aléatoirement et change la valeur de cet indice, entre 0 et 7)
    ind.val[random.randint(0,echec_dim-1)] = random.randint(0,echec_dim-1)
    return ind

# %%
def algoloopSimple():
    pop = create_rand_pop(25)
    solutiontrouvee = False
    nbriteration = 0
    while not solutiontrouvee:
        print("Iteration numéro: ", nbriteration)
        nbriteration += 1
        evaluation = evaluate(pop)
        if evaluation[0].fitness() == 0:
            solutiontrouvee = True
        else:
            select = selection(evaluation, 10, 4)
            croises = []
            for i in range(0, len(select), 2):
                croises += croisement(select[i], select[i+1])
            mutes = []
            for i in select:
                mutes.append(mutation(i))
            newalea = create_rand_pop(5)
            pop = select[:] + croises[:] + mutes[:] + newalea[:]
    print("Solution trouvee: ", evaluation[0].val)
    return evaluation[0].val

# %%
solution = algoloopSimple()

# %%
print("Solution list: " , solution)

# %%
import matplotlib.pyplot as plt

board = np.zeros((echec_dim, echec_dim))
board[::2 , ::2] = 1
board[1::2 , 1::2] = 1
for i in range(echec_dim):
    board[i, solution[i]] = 3
plt.imshow(board, cmap = 'binary')
plt.show()

# %%
total_iter = 0

def algo_loop_infinite(list_solution, total_iter):
    pop = create_rand_pop(25)
    solutiontrouvee = False
    nbriteration = 0
    while not solutiontrouvee:
        nbriteration += 1
        evaluation = evaluate(pop)
        if evaluation[0].fitness() == 0:
            solutiontrouvee = True
        else:
            select = selection(evaluation, 10, 4)
            croises = []
            for i in range(0, len(select), 2):
                croises += croisement(select[i], select[i+1])
            mutes = []
            for i in select:
                mutes.append(mutation(i))
            newalea = create_rand_pop(5)
            pop = select[:] + croises[:] + mutes[:] + newalea[:]
    if evaluation[0].val not in liste_solution:
        print(f"Solution [iter_sol = {nbriteration} & iter_total = {total_iter}]: ", evaluation[0].val)
        total_iter += 1
        liste_solution.append(evaluation[0].val)
        #! Apres de nombreux tests, je me suis rendu compte qu'il faut environ 92 iterations pour trouver toutes les solutions
        if total_iter == 91:
            return 
        algo_loop_infinite(liste_solution,total_iter)
    else:
        algo_loop_infinite(liste_solution,total_iter)
    return liste_solution

liste_solution = []
algo_loop_infinite(liste_solution,total_iter)

# %%
import numpy as np

# %%
del(echec_dim, individu, create_rand_pop, evaluate, selection, croisement, mutation, algoloopSimple)

# %%
data = np.random.normal(0 , 1 , (500 , 3))

# %%
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(10,10))
# choose projection 3d for creating a 3d graph
axis = fig.add_subplot(111, projection='3d')
axis.scatter(
    data[:,0],
    data[:,1],
    data[:,2],
    cmap='plasma'
)

# %%
mean = np.mean(data, axis=0)
print(mean)

# %%
std = np.std(data, axis=0)
print(std)

# %%
data_normalized = (data - mean) / std
print(data_normalized)

# %%
def normalisation(data):
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    data_normalized = (data - mean) / std
    return data_normalized

normalisation(data)

# %%
datanorm = normalisation(data)

# %%
datanorm_transpose = datanorm.T

# %%
covariance = np.dot(datanorm_transpose, datanorm)
print(covariance.shape)

covariance = np.cov(datanorm.T)
print(covariance.shape)

# %%
eigen_values, eigen_vectors = np.linalg.eig(covariance)
print("Valeurs propre: ",eigen_values)
print("Vecteurs propre: \n",eigen_vectors)

# %%
eigen_vectors = eigen_vectors[:, np.argsort(eigen_values)]
print("Vecteurs propre triés: \n",eigen_vectors)

# %%
pca = eigen_vectors[:, :2]
print("Matrice pca: \n",pca)

# %%
projected_data = np.dot(datanorm, pca)
print("Projected data: \n",projected_data)

# %%
fig = plt.figure(figsize=(10,10))
plt.scatter(
    projected_data[:,0],
    projected_data[:,1],
    cmap='plasma'
)




