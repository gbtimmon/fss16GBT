## Reference
Menzies, Tim, et al. "Local versus global lessons for defect prediction and effort estimation." IEEE Transactions on Software Engineering 39.6 (2013): 822-834.

## Index Terms: 
- Data mining -  Data mining is the process of analyzing data and summarizing it into useful information. Data mining software is one of a number of analytical tools for analyzing data. 
- Clustering - The process of organizing objects into groups whose members are similar in some way. It is an important unspervised learning problem.
- Defect Prediction - Software development effort estimation is predicting the most realistic amount of effort required to develop or maintain software.

## Introduction
This paper addresses the question of what is best way to reason with data. It is focused on the source of the data and implicitly the applicability of the lessons derived by the models for defect prediction or effort estimation. 
Two compareisons for how to reason with data are global lessons vs local lessons.

- Global lessons: learnt from data from multiple sources that can generate rules that apply to any context. Available from existing data.
- Local lessons: learnt from within one source, useful in a particular context. Available by mining current data and infering.


## Learner
The paper's algorithms are agnostic with respect to the semantics of their input data, which means that we use the same algorithms for defect data and effort data. Contrast sets list the differences between classes. To find a contrast set, the paper looks for an attribute where: 
(1) all the values from one class are similar but
(2) those values differ in different classes.
A major advantage of contrast set learning for software engineering is that it generates very succinct rules.
Their clustering algorithm, named WHERE, assumes that the dimensions of most interest are the dimensions of greatest variability. This assumption is shared by other researchers such as those using feature weighting based on variance or principal component analysis (PCA).
They use the the WHICH contrast rule learner. WHICH learns rules of the form if Rx then (change = "1/"0 & support) . Here, Rx is a treatment containing a set of attribute value pairs av; "0 is the median score for instances in the untreated population.WHICH builds these rules by looping over attribute value combinations, combining those that look most promising.

## Experiments
There are experiments that compare the results of defect prediction and effort estimation obtained from learning rules from global data, local data, and clusters, respectively. 
### Experiment 1: Global rules are suboptimal
They found that the rules generated from cluster lessons were better and different than those learned globally. The rule learning method is effective: the median and stability values of the above are small percentages of original data. The data obtained is not supportive of the claim that global lessons are the best for defect prediction or effort estimation.

### Experiment 2 : local rules are suboptimal
Based on an analysis of rules learned from neighboring clusters in different sources, they conclude that it is sub-optimal to learn purely local rules from the clusters within the same source as the test data. This is the standard overfitting-avoidance result.

## Conclusion
The results of the paper strongly endorse the creation of the local lessons team. However, that team should apply automatic algorithms to build clusters from all available data. It concludes that basic global rules are not sufficient for such complex entities, and neither is it sufficient to characterize the data into local contexts. Future work includes improving the WHICH and WHERE, as well as exploring multi-goal optimization.




