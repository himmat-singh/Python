def fib(n): #define Fibonacci series upto n
	"""Print a Fibonacci series upto n"""
	a,b=0,1
	while a<n:
		'''if(b<n):
			print(a,end=', ')
		else:
			print(a,end=' ')
			'''
		
		print(a)
			
		a,b=b,a+b
		


#Now call the Fibonacci function defined above
fib(1000)
