#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - The while loop will iterate exactly n times


b) O(n^2) This is looping the same input twice with the for and while loops.


c) O(n log n) Recursion that is looping through based on the input.

## Exercise II

- n is the number of floors

- n contains f which equals the floor where the egg will break. 

- Find the length of n. 

- If the length is <= 1 then return n. Otherwise, split n in half by finding the middle floor (len(n)//2)

- Once we're on the middle floor we'll drop the egg and if it breaks then we'll go to the middle floor between the bottom 
floor and the floor we're on and start working our way down.

- If the egg does not break, go to the middle 
floor between the top floor and the floor we're on. 

- Continue until the egg is broke and f is found.

The time complexity will be O(log n) because we're cutting down the floors in halves every time we call the function