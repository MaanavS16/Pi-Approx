#Maanav Singh -- Challenge 1 (Non-Calculus Based Solution) -- Panther Creek High School Data Science Club
import math
#leibniz Algorithm
#adjust sensitivity of convergence detectance (Increase to make more sensitive)
q = 12

sigma = 0
n = 0
pi_last = 0

while True:
    sigma_temp = (-1/(3 + 4*n)) + (1 / (5 + 4*n))
    sigma += sigma_temp
    pi_approx = 4*(1+sigma)

    #used to detect convergence
    if round(pi_approx, q) == round(pi_last, q):
        break
    print(n, sigma, pi_approx)
    n += 1
    pi_last = pi_approx


error = math.pi - pi_approx
print("after " + str(n) + " iterations with the Leibniz approximation algorithm the error was " + str(error))
print("convergence detectance set to q=" + str(q) + " digits (derivatice must be less than 10^-q)")
