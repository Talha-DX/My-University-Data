# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])  
# print(arr)
# -----------------------
# import numpy as np
# arr = np.linspace(0, 10, 5)
# print(arr)
# -----------------------
# import numpy as np
# arr_zeros = np.zeros((3, 3))
# arr_ones = np.ones((2, 2))
# arr_full = np.full((3, 3), 5)

# print(arr_zeros)
# print(arr_ones)
# print(arr_full)
# -----------------------
# import numpy as np
# arr = np.random.rand(3, 3)
# print(arr)
# -----------------------
# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])

# print("Data Type:", arr.dtype)
# print("Shape:", arr.shape)
# print("Size:", arr.size)
# print("Dimensions:", arr.ndim)
# -----------------------
# import numpy as np
# arr = np.array([1, 2, 3])
# print("Addition:", arr + 5)
# print("Multiplication:", arr * 2)
# -----------------------
# import pandas as pd
# data = [['Ali', 22], ['Ayesha', 21], ['Usman', 23]]
# df = pd.DataFrame(data, columns=['Name', 'Age'])
# print(df)
# import pandas as pd
# data = {
#     'Name': ['Ali', 'Ayesha', 'Usman'],
#     'Age': [22, 21, 23],
#     'Grade': ['A', 'B', 'A']
# }
# df = pd.DataFrame(data)
# print(df)
# import pandas as pd
# df = pd.read_csv('students.csv')
# print(df.head())

# -------------------Matplotlib------------------------

# --------------1)Line Bar------------------------

# import matplotlib.pyplot as plt

# x = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
# y = [4000,7000,8000,7500,9000,10000,9500]

# plt.plot(x,y,marker = "o")
# plt.title("Daily Step Count")
# plt.xlabel("Days")
# plt.ylabel("Steps")
# plt.grid(True)
# plt.show()

# --------------2) Bar Chart------------------------

# import matplotlib.pyplot as plt
# x = ["Mon","Tue","Wed","Thu","Fri"]
# y = [40,60,10,20,50]

# plt.bar(x,y)

# plt.title("Item Sold Per Day")
# plt.xlabel("Day")
# plt.ylabel("NUmber of Items")
# plt.grid(False)
# plt.show()


# --------------3) Histogram------------------------

# import matplotlib.pyplot as plt
# scores = [45,34,78,82,12,90,45,21,45,67,87,43,18,92,41]

# plt.hist(scores, bins=8)
# plt.title("Score Distribution")
# plt.xlabel("Score Range")
# plt.ylabel("Frequency")
# plt.grid(False)
# plt.show()


# --------------4) Scatter plot------------------------

# import matplotlib.pyplot as plt
# x = [1,2,3,4,5,6,7,8]
# y = [30,20,45,12,43,87,32,43]

# plt.scatter(x,y)
# plt.title("Study Hours vs Test Score")
# plt.xlabel("Hours of Study")
# plt.ylabel("Score")
# plt.grid(True)
# plt.show()

# --------------5) Pie Chart------------------------

# import matplotlib.pyplot as plt

# companies = ["Company A","Company B","Company C","Company D","Company E"]
# market_score = [34,23,54,12,65]

# plt.pie(market_score, labels=companies, autopct='%1.1f%%',startangle=150,colors=['blue','orange','green','red','purple'])
# plt.title("Marktet Share of Tech Companies")
# plt.show()

# --------------6) Area PLot------------------------

# import matplotlib.pyplot as plt
# import pandas as pd

# data = {
#     'Month':['Jan','Feb','Mar','Apr','May'],
#     'Sales': [120,200,300,250,500]
# }
# df = pd.DataFrame(data)
# df.plot(x='Month',y='Sales',kind='area',color='yellow',alpha=0.5)
# plt.title("Cummulative Sales Over Time")
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.grid(False)
# plt.show()

# --------------3D plot------------------------
  
# import matplotlib.pyplot as plt 
# from mpl_toolkits.mplot3d import Axes3D 
# import pandas as pd 

# data = {
#     'Age': [23, 25, 30, 35, 40],
#     'Height': [150, 160, 170, 180, 190], 
#     'Weight': [50, 60, 70, 80, 90] 
# }

# df = pd.DataFrame(data)
# fig = plt.figure() 
# ax = fig.add_subplot(111, projection='3d') 
# ax.scatter(df['Age'], df['Height'], df['Weight'], color='red') 
# ax.set_xlabel('Age') 
# ax.set_ylabel('Height') 
# ax.set_zlabel('Weight')
# plt.title('3D Scatter Plot') 
# plt.show()

# -------------- Seaborn ------------------------

# -------------- 1)Bar Plot ---------------------

# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns

# data = {
#     'Subject':['Math','English','Science','Histroy','Computer'],
#     'Average_Score':[54,65,87,23,13]
# }
# df = pd.DataFrame(data)
# sns.barplot(x='Subject', y='Average_Score',data=df)
# plt.title("Average Score by Subject")
# plt.xlabel("Subject")
# plt.ylabel("Score")
# plt.show()

# -------------- 2) Line plot ---------------------

# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns

# sales_data = {
#     'Month':['Jan','Feb','Mar','Apr','May'],
#     'Revencue':[5000,7000,6500,8500,9000]
# }

# df = pd.DataFrame(sales_data)
# sns.lineplot(x='Month',y='Revenue',data=df,marker='o',color='green')
# plt.title("Monthly Revenue Trend")
# plt.xlabel("Subject")
# plt.ylabel("Revenue{$}")
# plt.grid(True)
# plt.show()

# -----------------------------------------------------

# import matplotlib.pyplot as plt
# x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# y = [5, 6, 8, 7, 9, 10, 8]
# plt.plot(x, y, marker='o')
# plt.title("Weekly Water Intake (in glasses)")
# plt.xlabel("Day of the Week")
# plt.ylabel("Glasses of Water")
# plt.show()

# ------------------------------------------------------

# import matplotlib.pyplot as plt
# x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# y = [45, 60, 50, 70, 85, 95, 90]
# plt.bar(x, y)
# plt.title("Weekly Coffee Sales")
# plt.xlabel("Day of the Week")
# plt.ylabel("Number of Coffees Sold")
# plt.show()

# ------------------------------------------------------

# import matplotlib.pyplot as plt
# sleep_hours = [5, 6, 7, 8, 5, 6, 7, 7, 8, 9, 5, 6, 8, 9, 7]
# plt.hist(sleep_hours, bins=5, edgecolor='black')
# plt.title("Distribution of Sleeping Hours")
# plt.xlabel("Hours of Sleep")
# plt.ylabel("Number of Students")
# plt.show()

# ------------------------------------------------------

# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5, 6, 7, 8]  # Hours on social media
# y = [95, 90, 85, 80, 75, 70, 60, 55]  # Exam scores
# plt.scatter(x, y)
# plt.title("Social Media Usage vs Exam Scores")
# plt.xlabel("Hours Spent on Social Media")
# plt.ylabel("Exam Scores")
# plt.show()

# -----------------------------------------------------

# import matplotlib.pyplot as plt
# categories = ['Food', 'Rent', 'Transport', 'Shopping', 'Savings']
# expenses = [25, 35, 15, 10, 15]
# plt.pie(expenses, labels=categories, autopct='%1.1f%%')
# plt.title("Monthly Expenses Breakdown")
# plt.show()

# -----------------------------------------------------

# from collections import deque

# graph = {
#     0: [1, 3, 4],
#     1: [2],
#     2: [],
#     3: [5],
#     4: [5],
#     5: []
# }

# def bfs(start):
#     visited = []
#     queue = deque([start])

#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             visited.append(node)
#             queue.extend(graph[node])
#     return visited

# print("BFS:", bfs(0))


# ------------------------- Task 2 ------------------------

graph = {
    1: [2, 7],
    2: [3, 6],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: [8, 9],
    8: [],
    9: [10, 11],
    10: [],
    11: []
}

def dfs(start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(neighbor, visited)
    return visited

print("DFS:", dfs(1))
