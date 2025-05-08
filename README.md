# Banking Marketing Campaign Analysis

## **Project Summary**

This project presents a detailed exploratory data analysis (EDA) of a telemarketing campaign conducted by a Portuguese banking institution. The campaign aimed to promote **term deposit subscriptions** by reaching out to potential clients via phone calls.

Using Python, this project uncovers patterns in customer behavior, campaign strategies, and financial indicators to understand what factors influence whether a client subscribes to a term deposit.

---

## **Dataset Information**

- **Source**: Direct marketing campaigns (via phone) from a Portuguese bank
- **Period Covered**: May 2008 – November 2010
- **Observations**: 45,211 rows
- **Attributes**: 18 columns
- **Target Variable**: `y` — Indicates if the client subscribed to a term deposit (`yes` or `no`)

### Key Columns
- `age`: Age of the client
- `job`: Type of job (e.g., management, technician)
- `marital`: Marital status
- `education`: Education level
- `default`, `housing`, `loan`: Credit, housing, and personal loan status
- `contact`: Communication type (cellular/telephone)
- `month`, `day`, `duration`: Call timing and duration
- `campaign`, `previous`, `pdays`, `poutcome`: Campaign interaction history

---

## **Project Objectives**

- Perform data cleaning and preprocessing
- Analyze demographic and financial attributes
- Visualize customer behavior and subscription trends
- Identify correlations between attributes and the likelihood of term deposit subscription
- Offer actionable insights for improving future marketing efforts

---

## **Technologies Used**

- **Python 3.x**
- **Pandas** – Data manipulation and preprocessing
- **NumPy** – Numerical operations
- **Matplotlib** – Static data visualization
- **Seaborn** – Advanced data visualization

---

## **Exploratory Data Analysis (EDA)**

The following analyses and visualizations were performed:

- **Age Distribution** of clients
- **Job Type** and **Marital Status** frequencies
- **Education Level** trends among clients
- **Credit Defaults**, **Housing Loans**, and **Personal Loans**
- **Communication Methods** used to contact clients
- **Call Duration and Timing** insights (days and months)
- **Campaign Performance** (number of contacts, previous outcomes)
- **Client Subscription Patterns** and their correlation with:
  - Call duration
  - Average yearly balance
  - Past campaign success

Visualizations include histograms, count plots, pie charts, and a heatmap showing correlations between numerical variables and subscription likelihood.

---

## **Key Findings**

- Most clients are aged **30–40** and work in **management**, **blue-collar**, or **technician** roles.
- **Married clients** with **secondary education** form the largest demographic.
- Clients with **longer call durations** and **past positive responses** are more likely to subscribe.
- **May** saw the highest number of contacts and conversions.
- Clients with **higher average balances** show greater likelihood of subscribing.
- Most clients were **contacted only once**, and long gaps between contacts reduced conversion chances.

---
## How to Run the Project

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/RidaArshad/Finlatics.git
   cd Finlatics


