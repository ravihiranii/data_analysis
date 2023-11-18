
# importing a necessary libraries:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# initializing a df as a DataFrame
df = pd.DataFrame()

# Reading a CSV File
df = pd.read_csv('shopping_trends_updated.csv')
print(df.head())

# Printing columns of dataframe
print(df.columns)







# 1. Customer Demographics:

# Q-1.1 What is the distribution of customers by age and gender?

combine = df.groupby(['Age','Gender']).size().unstack()
print(combine)

# Plotting the result
combine.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Distribution of Customers by Age and Gender')
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend(title='Gender', loc='upper right')
plt.show()




# Q-1.2 How is the distribution of customers across different locations?

location = df.groupby('Location').size()
print(location)

# Plotting the result
loc = [location for location, df in df.groupby('Location')]

plt.figure(figsize=(12,6))
plt.bar(loc,df.groupby('Location').size(), color='b', label='States')
plt.xticks(loc, rotation='vertical', size=8)
plt.title('Distribution of Customers by Location')
plt.xlabel('Location')
plt.ylabel('No.of Customer')
plt.legend()
plt.tight_layout()
plt.show()



# 2. Purchase Analysis:

# Q-2.1 What are the most purchased items and categories?

most_purchase = df.groupby(['Category','Item Purchased']).size()
print(most_purchase)

plt.figure(figsize=(10, 6))
most_purchase.plot(kind='bar', color='skyblue')
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Number of Items Purchased in Each Category')
plt.xticks(rotation=45)  # Rotates the x-axis labels for better readability
plt.tight_layout()
plt.show()


# Now we want to print most purchased item and category:

new_df = df.groupby(['Category','Item Purchased']).size().sort_values(ascending=False)

for x in new_df[:10].index.tolist():
    print(x)










#    Q-2.2 How does the purchase amount vary across different items and categories?
#    Q-2.3 Are there any seasonal trends in purchasing behavior?

