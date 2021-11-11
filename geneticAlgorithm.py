import random

chromo1 = [0, 0, 0 ,0, 0, 0, 0, 0]
chromo2 = [1, 1, 1, 1, 1, 1, 1, 1]
chromo3 = [1, 1, 0, 1, 0, 0, 0, 1]
chromo4 = [0, 1, 1, 0, 1, 0, 0, 0]

randomAnswer1= []
randomAnswer2= []
randomAnswer3= []
randomAnswer4= []
newValue=[]

 
#def fitness:
    ## choose biggest chromo
    ## check for 3 0's

#def crossover:
    ## select 2 chromo and random position select, split two chromo in half
    
randomChromo1 = random.choice(chromo1)
randomChromo2 = random.choice(chromo2)
randomChromo3 = random.choice(chromo3)
randomChromo4 = random.choice(chromo4)

print("\n=========== Crossover Chromosomes ===========\n")

##print(chromo1)
##print(chromo2)
##print(chromo3)
##print(chromo4)

print(str(chromo1) + " - Chromosome 1")
print(str(chromo2) + " - Chromosome 2")
print(str(chromo3) + " - Chromosome 3")
print(str(chromo4) + " - Chromosome 4")

##def randomAnswerFunc(chromo):
##    ##chromo=chromo
##    length = len(chromo)
##    middle_index = length//2
##    first_half = chromo1[:middle_index]
##    second_half = chromo1[middle_index:]
##    print(first_half)
##    print(second_half)

##randomAnswerFunc(chromo1)
##randomAnswerFunc(chromo2)
##randomAnswerFunc(chromo3)
##randomAnswerFunc(chromo4)
    
length = len(chromo1)
middle_index = length//2
first_half = chromo1[:middle_index]
second_half = chromo1[middle_index:]

length2 = len(chromo2)
middle_index = length//2
first_half2 = chromo2[:middle_index]
second_half2 = chromo2[middle_index:]

length3 = len(chromo3)
middle_index3 = length//2
first_half3 = chromo3[:middle_index]
second_half3 = chromo3[middle_index:]

length4 = len(chromo4)
middle_index4 = length//2
first_half4 = chromo4[:middle_index]
second_half4 = chromo4[middle_index:]



print("\n======== Splited and Before Mutation ========\n")

randomAnswer1 = first_half + second_half2
##print(randomAnswer1)
print(str(randomAnswer1) + " - Chromosome 1")

randomAnswer2 = first_half2 + second_half
print(str(randomAnswer2) + " - Chromosome 2")

randomAnswer3 = first_half3 + second_half4
print(str(randomAnswer3) + " - Chromosome 3")

randomAnswer4 = first_half4 + second_half3
print(str(randomAnswer4) + " - Chromosome 4")

##def mutation:
    ## random position choose and change its value, 0=1, 1=0
    ## repeat fitness function

randomMutation1 = random.choice(randomAnswer1)
randomMutation2 = random.choice(randomAnswer2)
randomMutation3 = random.choice(randomAnswer3)
randomMutation4 = random.choice(randomAnswer4)
for r, v in enumerate(randomAnswer1):
    if v == 0:
        randomAnswer1[r] = 1
    else:
        randomAnswer1[r] = 0
        
for r, v in enumerate(randomAnswer2):
    if v == 0:
        randomAnswer2[r] = 1
    else:
        randomAnswer2[r] = 0
        
for r, v in enumerate(randomAnswer3):
    if v == 0:
        randomAnswer3[r] = 1
    else:
        randomAnswer3[r] = 0
        
for r, v in enumerate(randomAnswer4):
    if v == 0:
        randomAnswer4[r] = 1
    else:
        randomAnswer4[r] = 0

print("\n============== After Mutation ===============\n")

print(str(randomAnswer1) + " - Chromosome 1")
print(str(randomAnswer2) + " - Chromosome 2")
print(str(randomAnswer3) + " - Chromosome 3")
print(str(randomAnswer4) + " - Chromosome 4")
