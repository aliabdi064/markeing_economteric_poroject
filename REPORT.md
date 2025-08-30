# Marketing Econometric Project: A Deep Dive into Advertising's Impact on Sales

## Introduction

**What is this project about?**

This project aims to understand the relationship between advertising spend on different channels (TV, Radio, and Newspaper) and sales. We use econometric techniques to build a predictive model that can not only forecast sales but also help in optimizing the advertising budget.

**Why is it important?**

In today's competitive market, it's crucial for businesses to understand the effectiveness of their marketing campaigns. By analyzing the data, we can identify which advertising channels are providing the best return on investment and make data-driven decisions to maximize sales.

## Project Structure

The project is now organized into a clean and logical directory structure to enhance navigability and maintainability:

-   **`data/`**: Contains the raw dataset (`advertising.csv`).
-   **`notebooks/`**: Houses all Jupyter notebooks (`.ipynb` files) used for exploratory data analysis, predictive modeling, and comprehensive analysis.
-   **`plots/`**: Stores all generated image files (`.png`) from the data visualization steps.
-   **`scripts/`**: Contains Python scripts (`.py` files) for various tasks such as data loading, exploratory analysis, and regression modeling.
-   **Root Directory**: The main directory contains essential project files like this `REPORT.md`, `README.md`, `.gitignore`, and `requirements.txt`.

## 1. Data Exploration and Preprocessing

We started by loading the `advertising.csv` dataset and examining its structure. The dataset contains 200 rows and 4 columns: `TV`, `Radio`, `Newspaper`, and `Sales`. There are no missing values in the dataset. This analysis is primarily performed in the `exploratory_analysis.py` script and the `Exploratory_Data_Analysis.ipynb` notebook.

## 2. Correlation Analysis

We calculated the correlation between the variables in our dataset. The correlation matrix shows that:

*   **TV** has a strong positive correlation with Sales (0.78).
*   **Radio** has a moderate positive correlation with Sales (0.58).
*   **Newspaper** has a weak positive correlation with Sales (0.23).

This suggests that TV and Radio are good predictors for Sales. The correlation analysis can be found in `exploratory_analysis.py` and `Exploratory_Data_Analysis.ipynb`.

## 3. Hypothesis Testing

We performed a hypothesis test to check the significance of the relationship between TV advertising and sales. The p-value for the TV coefficient was very close to zero, which means that we can reject the null hypothesis and conclude that there is a statistically significant relationship between TV advertising and sales. This is detailed in the `Predictive_Modeling.ipynb` notebook.

## 4. Regression Modeling

We built a multiple linear regression model to predict sales using all three advertising channels. The model summary from the `Predictive_Modeling.ipynb` notebook shows that:

*   **R-squared:** 0.897
*   **Adjusted R-squared:** 0.896
*   **F-statistic:** 570.3

## 5. Model Evaluation and Interpretation

*   **R-squared and Adjusted R-squared:** The R-squared value of 0.897 indicates that approximately 89.7% of the variance in sales can be explained by the advertising spend on TV, Radio, and Newspaper.
*   **F-statistic:** The F-statistic is very large (570.3) and the p-value is very close to zero, which means that the overall model is statistically significant.
*   **Coefficients and p-values (t-test):**
    *   **TV:** The coefficient for TV is 0.0458. This is a statistically significant relationship.
    *   **Radio:** The coefficient for Radio is 0.1885. This is a statistically significant relationship.
    *   **Newspaper:** The coefficient for Newspaper is -0.0010. This relationship is not statistically significant.
*   **Multicollinearity (VIF):** The VIF values for all variables are very low (all less than 2), which indicates that there is no significant multicollinearity in the model.

## 6. Budget Optimization

We used the trained multiple linear regression model to find the optimal allocation of a £1000 budget. The optimal budget allocation is:

*   **TV:** £0.00
*   **Radio:** £1000.00
*   **Newspaper:** £0.00

Estimated maximum sales for a £1000 budget: **188.54**

This result is driven by the fact that the coefficient for Radio is much larger than the coefficients for TV and Newspaper.

## 7. A/B Testing Discussion

The `advertising.csv` dataset is an observational dataset. Therefore, a traditional A/B test is not applicable. While we cannot perform a traditional A/B test, our regression model can still provide valuable insights. However, we should be careful about making strong causal claims based on this observational data.

## 8. Conclusion and Recommendations

**Summary of Findings:**

*   We have successfully built a multiple linear regression model that can predict sales based on advertising spend.
*   The model has a high R-squared value (0.897).
*   TV and Radio advertising have a statistically significant positive impact on sales, with Radio having a much larger impact per pound spent.
*   Newspaper advertising does not have a statistically significant impact on sales.

**Recommendations:**

*   **Focus on Radio advertising:** The model suggests that Radio advertising is the most effective channel for increasing sales.
*   **Continue with TV advertising:** TV advertising also has a significant positive impact on sales.
*   **Re-evaluate Newspaper advertising:** The company should consider re-evaluating its strategy for Newspaper advertising and potentially reallocate the budget to Radio and TV.

**Next Steps and Further Analysis:**

*   **Explore Interaction Terms:** The current model assumes that the effect of each advertising channel is independent. It would be worthwhile to explore interaction terms (e.g., the combined effect of TV and Radio advertising) to see if they improve the model.
*   **Consider Non-linear Models:** The relationship between advertising spend and sales might not be perfectly linear. Exploring non-linear models could potentially yield a more accurate model.
*   **Run Controlled Experiments:** To get a better understanding of the causal impact of advertising on sales, the company should consider running controlled experiments (e.g., A/B tests) in the future.