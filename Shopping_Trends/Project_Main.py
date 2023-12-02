
# importing a necessary libraries:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# initializing a df as a DataFrame
df = pd.DataFrame()

# Read a CSV File through a Pandas
df = pd.read_csv('shopping_trends_updated.csv')
print(df.head())

# Printing columns of dataframe
print(df.columns)





# 1. Customer Demographics:

# Q-1.1 What is the distribution of customers by age and gender?

# Using a Groupby to make a Age & Gender group
groupby_age_gender = df.groupby(['Age','Gender']).size().unstack()
print(groupby_age_gender)

# Plotting the result
groupby_age_gender.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Distribution of Customers by Age and Gender')
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend(title='Gender', loc='upper right')
plt.show()


# Q-1.2 How is the distribution of customers across different locations?

# Count the distribution of customer by Location
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

# Count the Purchase by grouping items and categories
most_purchase = df.groupby(['Category','Item Purchased']).size()
print(most_purchase)

# Plotting the result
plt.figure(figsize=(10, 6))
most_purchase.plot(kind='bar', color='skyblue')
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Number of Items Purchased in Each Category')
plt.xticks(rotation=45)  # Rotates the x-axis labels for better readability
plt.tight_layout()
plt.show()

# Print the most top 10 purchased items and categories:
new_df = df.groupby(['Category','Item Purchased']).size().sort_values(ascending=False)
top_10_items_and_category = new_df[:10]

print('Top 10 Most Purchased Items and Categories: \n')
for category, item in top_10_items_and_category.index:
    print(f'Category: {category}, Items: {item}, Count: {new_df[(category,item)]}')


# Q-2.2 How does the purchase amount vary across different items and categories?

# Calculate the Purchase Amount by Different Items
amount_by_items = df.groupby('Item Purchased')['Purchase Amount (USD)'].sum()
print(amount_by_items)

# Plotting the result
amount_by_items.plot(kind='bar', figsize=(10,8))
plt.title('Amount of purchase by different items')
plt.xlabel('Items')
plt.ylabel('Amount in US($)')
plt.tight_layout()
plt.show()

# Calculate the Purchase Amount by Different Category
amount_by_categories = df.groupby('Category')['Purchase Amount (USD)'].sum()
print(amount_by_categories)

# Plotting the result
plt.figure(figsize=(10,6))
plt.pie(amount_by_categories, labels=amount_by_categories.index, autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Amount Purchase by Different Categories')
plt.axis('equal')
plt.show()


#    Q-2.3 Are there any seasonal trends in purchasing behavior?

# Calculate the Purchase amount on Seasonal Trends
seasonal_trends = df.groupby('Season')['Purchase Amount (USD)'].sum()
print(seasonal_trends)

# Plotting the result
plt.figure(figsize=(10,6))
seasonal_trends.plot(kind='bar')
plt.title('Amount of Purchase by Seasons')
plt.xlabel('Seasons')
plt.ylabel('Purchase Amount in US($)')
plt.tight_layout()
plt.show()





# 3. Customer Behavior:

# Q-3.1 How frequently do customers make purchases?

# Count the frequency of the purchases
freq_of_purchase = df.groupby('Frequency of Purchases').size()
print(freq_of_purchase)


# Q-3.2 Is there a correlation between the frequency of purchases and age?

freq_of_purchase_by_age = df.groupby('Age')['Previous Purchases'].sum()
print(freq_of_purchase_by_age)

# Creating a line plot
plt.figure(figsize=(10, 6))
freq_of_purchase_by_age.plot(kind='line', marker='o')  # Line plot with markers at data points
plt.xlabel('Age')
plt.ylabel('Total Previous Purchases')
plt.title('Total Previous Purchases by Age')
plt.grid(True)  # Adding gridlines for better readability
plt.show()

# Find Correlation Co-efficient   
correlation_coefficient = df['Age'].corr(df['Previous Purchases'])
print(correlation_coefficient)

# Plotting result 
plt.figure(figsize=(6, 4))
sns.heatmap(data=df[['Age', 'Previous Purchases']].corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap: Age vs Previous Purchases')
plt.show()


# Q-3.3 Do customers who use promo codes tend to make larger purchases?

count_promo_user = df.groupby('Promo Code Used').size()
print(count_promo_user)

share_of_promouser_in_purchase = df.groupby('Promo Code Used')['Purchase Amount (USD)'].sum()
print(share_of_promouser_in_purchase)

share_of_promouser_in_purchase.index = ['Non-Promo Code User', 'Promo Code User']

plt.figure(figsize=(10,8))
plt.pie(share_of_promouser_in_purchase,autopct='%1.1f%%',labels=share_of_promouser_in_purchase.index,startangle=90)
plt.title('Percentage of Total Purchased Amount by Promo-Non Promo User')
plt.axis('equal')
plt.show()






# 4. Product and Review Analysis:

# Q-4.1: What is the average review rating for different items and categories?

# Average Review Rating by Different Items
review_rating_by_items = df.groupby('Item Purchased')['Review Rating'].mean().reset_index()
print(review_rating_by_items)

# Plotting a result with seaborn barplot
plt.figure(figsize=(10,8))
sns.barplot(x='Item Purchased',y='Review Rating',data=review_rating_by_items)
plt.title('Average of Review Ratings by Different Items')
plt.xlabel('Items')
plt.ylabel('Ratings')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Average Review Rating by Different Category
review_rating_by_category = df.groupby('Category')['Review Rating'].mean().reset_index()
print(review_rating_by_category)

# Plotting a result with seaborn barplot
plt.figure(figsize=(6,6))
sns.barplot(x='Category',y='Review Rating', data=review_rating_by_category)
plt.title('Average of Review Ratings by Different Category')
plt.xlabel('Category')
plt.ylabel('Ratings')
plt.tight_layout()
plt.show()



# Q-4.2: Is there a relationship between the review rating and the purchase amount?

# Get the correlation co-efficient
relation_status = df[[ 'Purchase Amount (USD)','Review Rating']]
correlation = relation_status.corr('pearson')
print(correlation)


grouped_data = df.groupby('Review Rating')['Purchase Amount (USD)'].mean().reset_index()
print(grouped_data)

plt.figure(figsize=(10, 6))
sns.swarmplot(x=grouped_data['Review Rating'], y=grouped_data['Purchase Amount (USD)'], data=df)
plt.title('Average of Purchase Amount Distribution by Review Rating')
plt.xlabel('Review Rating')
plt.ylabel('Purchase Amount (USD)')
plt.show()


# Q-4.3: Do certain colors or sizes receive higher review ratings?

# Higher Review Ratings By Different Size
size_review_rating = df.groupby('Size')['Review Rating'].mean().sort_values(ascending=False)
print(size_review_rating)

# Plotting the result into graph
plt.figure(figsize=(8,8))
plt.pie(size_review_rating, labels=size_review_rating.index, autopct='%1.1f%%', startangle=90)
plt.title('Rate of Review Rating by Different Sizes')
plt.axis('equal')
plt.show()


# Review Rating By Different Colors 
color_review_rating = df.groupby('Color')['Review Rating'].mean().sort_values(ascending=False).reset_index()
print(color_review_rating)

# Print the TOP-5 Colors by Review Ratings
print(color_review_rating.head(5))

# Plotting the result
plt.figure(figsize=(10,8))
sns.barplot(x='Color',y='Review Rating',data=color_review_rating, palette='viridis')
plt.title('Popular Colors by Review Rating')
plt.xticks(rotation=45)
plt.xlabel('Colors')
plt.ylabel('Review Rating')
plt.show()






# 5. Subscription and Discount Analysis:

# Q-5.1 What percentage of customers are subscribed to a service?

subscription = df.groupby('Subscription Status').size()
print(subscription)

# Calculate total count of customers
total_customers = subscription.sum()

# Calculate percentages
subscription_percentages = (subscription / total_customers) * 100
print(subscription_percentages)

# Using Pie-Chart for visualize the percentage of amount of subscription & non-subscription customer:

# Here we explode the part of Subscribe User
explode = (0.1,0)

plt.figure(figsize=(10,8))
plt.pie(subscription,labels=subscription.index, autopct='%2.1f%%', startangle=90, explode=explode)
plt.title('Distribution of Subscription Members')
plt.axis('equal')
plt.show()


# Q-5.2 How often do customers use discounts, and does it affect their purchase behavior?

# Check how many customer use discount
discount_user = df.groupby('Discount Applied').size()
print(discount_user)

# Check Relation of User with Purchased amount with respect to Discount Applied
discount = df.groupby('Discount Applied')['Purchase Amount (USD)'].sum()
print(discount)


# Q-5.3 Are there specific payment methods preferred by subscribers?

# Count the Subscribe Customer
subscribers = df[df['Subscription Status'] == 'Yes']

# Grouped by subscribe customer with payment type
payment_method = subscribers.groupby('Payment Method').size()
print(payment_method)

# Identify the index corresponding to the maximum count
max_index = payment_method.idxmax()

# Create an explode list with the maximum slice exploded
explode = [0.1 if idx == max_index else 0 for idx in payment_method.index]

# Plotting a Result
plt.figure(figsize=(10,8))
plt.pie(payment_method, labels=payment_method.index, autopct='%1.1f%%',startangle=90, explode=explode)
plt.title('Distribution of Payment Method by Subscribe User')
plt.axis('equal')
plt.show()






# 6.Geographical Insights:

# Q-6.1 Are there any location-specific trends in purchasing behavior?

purchase_by_loc = df.groupby('Location')['Purchase Amount (USD)'].sum().reset_index()
print(purchase_by_loc)

plt.figure(figsize=(12,8))
sns.barplot(x=purchase_by_loc['Location'],y=purchase_by_loc['Purchase Amount (USD)'],data=df)
plt.xticks(rotation='vertical')
plt.title('Purchasing behaviour by Different Location')
plt.xlabel('Locations')
plt.ylabel('Purchased Amount in US($)')
plt.ylim(3000,6000)
plt.tight_layout()
plt.show()


# Q-6.2 How does shipping type preference vary across different locations?

location_count = df['Location'].nunique()
print(location_count)

shipping_type_by_loc = df.groupby(['Location','Shipping Type']).size()
print(shipping_type_by_loc)
# Half Solved

def get_popular_shipping_type_by_loc(df):
    shipping_type_by_loc = df.groupby(['Location', 'Shipping Type']).size()
    max_shipping_type_by_loc = shipping_type_by_loc.unstack(fill_value=0).idxmax(axis=1)
    for location, max_type in max_shipping_type_by_loc.items():
        max_count = shipping_type_by_loc.loc[(location, max_type)]
        print(f"{location} - {max_type} {max_count}")

result = get_popular_shipping_type_by_loc(df.copy())





# 7. Customer Retention:

# Q-7.1 What is the rate of repeat customers based on previous purchases?

repeat_customer = df.groupby('Previous Purchases').size()
print(repeat_customer)

no_of_purchases = range(1,51)

plt.figure(figsize=(10,8))
repeat_customer.plot(kind='area')
plt.title('Rate of Repeat Customers')
plt.xticks(no_of_purchases, rotation='vertical')
plt.xlabel('Previous Purchases')
plt.ylabel('Count of Purchases')
plt.ylim(50,None)
plt.grid()
plt.show()


# Q-7.2 Are there patterns in the types of items that lead to repeat purchases?

repeat_item = df.groupby('Item Purchased').size().sort_values(ascending=False)
print(repeat_item)

most_sell_items = repeat_item[:10]

print('\nMost Repeat Purchased Items:')
for item, count in most_sell_items.items():
    print(f"{item} : {count}")

repeat_item = df.groupby('Item Purchased').size().reset_index(name='Count')
print(repeat_item)

#Plotting result
plt.figure(figsize=(12, 6))
sns.barplot(x='Item Purchased', y='Count', data=repeat_item, palette='viridis')
plt.title('Count of Items Purchased')
plt.xlabel('Item Purchased')
plt.ylabel('Count')
plt.xticks(rotation=90)  # Rotating x-axis labels for better readability
plt.ylim(100,None)
plt.tight_layout()
plt.show()






# 8. Payment Method Analysis:

# Q-8.1 What are the most popular payment methods among customers?

# Count the different payment method used by customers
popular_payment_method = df.groupby('Payment Method').size()
print(popular_payment_method)

max_use_payment_method = popular_payment_method.idxmax()

explode = [0.1 if idx == max_use_payment_method else 0 for idx in popular_payment_method.index]

# Plotting the result 
plt.figure(figsize=(8,8))
plt.pie(popular_payment_method, labels=popular_payment_method.index ,autopct='%1.1f%%',startangle=30, explode=explode)
plt.axis('equal')
plt.title('Distribution of Payment Method by Customers')
plt.show()


# Q-8.2 Is there a correlation between payment method and purchase amount?

# Count the purchased amount by different payment method
corr_payment = df.groupby('Payment Method')['Purchase Amount (USD)'].sum()
print(corr_payment)

max_use_pay_method_by_purchase = corr_payment.idxmax()

explode = [0.1 if idx == max_use_pay_method_by_purchase else 0 for idx in corr_payment.index]

# Plotting the result
plt.figure(figsize=(8,8))
plt.pie(corr_payment, labels=corr_payment.index ,autopct='%1.1f%%',startangle=30, explode=explode)
plt.axis('scaled')
plt.title('Distribution of Purchase Amount by Payment Method ')
plt.show()






# 9. Size and Color Preferences:

# Q-9.1 What are the most popular sizes and colors for different items?

# Most Popular Size By Differnt Items:
# Calculate the counts for each 'Item Purchased' and 'Size' combination
popular_size = df.groupby(['Item Purchased', 'Size']).size().reset_index(name='Count')

# Find the index of the maximum count for each 'Item Purchased'
max_counts_size_idx = popular_size.groupby('Item Purchased')['Count'].idxmax()

# Filter the DataFrame to get the rows with the maximum count for each 'Item Purchased'
max_counts = popular_size.loc[max_counts_size_idx]
print(max_counts)


# Most Popular Color By Different Items:
# Calculate the counts for each 'Item Purchased' and 'Color' combination
popular_color = df.groupby(['Item Purchased','Color']).size().reset_index(name='Count')

# Find the index of the maximum count for each 'Item Purchased'
max_counts_color_idx = popular_color.groupby('Item Purchased')['Count'].idxmax()

# Filter the DataFrame to get the rows with the maximum count for each 'Item Purchased'
max_counts = popular_color.loc[max_counts_color_idx]
print(max_counts)


# Q-9.2 Is there a relationship between size/color preferences and customer age or gender?

# Most size prefer by customer age:
# Calculate the count for each Age and Size combination
size_pre_by_age = df.groupby(['Age','Size']).size().reset_index(name='Count')

# Find the index of maximum count for each Age
count_idx = size_pre_by_age.groupby('Age')['Count'].idxmax()

# Filtering the rows with maximum count for each Age
max_counts = size_pre_by_age.loc[count_idx]
print(max_counts)

# Most color prefer by customer age:
# Calculate the count for each age and color combination
color_pre_by_age = df.groupby(['Age','Color']).size().reset_index(name='Count')

# Find the index of maximum count for each Age
count_idx = color_pre_by_age.groupby('Age')['Count'].idxmax()

# Filtering the rows with maximum count for each Age
max_counts = color_pre_by_age.loc[count_idx]
print(max_counts)


# Most size prefer by gender:
# Calculate the count for each Gender and Size combination
gender_pre_by_age = df.groupby(['Gender','Size']).size().reset_index(name='Count')

# Find the index of maximum count for each Gender
count_idx = gender_pre_by_age.groupby('Gender')['Count'].idxmax()

# Filtering the rows of maximum count for each gender
max_counts = gender_pre_by_age.loc[count_idx]
print(max_counts)

# Most color prefer by gender:
# Calculate the count for each Gender and Color combination
gender_pre_by_age = df.groupby(['Gender','Color']).size().reset_index(name='Count')

# Find the index of maximum count for each Gender
count_idx = gender_pre_by_age.groupby('Gender')['Count'].idxmax()

# Filtering the rows of maximum count for each gender
max_counts = gender_pre_by_age.loc[count_idx]
print(max_counts)

