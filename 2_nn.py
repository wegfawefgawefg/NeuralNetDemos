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
def forwardGate( x, y ):
	return x * y 

#	calculate derivative
def calcDerivative( x, y, h ):
	output_0 = forwardGate( x 		, y )
	output_1 = forwardGate( x + h 	, y )

	derivative = ( output_1 - output_0 ) / h
	return derivative

#	calculate derivative on error
def calcErrorDerivative( x, y, h, target ):
	output_0 = forwardGate( x 		, y )
	error_0 = target - output_0

	output_1 = forwardGate( x + h 	, y )
	error_1 = target - output_1

	derivative = ( error_1 - error_0 ) / h
	return derivative

#	outputs a randomy number between -1.0 and 1.0
def randy():
	return ( random.random() * 2.0 ) - 1.0

'''	goal is to make output equal to a target
	
	-currently no complex backprop as only one neuron present
	-not sure if derivative is even right
	-why the fuck do the weights go up to infinity
'''

#	-	-	-	-	-	SETTINGS	-	-	-	-	-	#
target = 500.0
tries = 50
stepSize = 0.1
h = 0.0001

x = 1.0
y = 1.0

#	-	-	-	-	-	PREP	-	-	-	-	-	#
output = 0.0
error = 0.0
lastError = 0.0

output = forwardGate( x, y )
error = output - target
bestError = error

#	save initial value
initialY = y
initialX = x
initialOutput = output
initialError = error

#	-	-	-	-	-	PREP NUMPY 	-	-	-	-	-	#
xAxisValues = range( 0, tries + 1 )
yAxisValues = [ bestError ]

#	-	-	-	-	-	MAIN	-	-	-	-	-	#

for i in range( 0, tries ):

	#	calculate error
	output = forwardGate( x, y )
	error = output - target

	#	calculate derivative
	xDir = calcErrorDerivative( x, y, h, target )
	yDir = calcErrorDerivative( y, x, h, target )

	#	DEBUG
	print("( xDir, yDir ): " + str(xDir) + ", " + str(yDir) )

	#	tweak x and y in direction of derivative
	x = x + stepSize * -xDir * error
	y = y + stepSize * -yDir * error

	#	STATS:
	##	add current best error to yAxisValues for graphing
	yAxisValues.append(error)

#	-	-	-	-	-	DATA COLLECTING	-	-	-	-	-	#
#	save final value
finalY = y
finalX = x

output = forwardGate( finalX, finalY )
error = output - target

bestOutput = output
bestError = error


#	-	-	-	-	-	RESULTS	-	-	-	-	-	#
#	output state before changes
print( "x was " + str( initialX ) )
print( "y was " + str( initialY ) )
print( "output was: " + str( initialOutput ) )
print( "error was: " + str( initialError ) )
print("")

#	output state after changes
print( "x is " + str( finalX ) )
print( "y is " + str( finalY ) )
print( "output: " + str( bestOutput ) )
print( "error: " + str( bestError ) )

#	-	-	-	-	-	PLOT 	-	-	-	-	-	#

plt.plot( xAxisValues, yAxisValues )

plt.xlabel( 'tries' )
plt.ylabel( 'error' )
plt.title( 'Error Over Tries' )
plt.grid( True )
plt.show()