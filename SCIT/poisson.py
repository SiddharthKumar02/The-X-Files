import numpy as np
import matplotlib.pyplot as plt
for i in range(3):
    mu=10
    s = np.random.poisson(mu,1000)
    lol=plt.hist(s,14,density=True)
    plt.ylabel('Frequency')
    plt.xlabel('Data')
    plt.title('Histogram for Random Poisson Distirbution')
    plt.savefig('Graphs/Poisson/Poisson'+str(i)+'.png')
    plt.show()
    
