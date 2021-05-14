def pal(palindrome):
	pal = list(palindrome)
	passL= int(len(pal)/2)
	y=0
	
	for x in range(passL):
		if pal[x]==pal[len(pal)-x-1]:
			y+=1
		else:
			y=0

	if y==passL:
		return 0

	return 1

#end of def
