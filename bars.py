import matplotlib.pyplot as plt
Months = ['Jan','Feb','March','April','May','june','July']
sales = [1200,1300,400,200,1400,1500,1600]
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(Months,sales,color='blue',marker='o')
plt.title("Monthly sales Trend")
plt.subplot(1,2,2)
plt.bar(Months,sales,color='yellow')
