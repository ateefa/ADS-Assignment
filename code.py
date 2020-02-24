# ADS Assignment 
# NAME - ATEEFA ATEEQUE
# ROll - 13
# RANDOMIZATION ALGORITHMS
# PRIMALITY TEST
# Short description of my code -----
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 	The code consistes of three different (Algorithms) test in increasing order of their realiabilty 
# 	as random algorithms for primality test depends on probability and they are not always   
# 	equally realiable in their outputs.
# 	fermat being the least realiable among these.
# 	3 Switch cases 1)Fermat   2)Miller-rabin  3)Solovay-Strassen
# 	Chose any three of them and see how they differ in their output. 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
when we dont use randomization the complexity we have is n in very ordinary methode else it can be reduced 
to root(n) using seive logic
lets see how that works on psedo code
--------------------------------
with complexity O(n):
    for (int i=2; i<n; i++) 
        if (n%i == 0) 
            return false; 
    return true; 
--------------------------------
using randomised algorithm we can reduce time complexity to a very great extent 
i.e to constant O(1)
lets check out how....		
'''



import random

# FERMAT ALGORITHM
# if a^n-1%n==1 n is probabily prime
# if a is any of the factor of n then it always gives right result
# this test is niether sure abt composite nor abt prime.
# O(k Log n)

def fermat(n):
	iter=30
	while (iter>0): 
		a = random.randint(2,n-2)
		if pow(a,n-1,n)!=1:
			return False
		iter-=1
	return True


if (fermat(561)):
	print("Is probabily Prime") 
else:  
	print("Not Prime")
# ----------------------------------------------------------------------
'''
# MILLER-RABIN
# this algorith is better than fermat algorithm
# s be the maximal power of 2 dividing p-1,
# so that p-1 = 2^s*d, such that d is odd. 
# Then for any 1 <= n <= p-1, either
# n^d = 1 (mod p)
#   or
# n^(2^(j)*d) = -1 (mod p) for some integer j with D: {0 <= j < s}
# if returns true -> probabily prime else composite
#  O(k log^3n)
'''
def miller(d, n):
	a = random.randint(1, n - 2);
	x = pow(a, d, n);
	if (x == 1 or x == n - 1): 
		return True
	while (d != n - 1):
		x = (x * x) % n
		d *= 2
		if (x == 1):
			return False
		if (x == n - 1):
			return True
	return False

def checkForPrime(n):
	if (n <= 1 or n == 4):
		return False
	if (n <= 3):
		return True
	d = n - 1
	while (d % 2 == 0):
		d //= 2
	# such that d is odd.
	for i in range(30):
		if (miller(d, n) == False):
			return False
	return True;	 			


if (checkForPrime(1729)):
	print("Is probabily prime") 
else:  
	print("Not Prime")

# ----------------------------------------------------------------------
# In most simple words this algorithm can be fully condenced down by saying
# if n is prime then its jacobi and legendre symbols will be equal else its composite
# (a/p) = a^(^(^p^-^1^)^/^2^)%p   Condition (i)
# legendre
# 	  	= 0    if a%p = 0
# (a/p) = 1    if there exists an integer k such that k^2 = a ( mod p )
#       = -1   otherwise.
# jacobi
# (a/n) = ((a/p1)^k^1) * ((a/p2)^k^2) * ..... * ((a/pn)^k^n)
# how we can calculate jacobi then ??
# 	if a>n then
# 		return ((a mod n)/n)
# 	else
# 		return (-1)^((a-1)/2)((n-1)/2)(a/n)	
# O(k·log^3 n)
def jcb(a,n):
		j = 1											
		while (a != 0):
			while (a%2==0):							
				j = j * pow(-1,(n*n-1)/8)			 
				a = a/2
			
			if not ( (a-3)%4 or (n-3)%4 ):			
				j = -j
			a,n = n,a								
			a = a % n								
		return j
def solovay_strassen(n, k=10):
	if n == 2 or n == 3:
		return True
	if not n & 1:
		return False
	for i in range(k):
		a = random.randrange(2, n - 1)				
		x = jcb(a, n)							
		
		y = pow(a, int((n - 1) / 2), n)			    
		if y != 1 and y != 0:						
			y = -1
			
		if (x == 0) or (y != x):					
			return False
	return True         

		
if(solovay_strassen(7623302,10)):
	print ('Is Prime')
else:
	print ('Not Prime')
