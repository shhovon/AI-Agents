matrix = []
counter = 0
oddRow = 0
evenRow = 0
dimension = int(input("Enter dimension of the matrix: "))
rows, cols = (int(dimension), int(dimension))
print("Matrix dimention: " + str(dimension))
print("Enter the matrix elements: ")

for i in range(0, dimension):
   row = list(map(int, input().split()))
   matrix.append(row)

print("Matrix: " + str(matrix))

for inv in range(rows):
     for con in range(cols):
         compare = matrix[inv][con]
         for i in range(rows):
             for j in range(cols):
                 if  compare > matrix[i][j] and compare > 0:
                     counter = counter+1
                 elif matrix[i] == 0:
                    oddRow = oddRow+1
                 elif matrix[j] != 0:
                    evenRow = evenRow+1

print("Inversion: "+ str(counter))

if(dimension % 2) != 0:
    if(counter % 2) == 0:
        print("Solvable")
elif(dimension % 2) == 0:
   if(oddRow != 0):
      print("Solvable")
   elif(evenRow != 0):
      print("Solvable")
##   else:
##      print("Not Solvable")
if(counter % 2) != 0:
   print("Not Solvable")

