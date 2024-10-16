# Handling-Skewness-of-the-Data
![image](https://user-images.githubusercontent.com/92606737/222619099-38033234-1c5a-4bae-9587-0c3296644206.png)

# What is Skewness of the data?
Skewness is a measure of the asymmetry of a distribution. A distribution is asymmetrical when its left and right side are not mirror images.

A distribution can have right (or positive), left (or negative), or zero skewness. A right-skewed distribution is longer on the right side of its peak, and a left-skewed distribution is longer on the left side of its peak:
![image](https://user-images.githubusercontent.com/92606737/222619252-4de0d028-05b0-4994-96d8-8d840f375153.png)



# Why Normal Distribution is important?
Transforming data into a normal distribution is important in machine learning for several reasons:
![image](https://user-images.githubusercontent.com/92606737/222619873-4705b99e-e05d-43d0-a4eb-7f652b3c230d.png)

- __Improved model performance__

     Many machine learning algorithms, such as linear regression and logistic regression, assume that the data is normally distributed. When the data is skewed, these algorithms may not perform as well and may produce biased or inaccurate results. Transforming the data into a normal distribution can improve the performance of these algorithms and lead to more accurate and reliable models.

- __Better feature scaling__
   
   Normalized data can help to improve the performance of some machine learning algorithms by reducing the impact of outliers and extreme values. Normalizing data can also help to improve the convergence of iterative algorithms such as gradient descent.

- __Better feature selection__
  
  Transforming data into a normal distribution can make it easier to identify important features that are correlated with the target variable. This is because normal distributions have a predictable and standardized shape that allows for easier analysis and interpretation.

- __Better interpretation__
    
   Normal distributions are easy to interpret and analyze. They have well-defined properties such as mean, variance, and standard deviation. This makes it easier to understand the data and draw meaningful conclusions.

- __Improved visualization__

   Normal distributions are easy to visualize and plot. This can help to identify patterns and relationships in the data that might be difficult to see in a skewed distribution.

In summary, transforming data into a normal distribution can improve the performance, interpretability, and visualization of machine learning models. However, it is important to choose the appropriate transformation based on the specific problem and the data itself. Additionally, it is important to assess the effectiveness of the transformation on the model's performance.


# Differenent methods to handle skewness of the data?
There are many methods that used in different conditions. Some are given below:
# Log Transform
   
   Log transformation is a common technique used in machine learning to transform skewed data into a more normal distribution. This can be particularly useful when working with numerical data in regression or classification problems.
   
   Log transformation is particularly useful when the data has a right-skewed distribution, where the majority of values are clustered on the left side of the distribution, and a few extreme values are on the right side. In this case, the transformation can make the data more symmetric and improve the performance of some statistical analyses that assume normality.

  In regression problems, log transformation is often used to transform response variables that have a skewed distribution. This can help to stabilize the variance and improve the accuracy of the regression model. For example, if the response variable is income, which is typically right-skewed, taking the logarithm of the income values can help to normalize the distribution and improve the performance of the regression model.

  In classification problems, log transformation can be used to transform skewed features. This can be particularly useful when using linear classifiers such as logistic regression, which assume that the features are normally distributed. Log transformation can also help to reduce the influence of outliers and improve the separation between classes.

  It's important to note that log transformation should be used with caution and only when appropriate.

 
# Least Square Transformation

The least squares transformation is a method used to transform data to approximate a linear relationship between the dependent and independent variables. It is commonly used in machine learning for linear regression problems.

In linear regression, the goal is to find the best fitting line that represents the relationship between the dependent variable and one or more independent variables. The least squares transformation is used to ensure that the errors between the predicted values and the actual values are minimized.

The least squares transformation can be useful when the data has a non-linear relationship between the independent and dependent variables, or when the data has a heteroscedastic distribution (i.e., the variance of the dependent variable changes with the level of the independent variable). By transforming the data, the relationship can be approximated by a linear model, which is easier to analyze and interpret.

One common example of using the least squares transformation in machine learning is in polynomial regression. In polynomial regression, the data is transformed by taking the logarithm, power, or root of the independent variable to approximate a non-linear relationship between the dependent and independent variables. This transformed data can then be used to fit a linear regression model.

# Reciporacal Transformation 

Reciprocal transformation is a type of transformation used in data analysis and machine learning to transform non-normally distributed data into a more normal distribution. It involves taking the reciprocal of each observation in the data set, which means dividing each observation by 1.

Reciprocal transformation is often used for data that has a positive skewness, which means that the tail of the distribution is longer on the positive side. This can happen when the data has a lower bound of zero, and the observations have a large range. In this case, the transformation can be used to reduce the range of the data and make it more symmetric around the mean.

However, it's important to note that reciprocal transformation can only be used on data that is strictly positive. If the data includes zero or negative values, the transformation is not possible. Additionally, reciprocal transformation can be sensitive to outliers, as extreme values can have a large effect on the transformation.

## Box-Cox Transformation 

Box-Cox transformation is a widely used method for transforming non-normal distributions to a normal distribution. It is named after statisticians George Box and David Cox who proposed this method in their 1964 paper.

The Box-Cox transformation is defined by the parameter λ, which can take any value from negative infinity to positive infinity. The transformation involves raising the original values of the variable to the power of λ and then subtracting 1 from the result. The value of λ is typically chosen to maximize the log-likelihood function of the transformed data, which results in the most normal distribution.

The Box-Cox transformation can be applied to any positive continuous variable, but it is particularly useful for variables that are highly skewed or have heteroscedasticity (i.e., the variance of the variable changes with the level of the variable). By transforming the data, the relationship between the dependent and independent variables can be approximated by a linear model, which is easier to interpret and analyze.

One of the advantages of the Box-Cox transformation over other transformation methods is that it can handle a wide range of data distributions and can adapt to different levels of skewness and heteroscedasticity. Additionally, the transformation is reversible, which means that the original data can be recovered from the transformed data.

# Yeo Johnson Transformation 

The Yeo-Johnson transformation is a variation of the Box-Cox transformation that can be used to transform non-normal distributions to a normal distribution. It was proposed by Robert Yeo and Robert Johnson in their 2000 paper.

The Yeo-Johnson transformation is similar to the Box-Cox transformation, but it can handle both positive and negative values of the variable, unlike the Box-Cox transformation, which can only be applied to positive values. The transformation is defined by a parameter λ, which can take any value from negative infinity to positive infinity, and a parameter σ, which is used to handle negative values of the variable.

The transformation involves two steps. In the first step, the data is shifted to make all values positive. This is done by adding a constant to the variable that is equal to the absolute value of the smallest value in the variable plus one. In the second step, the transformed data is obtained by raising the shifted data to the power of λ, subtracting 1 if λ is not equal to zero, and dividing by λ times the standard deviation of the shifted data if λ is not equal to 0, or by the natural logarithm of the shifted data plus one if λ is 0.

Like the Box-Cox transformation, the Yeo-Johnson transformation can be applied to any continuous variable, but it is particularly useful for variables that are highly skewed or have heteroscedasticity. The transformation can be used in a similar way as the Box-Cox transformation to approximate the relationship between the dependent and independent variables by a linear model.

One of the advantages of the Yeo-Johnson transformation over other transformation methods is its ability to handle both positive and negative values of the variable. Additionally, the transformation is reversible, which means that the original data can be recovered from the transformed data.


# Key Differences Between Box-Cox and Yeo-Johnson Transformations:

## Handling of Negative and Zero Values:

Box-Cox Transformation only works with strictly positive data. If any values are zero or negative, you must shift the data (e.g., by adding a constant) to apply the transformation.

Yeo-Johnson Transformation can handle both positive and negative values without requiring any modification to the data.
Formulation Differences:

Both transformations use a parameter 𝜆

λ to determine the best transformation that maximizes the log-likelihood function and makes the data more normally distributed.

When 

λ=0, Box-Cox reduces to a log transformation, while Yeo-Johnson applies a modified formula for non-positive values.
Mathematical Formulation:
 
# When to Use Which:

## Box-Cox: 
If your data is strictly positive (e.g., income, prices), Box-Cox is the better option as it is simpler.
## Yeo-Johnson:
Use it when your data contains both positive and negative values (e.g., profit/loss data).

## Practical Implementation:
Both transformations can be implemented using SciPy in Python.

Box-Cox Example:

python
Copy code
from scipy.stats import boxcox
data_transformed, lambda_ = boxcox(data)
Yeo-Johnson Example:

python
Copy code
from scipy.stats import yeojohnson
data_transformed, lambda_ = yeojohnson(data)
Conclusion:
Both transformations aim to improve normality and stabilize variance for better performance in statistical modeling. The key difference is that Box-Cox works only with positive values, while Yeo-Johnson can handle negative and zero values as we

# More Transformations 
## 1. Log Transformation
Best for: Right-skewed data (positive skew) with large ranges.

How it works: Takes the natural logarithm of each value, compressing the larger values more than smaller ones.

Limitation: Cannot handle zero or negative values directly (you need to add a constant).

python
Copy code

import numpy as np

df['log_transformed'] = np.log(df['original_data'] + 1)

## 2. Square Root Transformation
Best for: Data with moderate skewness (e.g., counts or frequency data).

How it works: Takes the square root of each value, compressing larger values but less aggressively than log transformation.

Limitation: Cannot handle negative values directly.

python
Copy code

df['sqrt_transformed'] = np.sqrt(df['original_data'])

## 3. Box-Cox Transformation
Best for: Positive data only. It is useful when you need to find the best transformation automatically.

How it works: Box-Cox transforms data using a parameter 
𝜆
λ that maximizes the likelihood of achieving normality.

Limitation: Only works on strictly positive values.

python
Copy code

from scipy.stats import boxcox

data_transformed, lambda_ = boxcox(df['original_data'] + 1e-8)

## 4. Yeo-Johnson Transformation
Best for: Data with both positive and negative values.

How it works: A generalized version of Box-Cox that can handle non-positive values. It adjusts the transformation based on the sign of the data.

python
Copy code

from scipy.stats import yeojohnson

data_transformed, lambda_ = yeojohnson(df['original_data'])

## 5. Power Transformation (Exponential or Reciprocal)

Best for: Various skewed distributions.

How it works: A power transformation (e.g., 
𝑥
1
/
2
x 
1/2
  or 
𝑥
−
1
x 
−1
 ) modifies the data's scale to reduce skewness.

Limitation: Choice of power depends on the data’s characteristics.

python
Copy code

df['reciprocal_transformed'] = 1 / df['original_data'] 

## 6. Winsorization
Best for: Outliers causing extreme skewness.

How it works: Caps the extreme values in the data at a predefined percentile, reducing their impact without removing them.

Limitation: May obscure real data patterns by flattening extreme values.

python
Copy code

from scipy.stats.mstats import winsorize

df['winsorized'] = winsorize(df['original_data'], limits=[0.05, 0.05])

## 7. Logit Transformation
Best for: Proportional data bounded between 0 and 1 (e.g., probabilities).

How it works: Transforms the data using the logit function, which is the log-odds transformation.

python
Copy code

from scipy.special import logit

df['logit_transformed'] = logit(df['proportional_data'])

## 8. Rank-Based Transformation (Quantile Transformation)
Best for: Handling extreme skewness and outliers.

How it works: Assigns ranks to data points and transforms them to follow a desired distribution (e.g., normal distribution).

python
Copy code

from sklearn.preprocessing import QuantileTransformer

qt = QuantileTransformer(output_distribution='normal')

df['quantile_transformed'] = qt.fit_transform(df[['original_data']])

## 9. Log-Log Transformation
Best for: When both the dependent and independent variables are skewed.

How it works: Applies a log transformation to both variables, making relationships linear and reducing skewness. 

## Choosing the Right Transformation

Use log transformation for highly skewed data with large values.

Square root transformation is appropriate for mildly skewed data.

Box-Cox and Yeo-Johnson transformations are suitable when you need data-driven adjustments.

Quantile transformation is ideal when you need to forcefully normalize extreme skewed data.

