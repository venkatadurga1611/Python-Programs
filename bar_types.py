import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y1 = [2,4,6,8,10]
y2 = [10,8,6,4,2]
plt.figure(figsize=(10,6))
plt.subplot(2,2,1)
plt.plot(x,y1,color='blue',marker='o')
plt.title("Line Plot")
plt.subplot(2,2,2)
plt.scatter(x,y2,color='pink')
plt.title("Scatter Plot")
plt.subplot(2,2,3)
plt.bar(x,y1,color='yellow')
plt.title("Bar Chart")
plt.subplot(2,2,4)
plt.barh(x,y2,color='purple')
plt.title("Horizontal Bar chart")
