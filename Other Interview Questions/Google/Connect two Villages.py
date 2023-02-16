"""
Connect two Villages
There is a NXM matrix between two villages and the two villages can communicate if there is a series of tower which will connect both right and left edges of the matrix.

Initially the NXM matrix is empty, so each time we will call the buildTower() API which will return the row,col where a tower will be constructed.

Find the number of times the API has to be invoked so that the 2 villages can communicate.

The matrix which I have drawn is just for reference, we are just given the size of matrix i.e mXn

Eg:
n= 3,m= 3
Step 1 )

 |  * * * |   
 |  * * * |				
 |  * * * |
As the array is empty we will call the buildTower() API ans it returns 0,0

Step 2)

 |  T * * |   
 |  * * * |				
 |  * * * |
 
 We can see that the edges are not connected and we again call buildTower() and it returns 2,2
Step 3)

 |  T * * |   
 |  * * * |				
 |  * * T |
 
 We can see that the edges are not connected and we again call buildTower() and it returns 1,1
Step4)

 |  T * * |   
 |  * T * |				
 |  * * T |
 
 Now we see that the edges are connected i.e 0,0 -> 1,1 -> 2,2 so the villages can now communicate
 
Ans =3  as we had to call buildTower() 3 times before both villages can communicate
"""

