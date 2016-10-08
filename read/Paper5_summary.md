## Reference
Oliveira, Adriano LI, et al. "GA-based method for feature selection and parameters optimization for machine learning regression applied to software effort estimation." information and Software Technology 52.11 (2010): 1155-1166.

## Introduction
We have been studying effort estimation, its methods and application of data mining techniques to the same. This paper talks about feature selection and parameter optimizations and how it affects the results. The paper proposes to use Genetic Algorithm (GA) to improve prediction performance.
Machine learning techniques use data from past projects to build a regression model that is subsequently employed to predict the effort of new software projects. Two factors substantially influence the accuracy and computation time of machine learning techniques: 
(1) the choice of the input feature subset
(2) the choice of the parameters values of machine learning techniques

## Regression methods
- Support vector regression
- Multi-layer Perceptron (MLP) neural network
- Model trees

## Genetic algorithm
When GA is used for the resolution of real-world problems, a population comprised of a random set of individuals is generated
(each individual of the population, called chromosome, normally corresponds to a possible solution of the problem). The population
is evaluated during the evolution process. For each individual a rating is given, reflecting the degree of adaptation of the individual to the environment.
### Genenic operators
- Selection operator: Select parents increase the probability to reproduce members of the population that have good values of the objective function.
- Crossover operator: recombination of characteristics of parents during reproductions, so next generation can inherit them.
- Mutation operator: applied to the individuals with a probability given for mutation rate.

### GA based feature selection and parameters optimization
- Chromosome design: The chromosome is divided into two parts- parameters of the technique and the inpur features to be sleected. The minimum and maximum value of each parameter is decided by the user. In the chromosome, the description of feature representation is: the bit with value ‘1’ indicates that the feature is not removed; ‘0’ indicates that the input feature must be removed.

- Fitness function: The two measures discuessed in the paper are the Mean Magnitude of Relative Error (MMRE) and the PRED.In this paper, they use these to select the fitness function for the COCOMO data set (which aims only to find the smaller MMRE).

## Experiment
The paper experiments over 6 data sets, with software background. They use PRED, MMRE, Absolute resolutions and removed features while comparing the techniques for each data set. 

## Conclusion
In all the data sets, our method achieved the best performance in terms of PRED(25). 
Our simulations have shown that the
GA-based method was able to improve performance of the three machine learning techniques considered in the problem of software effort estimation. For future work, they propose to use particle swarm optimization. The want to see if PSO works better than GAin many classification problems.


I would like to know more about the six data sets they were comparing and why they got slightly different conclusions for each.
