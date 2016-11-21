## Reference 
Whigham, Peter A., Caitlin A. Owen, and Stephen G. Macdonell. "A baseline model for software effort estimation." ACM Transactions on Software Engineering and Methodology (TOSEM) 24.3 (2015): 20.

## Introduction
The key objective of software effort estimation (SEE) has been to produce a robust, accurate predictive cost model. The new trend is new, often complex, modelling approaches for effort estimation, increasingly based on approaches from the field of machine learning in light of their apparent ability to better cope with the complex circumstances. Although multiple linear regression (MLR) has been used with mixed results in SEE and so has “fallen out of favour” in deference to other (machine learning) methods, we contend that with appropriate, automatic, data-driven transformations. Early methods in effort prediction included the constructive cost (COCOMO) model and function point analysis (FPA). 
Why do these discrepancies exist in results of newer methods?

- One obvious reason is that some datasets are more suited to some types of models than others, and therefore different datasets will produce different model performances.
- In addition, naively applying a linear regression model is often inappropriate due to the non-normality of the residuals and without considering transformations to the response and/or explanatory variables. 

## Baseline models
Characteristics:  
1. be simple to describe, implement, and interpret  
2. be deterministic in its outcomes  
3. be applicable to mixed qualitative and quantitative data  
4. offer some explanatory information regarding the prediction by representing generalised properties of the underlying data  
5. have no parameters within the modelling process that require tuning  
6. be publically available via a reference implementation and associated environment for execution  
7. generally be more accurate than a random guess or an estimate based purely on the distribution of the response variable.  

The ongoing use of a baseline model in the literature would give a single point of comparison, allowing a meaningful assessment of any new method against previous work. number of possibilities for models exist: a linear regression model, a simple decision tree, generalised linear models, extensions to linear and tree-based modelling etc. Their baseline model is presented as an implementation in the R programming environment,since R is a free, open-source environment with a standard core MLR implementation. The standard accuracy measure for this model used is RE, where RE∗ greater than 1 would be considered poor, independent of the dataset. 

## Experiment Discussions
The hybrid method was argued to be better than artificial neural networks, a standard classification and regression tree (CART) method, multiple linear regression, and stepwise regression. The paper's results would suggest that the ATLM is comparable with their hybrid method, even though the model is simple and has no parameters that require tuning from one dataset to another. 
The authors want to ensure that new effort estimation methods are assessed in such a way that a fair comparison against a known standard can occur.The issue of instability in software engineering datasets has been previously noted as an important aspect of modelling that must be considered. Comparison with other methods that also showed a significant difference would at least be able to argue some useful prediction performance. An alternative solution to this variation in performance is to perform many runs of cross-validation or training/test splits (many more than 30) to obtain a fair estimate of mean/variance in performance and to allow a meaningful statistical comparison.

## Conclusion
The proposed linear model with automatic transformations (ATLM) has been shown to satisfy the requirements for such a model, and should therefore be used as the baseline model when proposing and assessing new models of effort estimation.

More explanation and more testing to compare with previous models would be helpfull. Also, there is no future work given in the paper and there could surely be more improvements to the model.
