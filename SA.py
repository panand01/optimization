import numpy as np
import random
from math import exp,log10,log
import math

#defination of objective function 
def rosenbrock(x,y):
    return (a - x)**2 + b*(y - x**2)**2

#parameter value of Rosenbrock function
a = 1    
b = 100

#random point on the given function
x = random.randrange(-2,2,1)
y = random.randrange(-3,3,1)

m_1 = 0
m_2 = 0
energy_delta_plus = 0    

#initial temperature calculation
large_temperature = 500
test_value_previous = rosenbrock(x,y)

for p in np.arange(500):
        
    x_1 = x + round(random.uniform(-1,1),4)
    test_value_current = rosenbrock(x_1,y)
    delta_value = test_value_current - test_value_previous

    if delta_value < 0:
        m_1 = m_1 + 1
        test_value_previous = test_value_current
    else:        
        update = round(random.uniform(0,1),4) < exp(-(delta_value)/large_temperature)
        if update == True:
            m_2 = m_2 +1
            energy_delta_plus = energy_delta_plus + delta_value
            test_value_previous = test_value_current
        else:
            x_1 = x
    
    
    y_1 = y + round(random.uniform(-1,1),4)
    test_value_current = rosenbrock(x_1,y_1)
    delta_value = test_value_current -  test_value_previous
    
    if delta_value < 0:
        m_1 = m_1 + 1
        test_value_previous = test_value_current
    else:        
        update = round(random.uniform(0,1),4) < exp(-(delta_value)/large_temperature)
        if update == True:
            m_2 = m_2 +1
            energy_delta_plus = energy_delta_plus + delta_value
            test_value_previous = test_value_current
        else:
            y_1 = y

A =( ( ( m_1 + m_2 ) * 0.95 - m_1 ) / m_2 )       
        
initial_temperature = -energy_delta_plus/( log(A) * m_2 )


N = 460 #Number of iteration
n = 2 #Number of varibles of the objective function

x = random.randrange(-2,2,1)
y = random.randrange(-3,3,1)
test_value_previous = rosenbrock(x,y)
temperature_factor = np.arange(1,0.01,-0.001)

for i in np.arange(N):
    
    x_1 = x + round(random.uniform(-1,1),4)
    test_value_current = rosenbrock(x_1,y)
    delta_value = test_value_current - test_value_previous

    if delta_value < 0:
        test_value_previous = test_value_current
    else:        
        update = round(random.uniform(0,1),4) < exp(-(delta_value)/initial_temperature*(2*temperature_factor[i]))
        if update == True:
            test_value_previous = test_value_current
        else:
            x_1 = x
        
    y_1 = y + round(random.uniform(-1,1),4)
    test_value_current = rosenbrock(x_1,y_1)
    delta_value = test_value_current -  test_value_previous
    
    if delta_value < 0:
        test_value_previous = test_value_current
    else:        
        update = round(random.uniform(0,1),4) < exp(-(delta_value)/initial_temperature*(2*temperature_factor[i] + 1))
        if update == True:
            test_value_previous = test_value_current
        else:
            y_1 = y
    
print('minimum value of rosenbrock function is ' + str(rosenbrock(x_1,y_1)))
  
    
    
    
    
    
    
    
    
    