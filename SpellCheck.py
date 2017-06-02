from sortedcontainers import SortedSet
def addToResult(value,result,dictionary): 		#if a valid value in dictionary add to the possibilities
	if(value in result):
		return
	else:
		if(value in dictionary):
			result.add(value)

def addLetter(query,letters,dictionary,result):		# generates valid combinations after addition of letters
	curlist = []
	for qry in query:
		for i in range(len(qry)+1):
			for c in letters:
				newstr = qry[:i] + c + qry[i:]
				addToResult(newstr,result,dictionary)
				curlist.append(newstr)
	return curlist

def spellcheck(dictionary,query):

	dictionary = [w.lower() for w in dictionary] # make case insensitve 
	query = query.lower() 
	letters = "abcdefghijklmnopqrstuvwxyz"	
	qlen = len(query) #length of the query
	dictlen = len(dictionary) #length of dictionary
	
	# set for fast search
	result = SortedSet()
	dictionary = SortedSet(dictionary)
	
	#check for swapping
	if (query in dictionary):
		result.add(query)            #if query is valid entry in dictionary

	for i in range(qlen):
		temp1 = list(query)
		temp2 = list(query)

		if(i<qlen-1):
			temp1[i],temp1[i+1] = temp1[i+1],temp1[i]
		if(i>0):
			temp2[i],temp2[i-1] = temp2[i-1],temp2[i]
		
		temp1 = ''.join(temp1);
		temp2 = ''.join(temp2);
		addToResult(temp1,result,dictionary)
		addToResult(temp2,result,dictionary)

	#check for extra character
	for i in range(qlen):
		newstr  = query[:i]+query[i+1:]
		addToResult(newstr,result,dictionary)

	#check for misspelt character
	for i in range(qlen):
		for j in range(26):
			newstr = query[:i] + letters[j] + query[i+1:]
			addToResult(newstr,result,dictionary)

	#check for additions
	qrylst = []
	qrylst.append(query)
	qrylst = addLetter(qrylst,letters,dictionary,result)# for one character addition
	qrylst = addLetter(qrylst,letters,dictionary,result)#	for second character additon
	return result

finans = spellcheck(["alsos","alsose","low","peter","perte","goosebumps","goosebump","eaelso"],"also")
for w in finans:
	print w,