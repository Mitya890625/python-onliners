## Dependencies
import numpy as np
## Data: row is customer shopping basket
## row = [course 1, course 2, ebook 1, ebook 2]
## value 1 indicates that an item was bought.
basket = np.array([[0, 1, 1, 0],
[0, 0, 0, 1],
[1, 1, 0, 0],
[0, 1, 1, 1],
[1, 1, 1, 0],
[0, 1, 1, 0],
[1, 1, 0, 1],
[1, 1, 1, 1]])
## One-liner (broken down in two lines;)
copurchases = [(i,j,np.sum(basket[:,i] + basket[:,j] == 2))
               for i in range(4) for j in range(i+1,4)]
## Result
print(max(copurchases, key=lambda x:x[2]))