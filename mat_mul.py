def print_matrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			print(matrix[i][j])
		print("\n")
	for h in matrix:
		print (h)
		
#def main():
r1=int(input("enter first matrix rows:"))
c1=int(input("enter first matrix columns:"))
r2=int(input("enter second matrix rows:"))
c2=int(input("enter second matrix columns:"))
if(c1!=r2):
	print("matrix multiplication is not possible:")
	exit()
#declaration of arrays
array1=[[0 for j in range (0,c1)] for i in range (0,r1)]
array2=[[0 for j in range (0,c2)] for i in range (0,r2)]
result=[[0 for j in range (0,c2)] for i in range (0,r1)]
print ("enter first matrix elements:" )
for i in range(0 , r1):
	for j in range(0 , c1):
		array1[i][j]=int (input("enter element"))
print ("enter second matrix elements:")
for i in range(0 , r2):
	for j in range(0 , c2):
		array2[i][j]=int(input("enter element"))
print ("first matrix")
print_matrix(array1)
print ("second matrix")
print_matrix(array2)
for i in range(0 , r1):
	for j in range(0 , c2):
		for k in range(0 , c1):
			result[i][j] += array1[i][k] * array2[k][j]
print ( "multiplication of two matrices:" )
print_matrix(result)
