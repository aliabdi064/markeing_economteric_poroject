# Marketing Econometric Project: A Deep Dive into Advertising's Impact on Sales

## Introduction

**What is this project about?**

This project aims to understand the relationship between advertising spend on different channels (TV, Radio, and Newspaper) and sales. We will use econometric techniques to build a predictive model that can not only forecast sales but also help in optimizing the advertising budget.

**Why is it important?**

In today's competitive market, it's crucial for businesses to understand the effectiveness of their marketing campaigns. By analyzing the data, we can identify which advertising channels are providing the best return on investment and make data-driven decisions to maximize sales.

**How will we do it?**

We will follow a step-by-step approach:

1.  **Data Exploration:** We'll start by exploring the dataset to understand its structure and the relationships between variables.
2.  **Correlation Analysis:** We'll examine the correlation between different advertising channels and sales.
3.  **Hypothesis Testing:** We'll formulate and test hypotheses to validate our assumptions.
4.  **Regression Modeling:** We'll build a multiple linear regression model to predict sales based on advertising spend.
5.  **Model Evaluation:** We'll evaluate the model's performance and interpret the results.
6.  **Budget Optimization:** We'll use the model to find the optimal allocation of a £1000 budget to maximize sales.
7.  **A/B Testing Discussion:** We will discuss the concept of A/B testing and its applicability to this dataset.

## 1. Data Exploration and Preprocessing

We started by loading the `advertising.csv` dataset and examining its structure. The dataset contains 200 rows and 4 columns: `TV`, `Radio`, `Newspaper`, and `Sales`. There are no missing values in the dataset.

## 2. Correlation Analysis

We calculated the correlation between the variables in our dataset. The correlation matrix shows that:

*   **TV** has a strong positive correlation with Sales (0.78).
*   **Radio** has a moderate positive correlation with Sales (0.58).
*   **Newspaper** has a weak positive correlation with Sales (0.23).

This suggests that TV and Radio are good predictors for Sales.

## 3. Hypothesis Testing

We performed a hypothesis test to check the significance of the relationship between TV advertising and sales. The p-value for the TV coefficient was very close to zero, which means that we can reject the null hypothesis and conclude that there is a statistically significant relationship between TV advertising and sales.

## 4. Regression Modeling

We built a multiple linear regression model to predict sales using all three advertising channels. The model summary shows that:

*   **R-squared:** 0.897
*   **Adjusted R-squared:** 0.896
*   **F-statistic:** 570.3

## 5. Model Evaluation and Interpretation

*   **R-squared and Adjusted R-squared:** The R-squared value of 0.897 indicates that approximately 89.7% of the variance in sales can be explained by the advertising spend on TV, Radio, and Newspaper. The adjusted R-squared is also very close to the R-squared, which means that the additional variables are adding value to the model.
*   **F-statistic:** The F-statistic is very large (570.3) and the p-value is very close to zero, which means that the overall model is statistically significant.
*   **Coefficients and p-values (t-test):**
    *   **TV:** The coefficient for TV is 0.0458, and the p-value is very close to zero. This means that for every £1000 increase in TV advertising spend, sales are expected to increase by approximately 45.8 units, holding other variables constant. This is a statistically significant relationship.
    *   **Radio:** The coefficient for Radio is 0.1885, and the p-value is very close to zero. This means that for every £1000 increase in Radio advertising spend, sales are expected to increase by approximately 188.5 units, holding other variables constant. This is a statistically significant relationship.
    *   **Newspaper:** The coefficient for Newspaper is -0.0010, and the p-value is 0.860. This means that the relationship between Newspaper advertising spend and sales is not statistically significant. The coefficient is also very close to zero, which suggests that Newspaper advertising has a negligible impact on sales.
*   **Multicollinearity (VIF):** The VIF values for all variables are very low (all less than 2), which indicates that there is no significant multicollinearity in the model.

## 6. Budget Optimization

We used the trained multiple linear regression model to find the optimal allocation of a £1000 budget across the three advertising channels to maximize sales. The optimal budget allocation is:

*   **TV:** £0.00
*   **Radio:** £1000.00
*   **Newspaper:** £0.00

Estimated maximum sales for a £1000 budget: **188.54**

This result is driven by the fact that the coefficient for Radio is much larger than the coefficients for TV and Newspaper.

## 7. A/B Testing Discussion

**What is A/B testing?**

A/B testing is a randomized controlled experiment where two or more versions of a variable are shown to different segments of users at the same time to see which version has the most impact on a specific metric.

**Is A/B testing applicable to this dataset?**

The `advertising.csv` dataset is an observational dataset, which means that the data was collected by observing the world as it is, without any intervention from our side. Therefore, a traditional A/B test is not applicable to this dataset.

**What can we do instead?**

While we cannot perform a traditional A/B test, our regression model can still provide valuable insights into the relationship between advertising spend and sales. However, we should be careful about making strong causal claims based on this observational data.

## 8. Conclusion and Recommendations

**Summary of Findings:**

*   We have successfully built a multiple linear regression model that can predict sales based on advertising spend on TV, Radio, and Newspaper.
*   The model has a high R-squared value, which means that it can explain a large portion of the variance in sales.
*   TV and Radio advertising have a statistically significant positive impact on sales, with Radio having a much larger impact per pound spent.
*   Newspaper advertising does not have a statistically significant impact on sales.
*   We have found the optimal allocation of a £1000 budget to be entirely on Radio advertising.

**Recommendations:**

*   **Focus on Radio advertising:** The model suggests that Radio advertising is the most effective channel for increasing sales. The company should consider increasing its budget for Radio advertising.
*   **Continue with TV advertising:** TV advertising also has a significant positive impact on sales, so it should be continued.
*   **Re-evaluate Newspaper advertising:** The model suggests that Newspaper advertising is not effective. The company should consider re-evaluating its strategy for Newspaper advertising. It might be better to reallocate the budget from Newspaper to Radio and TV.
*   **Further Analysis:** To get a better understanding of the causal impact of advertising on sales, the company should consider running controlled experiments (e.g., A/B tests) in the future.
