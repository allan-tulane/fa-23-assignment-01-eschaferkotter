

# CMPS 2200 Assignment 1

**Name:**Ethan Schaferkotter


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  Yes, 2^(n+1) is O(2^n) because since 2^(n+1) = 2*2^n, so it can be   reduced   to O(2^n). Since O(2^n) = O(2^n), therefore 2^(n+1) = O(2^n).
.  
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  No, because if you do the limit method, it equals to infinity, therefore 2^2^n grows significantly faster and is not = O(2^n).  
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  No, because using the limit method, it comes out to equal to infinity, meaning the numerator is growing quicker.
.  
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  Yes, because as seen in the last question, the limit as n->infinity for n^1.01/log^2n equals to infinity, therefore meaning that Ω(log^2n)
.  
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  The limit method limit n->infinity when sqrt(n)/(log(n)^3) equals to infinity, so no, it is not O(log(n)^3)
.  
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  Yes, because as seen in the last question, since it equals to infinity, therefore it is Ω(log(n)^3)


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  
  This functoion has a base case of x less than or equal to 1. If bigger than 1, it recursively creates a touple in accordance with the fibbonacci sequence and then merges the numbers in the touple, which in the fibonacci sequence is the sum of the two preceding numbers.
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  For a sequential implenetation, the work will be O(n) and the span will also be O(n), since they are dependent on the length of the array input.
.  
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  
.  
.  
.  
.  
.  
.  
.  

