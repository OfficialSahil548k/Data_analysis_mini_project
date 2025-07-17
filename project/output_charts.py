import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np
import sales_analysis as sa

data = pd.read_csv(r"D:\analysis\newOne\project\Analysed_superstore.csv")
sa.product_sales.head(10).plot(kind='bar', figsize=(10, 5), title='Top 10 Products by Sales')
plt.show()

sa.region_sales.plot(kind='bar', color='orange', title='Sales by Region')
plt.show()

sa.monthly_sales.plot(figsize=(12,6), title='Monthly Sales Trend', marker='o')
plt.show()