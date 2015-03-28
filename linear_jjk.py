class matrix():
	name = 'unnamed'
	d = 0 #number of dementions
	v = []  #vaiables in demetion
	def __init__(self):
		self.values = []	#arrays in classes append to each other, do this to avoid

#utility: creates a matrix
def add_one(a, z, i):
	if z[i] == a[i]:
		z[i] = 0
		z = add_one(a,z,i+1)
	else:
		z[i] += 1
	return z

def create(head):
	a = matrix
	z = []
	a.name = input("name matrix: ")
	a.d=int(input("Number of Dimentions: "))
	for i in range(a.d):
	        a.v.append(int(input(") ")))
	        z.append(0)
	j = "0"
	for q in range(a.d):
	        j = "[" + j + " for q in range(a.v[" + str(q) + "])]"
	print (j)
	a.values = eval(j)
	print (a.values)
	for i in range(a.d):
	        a.v[i] -= 1
	z[0] = -1
	while z != a.v:
		z = add_one(a.v, z, 0)
		if a.d == 1:
			a.values[z[0]] = int(input(") "))
		elif a.d == 2:
			a.values[z[1]][z[0]] = int(input(") "))
		elif a.d == 3:
			a.values[z[2]][z[1]][z[0]] = int(input(") "))
		elif a.d == 4:
			a.values[z[3]][z[2]][z[1]][z[0]] = int(input(") "))
		elif a.d == 5:
			a.values[z[4]][z[3]][z[2]][z[1]][z[0]] = int(input(") "))
	print (a.values)

	head.append(a)	#appends the tep class to the class matrix

#utility: prints an array
def print_array(vector):
	z = []
	for i in range(vector.d):
		z.append(0)
	z[0] = -1
	while z != vector.v:
		z = add_one(vector.v, z, 0)
		if a.d == 1:
			print( str(vector.values[z[0]]), end=" ")
		elif a.d == 2:
			print( str(vector.values[z[1]][z[0]]), end=" ")
		elif a.d == 3:
			print( str(vector.values[z[2]][z[1]][z[0]]), end=" ")
		elif a.d == 4:
			print( str(vector.values[z[3]][z[2]][z[1]][z[0]]), end=" ")
		elif a.d == 5:
			print( str(vector.values[z[4]][z[3]][z[2]][z[1]][z[0]]), end=" ")

#utility: math loop
def linear_math(matrixes):
	done = 3
	while done != '1':
		print("1) quit")
		print("2) constant * matrix")
		print("3) line swap on matrix")
		print("4) C*L1 + L2 -> L2")
		print("5) C*L1 -> L1")

		done = input("enter operation number: ")

		if done == '1':
			print("leaving math")
		elif done == '2':
			factor = float(input("enter factor: "))
			A_x_Const(factor,matrixes[display_arrays(matrixes)])
		elif done == '3':
			L_One = int(input("enter line one: "))
			L_Two = int(input("enter line two: "))
			swap(L_One,L_Two,matrixes[display_arrays(matrixes)])
		elif done == '4':
			factor = float(input("enter the factor for line one: "))
			L_One = int(input("enter line one: "))
			L_Two = int(input("enter line two: "))
			line_math(L_One,L_Two,factor,matrixes[display_arrays(matrixes)])
		elif done == '5':
			factor = float(input("enter the factor: "))
			L_One = int(input("enter the line: "))
			line_factored(L_One,factor,matrixes[display_arrays(matrixes)])


#functionality: constant times array
def A_x_Const(const,vector):
	i = 0
	#print(str(const) + "*",end="")
	print_array(vector)
	print("* " + str(const))
	print("---------")
	while (i+1) <= len(vector.values):
		vector.values[i] *= const
		i += 1
	print_array(vector)

#functionality: swap lines
def swap(L_one,L_Two,vector):
	print_array(vector)
	print("L"+str(L_one) + " <-> L" + str(L_Two))
	i = 0
	temp = 0
	while i < vector.m: #while a row has variables
		temp = vector.values[((L_one-1)*vector.m) + i]
		vector.values[((L_one-1)*vector.m) + i] = vector.values[((L_Two-1)*vector.m) + i]
		vector.values[((L_Two-1)*vector.m) + i] = temp
		i += 1
	print_array(vector)

#functionality: line times constant added to other line
def line_math(L_one,L_two,factor,vector):
	print_array(vector)
	print("("+str(factor)+"*L"+str(L_one)+")+L"+str(L_two)+" -> L"+str(L_two))
	i = 0
	while i < vector.m: #while row has variables
		if(vector.values[((L_two-1)*vector.m) + i] != 0):
			vector.values[((L_two-1)*vector.m) + i] += vector.values[((L_one-1)*vector.m) + i] * factor
		i += 1
	print_array(vector)

#functionality: line times constant
def line_factored(line,factor,vector):
	print_array(vector)
	print(str(factor)+"*L"+str(line)+"-> L"+str(line))
	i = 0
	while i < vector.m: #while row has variables
		if(vector.values[((line-1)*vector.m) + i] != 0):
			vector.values[((line-1)*vector.m) + i] *= factor
		i += 1
	print_array(vector)

#utility: displays all matrixes
def display_arrays(matrixes):
	i = 0

	while i < len(matrixes):	#prints our matrixes saved
		print(str(i) + ") " +matrixes[i].name)
		i += 1
	W_name = -1
	while W_name > (i-1) or W_name < 0:
		#try:
		#	W_name = int(input("matrix number: "))	#selects matrix to print
		#except ValueError:	#tries to solve if user inputs a character
		try:
			k = 0
			W_name = input("matrix name: ")	#selects matrix to print
			while k < len(matrixes):	#matches a number to the name
				if matrixes[k].name == W_name:
			  		W_name = int(k)	
				k += 1
				  	#end of while
		except ValueError: #stops the error for incorrect input
			print("enter the matrix NAME")

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
		linear_math(matrixes)
#main program ends
