import matplotlib.pyplot as plt
import pandas as pd
date = pd.date_range('2022-01-01',periods=10)
values=[1,2,3,4,5,6,7,8,10,9]
plt.figure(figsize=(10,4))
plt.plot(date,values,color='blue',marker='o',linestyle='-')
plt.title("Series Time Data Visualization")
plt.xlabel("date")
plt.ylabel("values")
plt.grid(True)
plt.gcf().autofmt_xdate()
plt.show()
