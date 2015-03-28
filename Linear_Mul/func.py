import header
import util

#functionality: constant times array
def A_x_Const(const,vector):
	i = 0
	#print(str(const) + "*",end="")
	util.print_array(vector)
	print("* " + str(const))
	print("---------")
	while (i+1) <= len(vector.values):
		vector.values[i] *= const
		i += 1
	util.print_array(vector)

#functionality: swap lines
def swap(L_one,L_Two,vector):
	util.print_array(vector)
	print("L"+str(L_one) + " <-> L" + str(L_Two))
	i = 0
	temp = 0
	while i < vector.m: #while a row has variables
		temp = vector.values[((L_one-1)*vector.m) + i]
		vector.values[((L_one-1)*vector.m) + i] = vector.values[((L_Two-1)*vector.m) + i]
		vector.values[((L_Two-1)*vector.m) + i] = temp
		i += 1
	util.print_array(vector)

#functionality: line times constant added to other line
def line_math(L_one,L_two,factor,vector):
	util.print_array(vector)
	print("("+str(factor)+"*L"+str(L_one)+")+L"+str(L_two)+" -> L"+str(L_two))
	i = 0
	while i < vector.m: #while row has variables
		if(vector.values[((L_two-1)*vector.m) + i] != 0):
			vector.values[((L_two-1)*vector.m) + i] += vector.values[((L_one-1)*vector.m) + i] * factor
		i += 1
	util.print_array(vector)

#functionality: line times constant
def line_factored(line,factor,vector):
	util.print_array(vector)
	print(str(factor)+"*L"+str(line)+"-> L"+str(line))
	i = 0
	while i < vector.m: #while row has variables
		if(vector.values[((line-1)*vector.m) + i] != 0):
			vector.values[((line-1)*vector.m) + i] *= factor
		i += 1
	util.print_array(vector)
