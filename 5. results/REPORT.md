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

The Correlation Based Feature Selection (CFS) method was used to generate a CSV with a reduced number of attributes.

## 3. Results and Discussion

## 4. Conclusions

## 5. Reflection