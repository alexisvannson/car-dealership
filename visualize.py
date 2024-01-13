import matplotlib.pyplot as plt
import seaborn as sns


df = dataframes['Sheet1']

# This will turn 'Not Priced' into Not a number
# remove the dollar sign and commas from the 'Price' column
price_numeric = df['Price'].replace('[\$,]', '', regex=True).apply(pd.to_numeric, errors='coerce')

# Drop rows where 'Rating' or 'Price' is NaN
visual_df = df.dropna(subset=['Rating', 'Price'])

# Convert 'Rating' to numeric
visual_df['Rating'] = visual_df['Rating'].astype(float)

# Plot distribution of 'Rating'
plt.figure(figsize=(10, 5))
sns.histplot(visual_df['Rating'], bins=20, kde=True)
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Plot distribution of 'Price' after converting to float
plt.figure(figsize=(10, 5))
sns.histplot(price_numeric, bins=20, kde=True)
plt.title('Distribution of Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()