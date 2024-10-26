# A supermarket wants to know if customers’ payment method (cash, card, mobile) is related to their purchase type (groceries, electronics, clothing).

import numpy as np
from scipy.stats import chi2_contingency
#How Payment Method Analysis Helps the Supermarket Reduces operational costs by optimizing payment infrastructure. 
#Enhances customer experience by matching the right payment options to specific purchase categories.
#Enables targeted promotions in partnership with banks or mobile payment providers. 
#Predicts customer behavior to personalize offerings and improve loyalty programs. 
#Stays aligned with trends to meet evolving customer expectations (e.g., rise of mobile payments). 
#Improves forecasting and inventory management by identifying trends between payment methods and product categories.

#data

observed = np.array([
    [50, 30, 20],  # Cash
    [30, 50, 20],  # Credit Card
    [20, 20, 60]   # Mobile Payment
])

alpha=0.05

chi2, p, dof, expected = chi2_contingency(observed)
print("chi2:",chi2)
print("p:",p)
print("dof:",dof)
print("expected:",expected)

if p<alpha:
  print("reject the null hypothesis")
else:
  print("failed to reject null hypothesis")
