# Matroid Feature Selection

## Definitions

**Matroid is in terms of independance a pair** $(E, \mathcal{I})$ where $E$ is a finite set (called the *ground set*) and $\mathcal{I}$ is a family of subsets of $E$ (called the *independent sets*) with the following properties:
1. The empty set in independant: $\emptyset \in \mathcal{I}$
2. Every subset of an independent set is independent: $\forall A' \subset A \subset E$ if $A \in \mathcal{I}$ then $A' \in \mathcal{I}$
3. If $A, B \in \mathcal{I}$ and $|A| > |B|$ then there exists an element $x \in A \setminus B$ such that $B \cup \{x\} \in \mathcal{I}$

**Matroid in terms of rank function** is a pair $(E, r)$ where $E$ is a finite set (called the *ground set*) and $r: 2^E \rightarrow \mathbb{N}$ is a function (called the *rank function*) with the following properties:
1. $r(\emptyset) = 0$
2. For all $A \subset E$ we have $r(A) \leq |A|$
3. For all $A, B \subset E$ it hold: $r(A \cup B) + r(A \cap B) \leq r(A) + r(B)$ which says that is, the rank is a submodular function.
4. For any set $A$ and element $x$ we have: $r(A) \leq r(A \cup \{x\}) \leq r(A) +1$

**Submodular function** is a set function $f: 2^E \rightarrow \mathbb{R}$ is submodular if for all $A, B \subset E$ we have:
1. $\forall X, Y \in E: X \subset Y, \forall x \in E \setminus Y$ following holds: $f(X \cup \{x\}) - f(X) \geq f(Y \cup \{x\}) - f(Y)$
2. $\forall X, Y \in E: X \subset Y$ following holds: $f(X \cup Y) + f(X \cap Y) \leq f(X) + f(Y)$
3. $\forall X \in E, \forall x_1, x_2 \in E \setminus X$ such that $x_1 \neq x_2$ we have: $f(X \cup \{x_1\}) + f(X \cup \{x_2\}) \geq f(X \cup \{x_1, x_2\}) + f(X)$

**Greedy algorithm** is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage. In many cases, a greedy strategy does not in general produce an optimal solution.

## Feature selection

Is a common technique in data science that aims to select a subset of features that are most relevant to the task at hand. The goal of feature selection is to reduce the number of features in the dataset, thus reducing the complexity of the model and improving its performance. We would like to find an optimal subset, however there are many possible subsets of features, and it is computationally infeasible to evaluate all of them. Therefore, we need to find a way to select a subset of features that is close to optimal, but can be computed efficiently. And that is where matroids come to help. If we can phrase the problem we’re trying to solve as a matroid, then the greedy algorithm is guaranteed to be optimal.

Feature is usually performed in one of two ways:
1. **Top-k feature selection** - select the top-k features that are most relevant to the task at hand.
2. **Threshold feature selection** - select all features that are above a certain threshold of relevance.

Setting the optimal $k$ or the thershold is also challenging and heavily depends on the task at dataset we are given. I this project we would work with the famous housding dataset with where the task is to predict price of a house. We will evaluate the features using mutal information which is also known as information gain. The mutual information between two random variables is a non-negative value, which measures the dependency between the variables. It is equal to zero if and only if two random variables are independent, and higher values mean higher dependency. More over mutal information is a submodular function.


## In Context of Matroids 

There is a strong connection between matroids and submodular functions, which arises from the fact that matroids can be characterized by a set of independent sets that satisfy the submodularity property. 

This connection between matroids and submodular functions has important implications for optimization, since it allows us to leverage the properties of matroids to design efficient algorithms for submodular function optimization. In particular, the matroid structure provides a natural way to define a greedy algorithm for maximizing a submodular function subject to a matroid constraint.

<!-- That is, suppose that your matroid  $M = (X, \mathbb{I})$ has a nonnegative real number $w(x)$ associated with each $x \in X$. And suppose we had a black-box function to determine if a given set $S \in X$ is independent. Then the greedy algorithm maintains a set $B$, and at every step adds a minimum weight element that maintains the independence of $B$. The greedy algorithm performs perfectly if and only if the problem is a matroid!


In the context of feature selection, we can define the independence structure of a set of features as follows: Let S be the set of all features in our dataset, and let I be a family of subsets of S such that a subset A of S is independent if and only if the features in A are not redundant or unnecessary for the task at hand. In other words, A is independent if removing any feature from A would result in a significant decrease in the performance of the model.

With this definition of independence, we can use a greedy algorithm over matroids to select the most relevant features for our task, ensuring that the selected features are not redundant or unnecessary. -->

### Resources and articles

[Maximizing Submodular Functions under Matroid Constraints by Evolutionary Algorithms](https://cs.adelaide.edu.au/~frank/papers/Submodular.pdf)

[When Greedy Algorithms are Perfect: the Matroid](https://jeremykun.com/2014/08/26/when-greedy-algorithms-are-perfect-the-matroid/)

[What is a Matroid?](https://www.math.lsu.edu/~oxley/matroid_intro_summ.pdf)

