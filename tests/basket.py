class Basket():
	pass

def basket(*argv):	
	books=[x for x in argv]
	cost1=0
	zerocounter=0
	sumbooks=sum(books)
	while sumbooks > 0:
		# How many zeros
		for i in range(len(books)):
			 if books[i] == 0:
			 	zerocounter+=1
	    #Diffrent discountes
		if zerocounter==0:
		 	cost1 += (int(5*8)*0.75)
		elif zerocounter==1:
			cost1+= (int(4*8)*0.8)
		elif zerocounter==2:
			cost1+=(int(3*8)*0.90)
		elif zerocounter==3:
			cost1+=(int(2*8)*0.95)
		else:
			cost1+=(8)
		
		#Decrement if not zero
		for i in range(len(books)):
			if books[i] != 0:
				books[i]-=1
		zerocounter=0
		sumbooks=sum(books)
	return print(cost1)
basket(0,0,0,0,1)

