# Marketing Econometric Project

This project aims to build an econometric model to predict sales based on marketing spend.

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
-   **Root Directory**: The main directory contains essential project files like this `README.md`, `.gitignore`, and `requirements.txt`.

## Dataset

The dataset used in this project is `advertising.csv`, which contains data on advertising spend across different channels and the corresponding sales.

## Model

The project will use a regression model to predict sales.

## Exploratory Data Analysis Visualizations

This section presents key visualizations generated during the exploratory data analysis phase, offering insights into the dataset's distributions and relationships.

### Histograms of Variables
![Histograms of all variables](plots/histograms.png)
These histograms show the distribution of spending on TV, Radio, and Newspaper advertising, as well as the distribution of Sales.

### Box Plots of Variables
![Box plots of all variables](plots/boxplots.png)
Box plots illustrate the spread and central tendency of each variable, helping to identify outliers and understand data variability.

### Scatter Plots of Sales vs. Advertising Channels
![Scatter plots of Sales vs. Advertising Channels](plots/scatter_plots.png)
These plots visualize the relationship between advertising spend on TV, Radio, and Newspaper, and their corresponding impact on Sales. They help in identifying linear relationships and potential correlations.

### Correlation Matrix Heatmap
![Correlation Matrix Heatmap](plots/correlation_heatmap.png)
This heatmap displays the correlation coefficients between all variables in the dataset, providing a quick overview of the strength and direction of linear relationships.

## 1. Data Exploration and Preprocessing

We started by loading the `advertising.csv` dataset and examining its structure. The dataset contains 200 rows and 4 columns: `TV`, `Radio`, `Newspaper`, and `Sales`. There are no missing values in the dataset. This analysis is primarily performed in the `scripts/exploratory_analysis.py` script and the `notebooks/Exploratory_Data_Analysis.ipynb` notebook.

## 2. Correlation Analysis

**What is Correlation?**
Correlation measures the strength and direction of a linear relationship between two variables. A correlation coefficient (like Pearson's r) ranges from -1 to +1.
-   **+1:** Perfect positive linear relationship (as one variable increases, the other increases proportionally).
-   **-1:** Perfect negative linear relationship (as one variable increases, the other decreases proportionally).
-   **0:** No linear relationship.

**Why is it important?**
Understanding correlations helps us identify which advertising channels have a stronger linear association with sales, providing initial insights into their potential effectiveness.

**How it's used in this project:**
We calculated the Pearson correlation coefficient between each advertising channel (TV, Radio, Newspaper) and Sales. This was visualized using a heatmap of the correlation matrix.

**Results:**
The correlation matrix shows the following relationships:

*   **TV and Sales (0.78):** This indicates a strong positive linear correlation. As TV advertising spend increases, sales tend to increase significantly.
*   **Radio and Sales (0.58):** This shows a moderate positive linear correlation. Radio advertising also contributes positively to sales, though less strongly than TV.
*   **Newspaper and Sales (0.23):** This suggests a weak positive linear correlation. Newspaper advertising has a much weaker linear relationship with sales compared to TV and Radio.

These results suggest that TV and Radio advertising are likely better predictors for Sales than Newspaper advertising. The correlation analysis can be found in `scripts/exploratory_analysis.py` and `notebooks/Exploratory_Data_Analysis.ipynb`.

## 3. Hypothesis Testing

**What is Hypothesis Testing?**
Hypothesis testing is a statistical method used to make inferences about a population based on a sample of data. It involves formulating a null hypothesis (H0) and an alternative hypothesis (H1), collecting data, and then using statistical tests to determine whether there is enough evidence to reject the null hypothesis.

**Why is it important?**
In econometric modeling, hypothesis testing helps us determine if the relationships observed between variables in our sample data are statistically significant and likely to hold true for the larger population. It helps us avoid drawing conclusions based on random chance.

**How it's used in this project:**
We performed hypothesis tests on the coefficients of our regression model to determine the statistical significance of each advertising channel's impact on sales. Specifically, we looked at the p-value associated with each coefficient.

**Hypotheses for each coefficient (e.g., for TV advertising):**
*   **Null Hypothesis (H0):** There is no linear relationship between TV advertising spend and Sales (i.e., the coefficient for TV is zero).
*   **Alternative Hypothesis (H1):** There is a linear relationship between TV advertising spend and Sales (i.e., the coefficient for TV is not zero).

**Results (from the regression model summary):**
For each advertising channel, a t-test is performed, and a p-value is calculated.

*   **TV (p-value ≈ 0.000):** The p-value for TV advertising is extremely small (close to zero). Since this p-value is much less than the conventional significance level (alpha = 0.05), we **reject the null hypothesis**. This means there is strong statistical evidence to conclude that TV advertising has a significant linear relationship with Sales.
*   **Radio (p-value ≈ 0.000):** Similarly, the p-value for Radio advertising is very small. We **reject the null hypothesis**, indicating a statistically significant linear relationship between Radio advertising and Sales.
*   **Newspaper (p-value = 0.860):** The p-value for Newspaper advertising is very high (0.860). Since this p-value is much greater than 0.05, we **fail to reject the null hypothesis**. This implies that there is no statistically significant linear relationship between Newspaper advertising and Sales in this model.

This analysis is detailed in the `notebooks/Predictive_Modeling.ipynb` notebook.

## 4. Regression Modeling, Evaluation, and Interpretation

**What is Multiple Linear Regression?**
Multiple Linear Regression is a statistical technique used to model the linear relationship between a dependent variable (in our case, Sales) and two or more independent variables (TV, Radio, Newspaper advertising spend). The goal is to find the best-fitting linear equation that predicts the dependent variable based on the independent variables.

The general form of the multiple linear regression equation is:
`Y = β₀ + β₁X₁ + β₂X₂ + ... + βₚXₚ + ε`
Where:
-   `Y`: The dependent variable (Sales).
-   `β₀`: The intercept, representing the expected value of Y when all independent variables are zero.
-   `β₁, β₂, ..., βₚ`: The coefficients for each independent variable, representing the change in Y for a one-unit increase in the corresponding X, holding other variables constant.
-   `X₁, X₂, ..., Xₚ`: The independent variables (TV, Radio, Newspaper).
-   `ε`: The error term, representing the unexplained variance or noise in the model.

**Why is it important?**
Regression modeling allows us to quantify the impact of each advertising channel on sales, predict future sales based on advertising budgets, and identify the most effective channels for investment.

**How it's used in this project:**
We built a multiple linear regression model using the `statsmodels` library in Python. The model predicts `Sales` based on `TV`, `Radio`, and `Newspaper` advertising spend.

**Model Summary and Key Metrics:**
The model summary from the `notebooks/Predictive_Modeling.ipynb` notebook provides several key metrics for evaluating the model's performance and the significance of its components:

*   **R-squared (0.897) and Adjusted R-squared (0.896):**
    *   **What they mean:** R-squared measures the proportion of the variance in the dependent variable (Sales) that can be predicted from the independent variables (advertising spend). Adjusted R-squared is a modified version that accounts for the number of predictors in the model, providing a more accurate measure for models with multiple independent variables.
    *   **Interpretation:** An R-squared value of 0.897 indicates that approximately 89.7% of the variation in Sales can be explained by the advertising spend on TV, Radio, and Newspaper. This is a very high value, suggesting that our model is a good fit for the data. The adjusted R-squared being very close to R-squared suggests that the included predictors are valuable and not just adding noise.

*   **F-statistic (570.3) and its p-value (≈ 0.000):**
    *   **What they mean:** The F-statistic is used to test the overall significance of the regression model. It compares the fit of the model with predictors to the fit of a model with no predictors. The p-value associated with the F-statistic tells us the probability of observing such an F-statistic if the null hypothesis (that all regression coefficients are zero) were true.
    *   **Interpretation:** A very large F-statistic (570.3) and an extremely small p-value (close to zero) indicate that the overall regression model is statistically significant. This means that at least one of the advertising channels has a significant linear relationship with Sales.

*   **Coefficients (β) and their p-values (t-test):**
    *   **What they mean:** The coefficients represent the estimated change in Sales for a one-unit increase in the corresponding advertising spend, holding other advertising spends constant. The p-value for each coefficient (from a t-test) indicates the statistical significance of that individual predictor.
    *   **Interpretation:**
        *   **TV (Coefficient: 0.0458, p-value ≈ 0.000):** For every £1 increase in TV advertising spend, Sales are expected to increase by approximately 0.0458 units, holding Radio and Newspaper spend constant. The very low p-value indicates this relationship is highly statistically significant.
        *   **Radio (Coefficient: 0.1885, p-value ≈ 0.000):** For every £1 increase in Radio advertising spend, Sales are expected to increase by approximately 0.1885 units, holding TV and Newspaper spend constant. This relationship is also highly statistically significant. Notably, Radio has a larger impact per unit of spend than TV.
        *   **Newspaper (Coefficient: -0.0010, p-value = 0.860):** The coefficient for Newspaper is very close to zero and its p-value is very high. This indicates that Newspaper advertising does not have a statistically significant linear relationship with Sales in this model. The negative sign, though negligible, suggests a very slight, almost non-existent, inverse relationship.
        *   **Intercept (β₀):** This represents the baseline sales when all advertising spend is zero.

*   **Multicollinearity (Variance Inflation Factor - VIF):**
    *   **What it means:** Multicollinearity occurs when independent variables in a regression model are highly correlated with each other. High multicollinearity can make it difficult to interpret the individual coefficients and can lead to unstable model estimates. VIF measures how much the variance of an estimated regression coefficient is inflated due to multicollinearity. A VIF value typically below 5 or 10 is considered acceptable.
    *   **Interpretation:** The VIF values for all variables in our model are very low (all less than 2). This indicates that there is no significant multicollinearity among the advertising channels, ensuring that the individual coefficients can be reliably interpreted.

This comprehensive analysis is detailed in the `notebooks/Predictive_Modeling.ipynb` notebook.

## 6. Budget Optimization

We used the trained multiple linear regression model to find the optimal allocation of a £1000 budget. The optimal budget allocation is:

*   **TV:** £0.00
*   **Radio:** £1000.00
*   **Newspaper:** £0.00

Estimated maximum sales for a £1000 budget: **188.54**

This result is driven by the fact that the coefficient for Radio is much larger than the coefficients for TV and Newspaper.

## 7. A/B Testing Discussion

The `data/advertising.csv` dataset is an observational dataset. Therefore, a traditional A/B test is not applicable. While we cannot perform a traditional A/B test, our regression model can still provide valuable insights. However, we should be careful about making strong causal claims based on this observational data.

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