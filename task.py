#Include two functions to calculate the sum and product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
#Examples:
#
# matrix_1 = Matrix(4,5,6,7)
# matrix_2 = Matrix(2,2,2,1)
#
# matrix_3 = matrix_2.add(matrix_1)
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#(If you want you can expand implementation to NxN matrix.)
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.
import math

class Matrix:
	def __init__(self, *val):
		self.num = int(math.sqrt(val.__len__()))
		self.arr = []

		for i in range( self.num ):
			temp_arr = []

			for j in range( self.num ):
				temp_arr.append(val[i*self.num + j])

			self.arr.append(temp_arr)

	def __str__(self):
		return "{}".format(self.arr)

	def add(self, matrix_2):
		new_arr = []
		for i in range( self.arr.__len__() ):
			temp_arr = []
			
			for j in range( self.arr[0].__len__() ):
				temp_arr.append( self.arr[i][j] + matrix_2.arr[i][j] )
			new_arr.append(temp_arr)

		return new_arr

		

def main():
	matrix_1 = Matrix(4,5,6,7)
	matrix_2 = Matrix(2,2,2,1)
	matrix_4 = Matrix(1,1,1,2,2,2,3,3,3)

	matrix_3 = matrix_2.add(matrix_1)

	print(matrix_1)
	print(matrix_2)
	print(matrix_3)
	print(matrix_4)
if __name__ == "__main__":
	main()