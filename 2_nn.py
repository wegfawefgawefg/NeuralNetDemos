import random
import matplotlib.pyplot as plt 
import numpy

'''	1_nn.py
	simple neural net
'''
'''	-has primitive backprop
	-weights deviate in direction of derivative
	-productivity is determined by difference between forward output and target
'''

#	forward propogation
def forwardGate( inp, weight ):
	return ( inp * weight ) 

#	calculate derivative
def calcDerivative( x, y, h ):
	output_0 = forwardGate( x 		, y )
	output_1 = forwardGate( x + h 	, y )

	derivative = ( output_1 - output_0 ) / h
	return derivative

#	calculate derivative on error
def calcErrorDerivative( inp, weight, h, target ):
	output_0 = forwardGate( inp 	, weight 	)
	error_0 = target - output_0 

	output_1 = forwardGate( inp 	, weight + h )
	error_1 = target - output_1

	derivative = ( error_1 - error_0 ) / h
	return derivative


#	outputs a randomy number between -1.0 and 1.0
def randy():
	return ( random.random() * 2.0 ) - 1.0

#	returns sign of a number
def sign( a ):
	if a >= 0:
		return 1
	if a < 0:
		return -1

'''	goal is to make output equal to a target
	
	-currently no complex backprop as only one neuron present
	-not sure if derivative is even right
	-doesnt like negative targets
		|-suspect this has to do with an incorrect sign somewhere
'''

#	-	-	-	-	-	SETTINGS	-	-	-	-	-	#
target = random.random() * 100.0
tries = 100
stepSize = 0.1
h = 0.0001

inp = 2.0
weight = random.random()

#	-	-	-	-	-	PREP	-	-	-	-	-	#
output = 0.0
error = 0.0

output = forwardGate( inp, weight )
error = target - output

#	save initial value
initialWeight = weight
initialOutput = output
initialError = error

#	-	-	-	-	-	PREP NUMPY 	-	-	-	-	-	#
xAxisValues = range( 0, tries + 1 )
yAxisValues = [ initialError ]

#	-	-	-	-	-	MAIN	-	-	-	-	-	#

for i in range( 0, tries ):

	#	calculate error
	output = forwardGate( inp, weight )
	error = target - output

	#	calculate derivative
	wDir = calcErrorDerivative( inp, weight, h, target )

	#	DEBUG
	#print("wDir:\t" + "%.2f" % wDir + "\tError:\t" + "%.2f" % error )

	#	tweak x and y in direction of derivative
	weight = weight + ( error / -wDir ) * stepSize

	#	STATS:
	##	add current best error to yAxisValues for graphing
	yAxisValues.append( error )

#	-	-	-	-	-	DATA COLLECTING	-	-	-	-	-	#
#	save final value
finalWeight = weight

output = forwardGate( inp, finalWeight )
error = target - output

finalOutput = output
finalError = error


#	-	-	-	-	-	RESULTS	-	-	-	-	-	#
print( "#	-	-	-	RESULTS	-	-	-	#" )

#	output state before changes
print( "weight 	was: \t" 	+ str( initialWeight 	) )
print( "output 	was: \t" 	+ str( initialOutput 	) )
print( "target 	was: \t" 	+ str( target 	 		) )
print( "error 	was: \t" 	+ str( initialError  	) )
print("")

#	output state after changes
print( "weight 	is: \t" 	+ str( finalWeight 	) )
print( "output 	is: \t" 	+ str( finalOutput 	) )
print( "target 	is: \t" 	+ str( target 		) )
print( "error 	is: \t"		+ str( finalError 	) )

#	-	-	-	-	-	PLOT 	-	-	-	-	-	#

plt.plot( xAxisValues, yAxisValues )

plt.xlabel( 'tries' )
plt.ylabel( 'error' )
plt.title( 'Error Over Tries' )
plt.grid( True )
plt.show()