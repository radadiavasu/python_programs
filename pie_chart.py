import matplotlib.pyplot as plt
 
A=['eat', 'movie', 'study', 'play','daily_work','sleep']
T=[2,4,6,7,8,9]
  
plt.pie(T, labels=A,autopct= '%1.1f%%')
plt.title('Activity Chart.')
plt.show()