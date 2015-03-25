class matrix():
	name = 'unnamed'
	n=1  #number of equations
	m=1  #number of variables
	def __init__(self):
		self.values = []	#arrays in classes append to each other, do this to avoid

def create(head):
	a = matrix()	#temp class
	print("")
	a.name = input("name matrix: ")
	a.n = int(input("number of eqations: "))
	a.m = int(input("number of variables: "))
	count = 0
	while count < (a.m*a.n):	#brings in matrix values
		b = int(input(") "))
		a.values.append(b)
		count += 1
	head.append(a)	#appends the tep class to the class matrix
	print("")

def print_array(vector):
	i = 0
	while (i+1) <= len(vector.values):
		if (i%vector.m) == 0:
			print("")	#puts in new lines
		print( str(vector.values[i]),end="")	#,end="" removes newline
		i += 1
	i = 0
	print("")
	print("")

def A_x_Const(const,vector):
	i = 0
	print_array(vector)
	print("* " + str(const))
	print("---------")
	while (i+1) <= len(vector.values):
		vector.values[i] *= const
		i += 1
	print_array(vector)

def swap(L_one,L_Two,vector):
	i = 0
	temp = 0
	while i < vector.m:
		temp = vector.values[L_one*]

def display_arrays(matrixes):
	i = 0

	while i < len(matrixes):	#prints our matrixes saved
		print(str(i) + ") " +matrixes[i].name)
		i += 1
	W_name = -1
	while W_name > (i-1) or W_name < 0:
		try:
			W_name = int(input("matrix number: "))	#selects matrix to print
		except ValueError:
			k = 0
			while k < len(matrixes):
				if matrixes[k].name == str(W_name):
			  		W_name = k	
				k += 1
			  	#end of while

	return W_name	#returns the key for mmatrix

#main program starts
print("this is for linear systems")
matrixes = []
end = 0
while end != 1:	#main loop
	print("1) quit")
	print("2) add matrix")
	print("3) print a matrix")
	print("4) test")

	op = input("enter operation number: ")	#operations

	if op == '1':
		end = 1
	elif op == '2':
		create(matrixes)
	elif op == '3':
		print_array(matrixes[display_arrays(matrixes)])
	elif op == '4':
		factor = int(input("enter number to factor by: "))
		A_x_Const(factor,matrixes[0])

#main program ends