import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as sns  


file_path = "C:/Users/ASUS/OneDrive/Desktop/Banking/banking_data.csv"
df = pd.read_csv(file_path)  


print("First 5 rows of the dataset:")
print(df.head())


print("\nChecking for missing values:")
print(df.isnull().sum())


cat_cols = ['job', 'education', 'contact', 'poutcome']
df[cat_cols] = df[cat_cols].fillna("unknown")


num_cols = ['balance', 'duration', 'campaign', 'previous', 'pdays']
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

#Answer to Questions:-

# Age distribution 
plt.figure(figsize=(8,5))
sns.histplot(df['age'], bins=30, kde=True, color="blue")
plt.title("Age Distribution of Clients")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Job Type distribution 
plt.figure(figsize=(10,5))
sns.countplot(y=df['job'], order=df['job'].value_counts().index, palette="viridis")
plt.title("Job Type Distribution")
plt.xlabel("Count")
plt.ylabel("Job Type")
plt.show()

# Marital Status distribution
plt.figure(figsize=(6,4))
sns.countplot(x=df['marital'], palette="coolwarm")
plt.title("Marital Status of Clients")
plt.xlabel("Marital Status")
plt.ylabel("Count")
plt.show()

# Education level 
plt.figure(figsize=(6,4))
sns.countplot(x=df['education'], palette="Set2")
plt.title("Education Level of Clients")
plt.xlabel("Education")
plt.ylabel("Count")
plt.show()

# credit default 
plt.figure(figsize=(5,5))
df['default'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=["red", "green"])
plt.title("Clients with Credit Default")
plt.ylabel("")
plt.show()

# Housing aur Personal Loans
fig, ax = plt.subplots(1, 2, figsize=(12,5))
sns.countplot(x=df['housing'], ax=ax[0], palette="pastel")
ax[0].set_title("Housing Loan Distribution")
sns.countplot(x=df['loan'], ax=ax[1], palette="cool")
ax[1].set_title("Personal Loan Distribution")
plt.show()

#communication clients ko contact karne ke liye
plt.figure(figsize=(6,4))
sns.countplot(x=df['contact'], palette="Blues")
plt.title("Contact Type Used in Campaigns")
plt.xlabel("Contact Type")
plt.ylabel("Count")
plt.show()

# subscription to the term deposit he ya nhi
plt.figure(figsize=(6,4))
sns.countplot(x=df['y'], palette=["#FF9999", "#66B2FF"])
plt.title("Subscription to Term Deposit")
plt.xlabel("Subscribed (yes/no)")
plt.ylabel("Count")
plt.show()

# Distribution of the last contact day of the month
plt.figure(figsize=(8,5))
sns.histplot(df['day'], bins=31, kde=False, color="purple")
plt.title("Distribution of Last Contact Day of the Month")
plt.xlabel("Day of the Month")
plt.ylabel("Count")
plt.show()

# How does the last contact month vary among clients
plt.figure(figsize=(8,5))
sns.countplot(x=df['month'], order=["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], palette="coolwarm")
plt.title("Distribution of Last Contact Month")
plt.xlabel("Month")
plt.ylabel("Count")
plt.show()

# Distribution of the duration of the last contact
plt.figure(figsize=(8,5))
sns.histplot(df['duration'], bins=30, kde=True, color="green")
plt.title("Distribution of Duration of Last Contact")
plt.xlabel("Duration (seconds)")
plt.ylabel("Count")
plt.show()

# kitne contacts hue during the campaign
plt.figure(figsize=(8,5))
sns.histplot(df['campaign'], bins=20, kde=False, color="orange")
plt.title("Number of Contacts Performed During Campaign")
plt.xlabel("Number of Contacts")
plt.ylabel("Count")
plt.show()

# kitne din passed since last contact from a previous campaign
plt.figure(figsize=(8,5))
sns.histplot(df['pdays'], bins=30, kde=True, color="red")
plt.title("Days Passed Since Last Contact from Previous Campaign")
plt.xlabel("Days")
plt.ylabel("Count")
plt.show()

# kitne contacts performed before the current campaign
plt.figure(figsize=(8,5))
sns.histplot(df['previous'], bins=20, kde=True, color="brown")
plt.title("Number of Contacts Before Current Campaign")
plt.xlabel("Number of Contacts")
plt.ylabel("Count")
plt.show()

# Distribution of average 
plt.figure(figsize=(8,5))
sns.histplot(df['balance'], bins=30, kde=True, color="teal")
plt.title("Distribution of Average Yearly Balance")
plt.xlabel("Balance")
plt.ylabel("Count")
plt.show()


#Outcomes of previous 
plt.figure(figsize=(6,4))
sns.countplot(x=df['poutcome'], palette="Set3")
plt.title("Outcomes of Previous Marketing Campaigns")
plt.xlabel("Outcome")
plt.ylabel("Count")
plt.show()

# correlations 
plt.figure(figsize=(14,10))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="PuBuGn", linewidths=0.5)
plt.title("Correlation Between Attributes and Subscription Likelihood")
plt.show()


print("\nSummary statistics of numerical columns:")
print(df.describe())

print("\nFinal dataset info:")
print(df.info())


