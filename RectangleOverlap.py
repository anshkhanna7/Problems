def checkRectangle():
	x1,y1,x2,y2 = [int(x) for x in raw_input("Enter Coordinates of point 1: ").split()]
	a1,b1,a2,b2 = [int(x) for x in raw_input("Enter Coordinates of point 2: ").split()]

	maxA = max(a1,a2)
	minA = min(a1,a2)
	maxB = max(b1,b2)
	minB = min(b1,b2) 
	
	maxX = max(x1,x2)
	minX = min(x1,x2)
	maxY = max(y1,y2)
	minY = min(y1,y2)									

	if ((maxX<minA or minX>maxA) or (maxY<minB or minY>maxB)):               #checks for overlap along x and y axis
		return False
	else:
		return True

if(checkRectangle()):
	print "Rectangles Overlap"
else:
	print "No Overlap"