
# importing a necessary libraries:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# initializing a df as a DataFrame
df = pd.DataFrame()

# Read a CSV File through a Pandas
df = pd.read_csv('shopping_trends_updated.csv',encoding='unicode escape')
print(df.head())

# Info shows the data columns, data types and null value
print(df.info())

# Printing columns of dataframe
print(df.columns)


# EXPLORATORY DATA ANALYSIS:

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
location = df.groupby(['Location'],as_index=False).size()
print(location)

# Plotting the result

sns.set(rc={'figure.figsize':(12,8)})
ax = sns.countplot(x='Location',data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.xticks(rotation='vertical')
plt.title('Distribution of Customers by Location')
plt.ylim(50,None)
plt.ylabel('Count')
plt.tight_layout()
plt.show()


# ***Most customers fall within the age range of 25 to 60, and the majority of customers are men.
# Additionally, cities like Montana, California, Illinois, and Idaho have a higher number of customers.***





# 2. Purchase Analysis:

# Q-2.1 What are the most purchased items and categories?

# Count the most purchased items and categories by grouping
most_purchase = df.groupby(['Category','Item Purchased']).size().reset_index(name='Count').sort_values(by='Count',ascending=False)
print(most_purchase)

# Plotting the result
sns.set(rc={'figure.figsize':(12,8)})
sns.barplot(data=most_purchase, x='Item Purchased',y='Count', hue='Category')
plt.xticks(rotation = 'vertical')
plt.title('Count of Items Purchased in Each Category')
plt.tight_layout()
plt.legend(loc='upper right')
plt.show()

# Print the most top 10 purchased items and categories:
new_df = df.groupby(['Category','Item Purchased']).size().sort_values(ascending=False)
top_10_items_and_category = new_df[:10]

print('Top 10 Most Purchased Items and Categories: \n')
for category, item in top_10_items_and_category.index:
    print(f'Category: {category}, Items: {item}, Count: {new_df[(category,item)]}')


# Q-2.2 How does the purchase amount vary across different items and categories?

# Count the sum of Purchase Amount by Different Items & Category
purchase_amount = df.groupby(['Category','Item Purchased'],as_index=False)['Purchase Amount (USD)'].sum()
print(purchase_amount)

sns.set(rc={'figure.figsize':(12,8)})
sns.barplot(data=purchase_amount, x='Item Purchased', y='Purchase Amount (USD)',hue='Category')
plt.xticks(rotation = 'vertical')
plt.title('Amount of purchase by different items')
plt.tight_layout()
plt.ylim(5000,None)
plt.legend(loc='upper right')
plt.show()

# Calculate the Distribution of Purchase Amount by Different Category
amount_by_categories = df.groupby(['Category'])['Purchase Amount (USD)'].sum()
print(amount_by_categories)

# Plotting the result
plt.figure(figsize=(10,6))
plt.pie(amount_by_categories, labels=amount_by_categories.index, autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Amount Purchase by Different Categories')
plt.axis('equal')
plt.show()

# Q-2.3 Are there any seasonal trends in purchasing behavior?

# Calculate the Purchase amount on Seasonal Trends
seasonal_trends = df.groupby(['Season'],as_index=False)['Purchase Amount (USD)'].sum()
print(seasonal_trends)

# Plotting the result
sns.set(rc={'figure.figsize':(10,6)})
ax = sns.barplot(data=seasonal_trends, x='Season', y='Purchase Amount (USD)')

for bars in ax.containers:
    ax.bar_label(bars)

plt.ylim(40000,None)
plt.title('Amount of Purchase by Seasons')
plt.tight_layout()
plt.show()

# ***Top-selling items include pants, blouses, and jewelry, with clothing & accessories dominating sales.
# Spring and fall emerge as peak seasons for purchases.***





# 3. Customer Behavior:

# Q-3.1 How frequently do customers make purchases?

# Count the frequency of the purchases
freq_of_purchase = df.groupby(['Frequency of Purchases'],as_index=False).size()
print(freq_of_purchase)

sns.set(rc={'figure.figsize':(10,6)})
ax = sns.countplot(data=df,x='Frequency of Purchases')

for bars in ax.containers:
    ax.bar_label(bars)

plt.ylim(500,None)
plt.title('Frequency of the purchases by customers')
plt.ylabel('Count')
plt.show()


# Q-3.2 Is there a correlation between the frequency of purchases and age?

freq_of_purchase_by_age = df.groupby(['Age'],as_index=False)['Purchase Amount (USD)'].sum()
print(freq_of_purchase_by_age)

sns.set(rc={'figure.figsize':(12,8)})
sns.jointplot(x='Age',y='Purchase Amount (USD)',data=freq_of_purchase_by_age)
plt.show()

# Q-3.3 Do customers who use promo codes tend to make larger purchases?

count_promo_user = df.groupby('Promo Code Used').size()
print(count_promo_user)

share_of_promo_user_in_purchase = df.groupby('Promo Code Used')['Purchase Amount (USD)'].sum()
print(share_of_promo_user_in_purchase)

share_of_promo_user_in_purchase.index = ['Non-Promo Code User', 'Promo Code User']

plt.figure(figsize=(10,8))
plt.pie(share_of_promo_user_in_purchase,autopct='%1.1f%%',labels=share_of_promo_user_in_purchase.index,startangle=90)
plt.title('Percentage of Total Purchased Amount by Promo-Non Promo User')
plt.axis('equal')
plt.show()


# ***Most customers prefer making annual or quarterly purchases, typically spending between 3800 to 4800.
# Non-promo code users outnumber those using promo codes.***






# 4. Product and Review Analysis:

# Q-4.1: What is the average review rating for different items and categories?

# Average Review Rating by Different Items & Category
review_rating_by_items = df.groupby(['Item Purchased','Category'],as_index=False)['Review Rating'].mean()
print(review_rating_by_items)

# Plotting a result with seaborn barplot
sns.set(rc={'figure.figsize':(10,6)})
sns.barplot(x='Item Purchased',y='Review Rating',data=review_rating_by_items, hue='Category')
plt.title('Average of Review Ratings by Different Items')
plt.ylim(3.0,None)
plt.ylabel('Average value of Ratings')
plt.xticks(rotation='vertical')
plt.tight_layout()
plt.show()


# Q-4.2: Is there a relationship between the review rating and the purchase amount?

grouped_data_sum = df.groupby(['Review Rating'],as_index=False)['Purchase Amount (USD)'].sum()
print(grouped_data_sum)

sns.set(rc={'figure.figsize':(10,8)})
sns.barplot(x='Review Rating',y='Purchase Amount (USD)',data=grouped_data_sum, palette='viridis')
plt.title('Relation between Review Rating and Purchase Amount')
plt.ylim(3000,None)
plt.tight_layout()
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
color_review_rating = df.groupby(['Color'],as_index=False)['Review Rating'].mean().sort_values(by='Review Rating',ascending=False)

# Print the TOP-5 Colors by Review Ratings
print(color_review_rating.head(5))

# Plotting the result
sns.set(rc={'figure.figsize':(10,8)})
sns.barplot(x='Color',y='Review Rating',data=color_review_rating, palette='viridis')
plt.title('Popular Colors by Review Rating')
plt.xticks(rotation='vertical')
plt.xlabel('Colors')
plt.ylabel('Review Rating')
plt.ylim(3.0,None)
plt.tight_layout()
plt.show()

# ***Gloves, sandals, and boots receive higher review ratings. Customers mostly spend within the review rating range of 3.5 to 4.9,
# XL and S sizes are popular, along with colors like gray, yellow, magenta, black, and orange, as per review ratings.***





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
discount = df.groupby(['Discount Applied'],as_index=False)['Purchase Amount (USD)'].sum()
print(discount)

sns.set(rc={'figure.figsize':(10,6)})
sns.barplot(data=discount,x='Discount Applied',y='Purchase Amount (USD)')
plt.title("Distribution of purchasing amount by Discount and Non-Discount User")
plt.show()


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

# *** Only 27% customers are using subscription, less customers are using discounts, credit card is most popular payment method.***





# 6.Geographical Insights:

# Q-6.1 Are there any location-specific trends in purchasing behavior?

purchase_by_loc = df.groupby(['Location'],as_index=False)['Purchase Amount (USD)'].sum()
print(purchase_by_loc)

sns.set(rc={'figure.figsize':(10,8)})
sns.barplot(x='Location',y='Purchase Amount (USD)',data=purchase_by_loc)
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


def get_popular_shipping_type_by_loc(df):
    shipping_type_by_loc = df.groupby(['Location', 'Shipping Type']).size()
    max_shipping_type_by_loc = shipping_type_by_loc.unstack(fill_value=0).idxmax(axis=1)
    for location, max_type in max_shipping_type_by_loc.items():
        max_count = shipping_type_by_loc.loc[(location, max_type)]
        print(f"{location} - {max_type} {max_count}")

result = get_popular_shipping_type_by_loc(df.copy())

# ***Montana, California, Illinois, Idaho, and Nevada States are top-selling states. Each city has its unique shipping type.



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

repeat_item = df.groupby(['Item Purchased']).size().reset_index(name='Count')

#Plotting result
sns.set(rc={'figure.figsize':(12,8)})
ax = sns.barplot(x='Item Purchased', y='Count', data=repeat_item, palette='viridis')
for bars in ax.containers:
    ax.bar_label(bars)
plt.title('Count of Items Purchased')
plt.xlabel('Item Purchased')
plt.ylabel('Count')
plt.xticks(rotation=90)  # Rotating x-axis labels for better readability
plt.ylim(100,None)
plt.tight_layout()
plt.show()


# *** Blouse, Jewelry, Pants, Shirts are most repeated purchased items by customers. ***



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


# *** Paypal and Credit card are most used payment method by customers.



# 9. Size and Color Preferences:

# Q-9.1 What are the most popular sizes and colors for different items?

# Most Popular Size By Different Items:
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


# ***The most popular size across genders is M. Yellow is the preferred color for females, while men tend to favor silver.***


'''
*** PROJECT SUMMARY ***

The project offers a comprehensive view of customer behavior and preferences across various dimensions:

- Demographics: Majority of customers, primarily men aged 25 to 60.
- Top-selling Items: Clothing and accessories, especially pants, blouses, and jewelry.
- Seasonal Trends: Spring and fall emerge as peak purchase seasons.
- Purchase Patterns: Customers prefer spending around 3800 to 4800, mostly annually or quarterly.
- Promotional Usage: Non-promo code users outnumber promo code users.
- Product Reviews: Gloves, sandals, and boots receive higher ratings within the 3.5 to 4.9 range.
- Preferences by Size and Color: Sizes M, XL, and S are popular, with females favoring yellow and men preferring silver.
- Payment Methods: Credit cards are the most used, while subscriptions and discounts see lower usage.
- Geographical Insights: Montana, California, Illinois, Idaho, and Nevada are top-selling states, each with unique shipping methods.
'''
