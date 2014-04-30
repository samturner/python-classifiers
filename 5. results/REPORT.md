#COMP3308 Assignment 1 Report

## 1.Aim

The purpose of this study was to build classifiers that where able to predict whether a person has diabetes or not based on a number of attributes collected from the publicly available Pima Indians Diabetes database.

This is important for a number of medical reasons. Primarily, it is useful to be able to predict whether or not someone has diabetes without having to do invasive testing.


## 2. Data

### Data Set Used

The data set used was the Pima Indians Diabetes data that is publicly available from the UCI Machine Learning Repository at http://archive.ics.uci.edu/ml/. In its raw state it contains 768 instances described with 8 numeric attributes. Where each attribute is correlates to a patients personal characteristics and test measurements and each patient is of Pima Indian Heritage.

**The attributes are as follows:**

   * Number of times pregnant
   * Plasma glucose concentration a 2 hours in an oral glucose tolerance test
   * Diastolic blood pressure (mm Hg)
   * Triceps skin fold thickness (mm)
   * 2-Hour serum insulin (mu U/ml)
   * Body mass index (weight in kg/(height in m)^2)
   * Diabetes pedigree function
   * Age (years)
   * Class variable (0 or 1)


### Data Preparation

To preprocess the data, a number of steps where taken:

* Add headers for each column at the top of the file.
* Change the class names from `0` and `1` to `class0` and `class1` respectively.
* Remove instances where at least one attribute is invalid. For more explanation of why certain fields where chosen and how we decided to deal with them see *Appendix 1*.
* The attributes have then been normalised so all values are in the range $$$0 ≤ x ≤ 1$$$

### Attribute Selection

The Correlation Based Feature Selection (CFS) method was used to generate a CSV with a reduced number of attributes. CFS operates under the assumption that there is redundant or irrelevant fields in the data. Kohavi and John formalise the definition:

**Definition:** A feature $$$V_i$$$ is said to be relevant if there exists some $$$v_i$$$ and $$$c$$$ for which $$$p(V_i = v_i) > 0$$$ such that:

$$
p(C =c|V_i =v_i) \neq p(C =c)
$$

The simplest way to select a feature subset is to test each possible subset of values to find the one that minimises the error rate, but obviously, this is an exhaustive search of the space and is not optimal. There are three main categories of feature selection algorithms: *wrappers*, *filters* and *embedded* methods where the method chosen is heavily influenced by the metric used.

##### Wrapper Algorithms

##### Filter Algorithms

##### Embedded Algorithms 


## 3. Results and Discussion

## 4. Conclusions

## 5. Reflection

## 6. Bibliography

* R. Kohavi and G. John. Wrappers for feature subset selection. Artificial Intelligence, special issue on relevance, 97(1–2):273–324, 1996.