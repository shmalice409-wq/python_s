import pandas as pd

data =[['Google', 10], ['Runoob', 12], ['Wiki', 13]]

df =pd.DataFrame(data,columns=["Site", "Age"])

# 使用astype设置每列的数据类型
df["Site"]=df['Site'].astype(str)
df["Age"]=df['Age'].astype(float)
print(df)
print("="*20)

data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}

df = pd.DataFrame(data)

print (df)
print("="*20)

#使用字典创建，字典中要包含列名
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

df = pd.DataFrame(data)

print (df)
print("="*20)

data={
    "name":["Tom", "Jack", "Steve", "Ricky"],
    "age":[28, 34, 29, 42]
}

df = pd.DataFrame(data)

print(f"First row:\n{df.loc[0]}\n")#这里返回的是一个series数据结构
print(f"First two rows:\n{df.loc[0:1]}\n")#这里返回的是dataframe的数据结构


# 创建 DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

print(f"查看前两行数据:\n{df.head(2)}\n")
print(f"查看基本信息:\n{df.info()}\n")
print(f"查看描述性统计信息:\n{df.describe()}\n")
df_sorted = df.sort_values(by='Age', ascending=False)
print(f"按年龄降序排序:\n{df_sorted}\n")
print(f"打印指定列：\n{df[['Name', 'Age']]}\n")
print(f"计算分组统计信息:\n{df.groupby('City')['Age'].mean()}\n")
df['Age'] =df['Age'].fillna(30)
df.to_csv('output.csv', index=False)