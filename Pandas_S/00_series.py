import pandas as pd

series=pd.Series([1,2,3,4,5],name="A")

#print(series)

# 自定义设置索引

custom_index=['a','b','c','d','e']
series=pd.Series([1,2,3,4,5],name="A",index=custom_index)
#print(series)

#print(series['a'])  # 通过索引获取值

dict_data={'a':1,'b':2,'c':3,'d':4,'e':5}
series=pd.Series(dict_data,name="A")
#print(series)


data = [1, 2, 3, 4, 5, 6]
index = ['a', 'b', 'c', 'd', 'e', 'f']
s = pd.Series(data, index=index)

print(F"索引: {s.index}")
print(F"数据: {s.values}")
print(F"数据类型: {s.dtype}")
print(f"前两行数据：{s.head(2)}")

s_doubled=s.map(lambda x: x*2)
print(f"数据翻倍: {s_doubled}")

cumsum_series = s.cumsum()
print(f"累积和: {cumsum_series}")
print(f"查找缺失值: {s.isnull()}")
soted_series = s.sort_values(ascending=False)
print(f"排序后的数据: {soted_series}")