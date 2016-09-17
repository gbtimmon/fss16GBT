## Reference
Dejaeger, Karel, et al. "Data mining techniques for software effort estimation: a comparative study." IEEE Transactions on Software Engineering 38.2 (2012): 375-397.

## Keywords
a) Data Mining: process of analyzing data from different perspectives and summarizing it into useful information.

b) Software Effort Estimation: Process of predicting the time and effort required to accomplish development or maintenance tasks.

c) Regression: Test if previously developed and tested software still performs correctly even after it was changed or interfaced with other software. 

## Introduction
Resourse planning for software companies includes computing power and personnel effort. Estimates of effort can help management improve planning of personnel. In this paper, 13 techniques are investigated, including tree/rule-based models, linear models, nonlinear models, and a lazy learning-based approach. Effort estimation is done by taking in details of the new account and then comparing it to past data using relevant metrics. New data intensive models are supercedeing older formal or expert based models. 

## Research of Techniques
The paper has researched various machine learning approaches to effort estimation, along with statistical information. A table in the paper shows a number of researches done over the years, but points out that it is difficult to reproduce and verify.
- Ordinary least squares regression: Ordinary Least Squares regression. It is a multiple regression with a linear model. 
- OLS regression with log transformation: This takes into account the skewness in data. Normal distributions have a zero skewness and so it uses log transformations so the data follows a more normal distribution.
- OLS regression with Box Cox (BC) transformation: Box Cox transformation corrects for discontinuities in data.It is an alternative to log transformations for the same goal.
- Robust regression: RoR is less vulnerable to the existence of outliers in the data.RoR is an application of Iteratively Reweighted
Least Squares (IRLS) regression. 
- Ridge regression.RiR addresses a potential problem with OLS in case of highly correlated attributes. This hasnt been commonly applied to effort estimation. 
- Least median squares regression: LMS is an alternative to robust regression with a breakdown point. It can be inefficient in some situations.
- MARS: Multivariate Adaptive Regression Splines. MARS is a nonlinear and nonparametric regression. It is a good prediction model for effort estimations and is commonly used in other domains. The model is constructed in two stages- in the first stage(forward pass), MARS starts from an empty model and constructs a large model by adding hinge functions tooverfit the data set. In the second stage, the algorithm removes the hinge functions associated with the smallest increase in terms of the Generalized Cross Validation (GCV) criterion
- CART: CART constructs a binary tree by recursively splitting the data set until a stopping criterion is met. It has been used for effort estimation with good results.
- Model tree: M5 is an extension for CART. The use of a model tree algorithm should allow for a more concise representation and higher accuracy compared to CART.
- Multilayered perceptron neural network: Neural networks are a nonlinear modeling technique inspired by the functioning of the human brain. in this paper, an MLP with one hidden layer was used. 
- Radial basis function networks: Radial Basis Function Networks are a special case of artificial neural networks. It makes use of Euclidean distance between neurons. This technique has been used for estimation as well.
- Case-based reasoning: it searches for the most similar cases and the effort is derived based on these retrieved cases. This technique is commonly used in software effort estimation.

## The data
Nine data sets from companies of different industrial sectors are used.
The data sets typically contain a unique set of attributes:
- Size attributes: size of project
- Environment information
- Project data: purpose and type of project
- Development related variables
Data is then preprocessed and setup according to the requirements of the techniques.The paper also discusses input selection and evaluation criterion. 

##Technique results
Ordinary least squares regression with logarithmic transformation (Log + OLS) is the overall best performing technique. However, a number of other techniques including least median squares regression, ordinary least squares regression with Box Cox transformation, and CART, are close as well. It also shows that COCOMO, an older model also performs as well as log + OLS on some data sets.

##Conclusion
These results also indicate that data mining techniques can make a valuable contribution to the set of software effort estimation techniques, but should not replace expert judgment. Instead, both approaches should be seen as complements. Some error is expected in the effort, since it is a continuous attribute, but a very far value( for eg. 25% error) cannot be accepted. 
Also, choosing thr right method makes a difference in performance. It notes that a simple regression technique can be well-suited for effort estimation.

## Improvements
The paper discusses effectiveness of various techniques using their results. More explanation could be given on how they arrived at these results, rather than a general explanation of the techniques.
