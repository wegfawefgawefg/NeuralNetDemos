import random

'''	1_nn.py
	simple neural net
'''
'''	-has no backprop
	-weights randomly deviate
	-productive deviates are kept
	-counterproductive deviations are discarded
	-productivity is determined by difference between forward output and target
'''

#	forward propogation
def forwardGate( x, y ):
	return x * y 

#	outputs a randomy number between -1.0 and 1.0
def randy():
	return ( random.random() * 2.0 ) - 1.0

'''	goal is to make output equal to a target
'''
'''	randomly tweak x and y
	do it by some small amount between positive and negative 1.0
'''
	#	run gate forward

	#	if output is closer to goal than current best output:
		#	make x = tweaked x
		#	make y = tweaked y
	#	if not, then try again

#	-	-	-	-	-	SETTINGS	-	-	-	-	-	#
target = 500.0
tries = 5000
tweakMag = 0.1

x = 0.0
y = 0.0

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

#	-	-	-	-	-	MAIN	-	-	-	-	-	#
testX = 0.0
testY = 0.0

for i in range( 0, tries ):
	#	tweak x and y by small amounts
	testX = x + ( tweakMag * randy() )
	testY = y + ( tweakMag * randy() )

	#	calculate error
	output = forwardGate( testX, testY )
	error = output - target

	#	if error this try is less than best error, push testX and testY to real x and y
	if abs( error ) < abs( bestError ):
		bestError = error
		x = testX
		y = testY

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