import pandas as pd

df = pd.read_csv(r"D:\analysis\newOne\project\superstore.csv")
#print(df.head(10))
#print(df.info())     shows columns details
#print(df.describe())  shows count mean etc.

df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True, errors='coerce')# or dayfirst=True
# print(df.isnull().sum())
# print(df['Postal Code'].count())
df['Postal Code'] = df['Postal Code'].dropna()
# print(df['Postal Code'].count())

product_sales = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False)
print(product_sales)
#print(product_sales)

region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
#print(region_sales)

df['Months'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Months')['Sales'].sum()
# print(monthly_sales)

# csv_path = r"D:\analysis\newOne\project\Analysed_superstore.csv"
# df.to_csv(csv_path)

