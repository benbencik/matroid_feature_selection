# Matroid Feature Selection

Def: Independance set I nad X je:
- I je neprázdne
- i z I a tak potom aj každá podmnožina z i je z I

Def: Maximálny nezávislý set je báza

Def: Veľkosť bázy je rank matroidu

That is, suppose that your matroid  $M = (X, \mathbb{I})$ has a nonnegative real number $w(x)$ associated with each $x \in X$. And suppose we had a black-box function to determine if a given set $S \in X$ is independent. Then the greedy algorithm maintains a set $B$, and at every step adds a minimum weight element that maintains the independence of $B$. The greedy algorithm performs perfectly if and only if the problem is a matroid!

### Resources and articles

[When Greedy Algorithms are Perfect: the Matroid](https://jeremykun.com/2014/08/26/when-greedy-algorithms-are-perfect-the-matroid/)

[What is a Matroid?](https://www.math.lsu.edu/~oxley/matroid_intro_summ.pdf)