# Lab 3 - Policy Search
 
The goal of Lab 3 is to write agents able to play *Nim* in which the player **taking the last object wins**.

* Task3.1: An agent using fixed rules based on *nim-sum* (i.e., an *expert system*)
* Task3.2: An agent using evolved rules
* Task3.3: An agent using minmax
* Task3.4: An agent using reinforcement learning

## Task 3.1
I have approached this problem trying to ignore all the informations about *nim-sum* that have been presented during lectures, so I defined some fixed rules and evaluate their performances against a **random player**. 

I have defined some very simple fixed rules, in order to see what are their performances:

* Pick the maximum possible number of the highest row
* Pick the minimum possible number of the highest row
* Pick an odd number of elements
* Pick an even number of elements (if possible)

Then, I tried to define a more complex fixed rule, in which I count the active rows number and we decide what to do. I thought that could be better for us to leave to the opponent an even number of active rows, so:
* if the active rows number is even, we pick the minimum possible number of elements of the highest row
* if the active rows number is odd, we pick the maximum possible number of elements of the highest row, so that after our action, the active rows number is even again

I have evaluated my fixed rules empirically, playing `NUM_MATCHES = 100` with `NIM_SIZE = 11` against a random player and counting the win rate as `won / NUM_MATCHES`

## Task 3.2
For performing Task 3.2 I have defined three different strategies, which depends by a parameter `p` that acts as a probability. I have tried to evolve my rules using an evolutionary algorithm on this parameter, in order to obtain better results.

This are in summary the three strategies:
* the first strategy consists in applying `count_rows_and_choose` or not with probability p
* the second strategy consists in picking an **odd** number of elements, respect to picking an **even** number of elements, depending on the probability p
* the third strategy consists in picking the **minimum** number of elements from a row, respect to picking the **maximum** number of elements from a row, depending on the probability p

In my genetic algorithm I have set these parameters: `POPULATION_SIZE = 100`, `NUM_GENERATIONS = 101`, `OFFSPRING_SIZE = 30`, `MUT_RATE = 0.5`. 
Each genome is characterized by the value p, and the fitness function, that corresponds to the win rate associated to that specific rule, using that specific probability p.

The crossover operation consists in the arithmetic mean of the value p of the two chosen genomes.

The mutation operation consists in changing the value of p of a genome. In order to explore differents solutions, the mutation consists in assigning a new random value to the genome, or otherwise in changing a little the previous value of p, increasing it by 0.1.


