x = int(input("Enter number of rows: "))
y = int(input("Enter number of columns: "))
mat = [[0 for i in range(y)]for j in range(x)]

for i in range(0,x):
    for j in range(0,y):
        mat[i][j]=int(raw_input())
print "This is the matrix ", mat
#[...} contains row values
print '\n'
for i in range(0,x):
      for j in range(0,y):
          if(i>j):
              temp = mat[i][j]
              mat[i][j] = mat[j][i]
              mat[j][i] = temp
print "This is it's transpose ", mat
      

