#Maanav Singh -- Challenge 1 (Calculus Based Solution)-- Panther Creek High School Data Science Club
import time
import math

#Use Taylor series to approximate Sin(X)
def taylor_sin(q,x):
    sigma = 0
    for n in range(0,q):
        sigma_temp = ((-1)**n  /  math.factorial(2*n+1)) * x**(2*n+1)
        sigma += sigma_temp
    return sigma

#Derivatice of Previous Taylor Series (Taylor Expansion of Cosine)
def taylor_cos(q,x):
    sigma = 0
    for n in range(0,q):
        sigma_temp = ((-1)**n  /  math.factorial(2*n)) * x**(2*n)
        sigma += sigma_temp
    return sigma

#take inital clock time (used to measure algorithm efficiency)
t0 = time.perf_counter()
x0 = 3
arrXn = [x0]

for i in range(0,50):
    xn = arrXn[-1]
    xnp1 = xn - (taylor_sin(round(100 + xn),xn) / taylor_cos(round(100 + xn),xn))
    arrXn.append(xnp1)
tf = time.perf_counter()

error = math.pi - arrXn[-1]
print("calculated pi: " + str(arrXn[-1]))
print("error: " + str(error))
print("cpu time: " + str(tf-t0))
