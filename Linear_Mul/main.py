import header
import util
import func

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
		util.create(matrixes)
	elif op == '3':
		util.print_array(matrixes[util.display_arrays(matrixes)])
	elif op == '4':
		util.linear_math(matrixes)
#main program ends