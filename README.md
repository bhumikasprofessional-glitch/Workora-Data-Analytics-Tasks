# Workora-Data-Analytics-Tasks
Data Cleaning &amp; Structural Validation Pipeline built for Workora Data Analytics Module.
## --- Module 2 Task: Customer Churn Analysis Pipeline ---

### 1. Objective & Risk Constraints
The system evaluates account-level transaction frequency, purchase recency, and scoring history to isolate churn dynamics. Users who exhibit severe rating dissatisfaction (Average Score $\le 2.0$) or cross the temporal expiration limit (inactive post-2010) are classified under the 'Churned' cohort matrix to identify factors behind cancellations.

### 2. Extracted Behavioral Trends
* **Rating Correlation Analysis:** Box plot metrics demonstrate that churned users show high clusters around critical review limits, signaling that bad quality experiences directly drive retention drops.
* **Operational Value:** Generates a structured account metric matrix (`Customer_Churn_Analysis_Report.csv`) helping CRM units execute automated win-back strategies.
