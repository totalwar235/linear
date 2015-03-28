import header
import func

#utility: displays all matrixes
def display_arrays(matrixes):
	i = 0

	while i < len(matrixes):	#prints our matrixes saved
		print(str(i) + ") " + matrixes[i].name)
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

#utility: creates a matrix
def create(head):
	a = header.matrix()	#temp class
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

#utility: prints an array
def print_array(vector):
	i = 0
	while (i+1) <= len(vector.values):
		if (i%vector.m) == 0:
			print("")	#puts in new lines
		print( str(vector.values[i])+" ",end="")	#,end="" removes newline
		i += 1
	i = 0
	print("")
	print("")

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
			func.A_x_Const(factor,matrixes[display_arrays(matrixes)])
		elif done == '3':
			L_One = int(input("enter line one: "))
			L_Two = int(input("enter line two: "))
			func.swap(L_One,L_Two,matrixes[display_arrays(matrixes)])
		elif done == '4':
			factor = float(input("enter the factor for line one: "))
			L_One = int(input("enter line one: "))
			L_Two = int(input("enter line two: "))
			func.line_math(L_One,L_Two,factor,matrixes[display_arrays(matrixes)])
		elif done == '5':
			factor = float(input("enter the factor: "))
			L_One = int(input("enter the line: "))
			func.line_factored(L_One,factor,matrixes[display_arrays(matrixes)])
