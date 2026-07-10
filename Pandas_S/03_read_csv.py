import pandas as pd

df =pd.read_csv("Pandas_S/nba.csv")

print(df)
"""to_string() 可以打印出完整的DataFrame,如果直接打印df,只会显示前5行和后5行中间使用省略号代替"""
print(df.to_string())
"""head()方法默认是打印前5行,也可以指定打印的行数"""
print(df.head(10))
"""tail()方法默认是打印后5行,也可以指定打印的行数"""
print(df.tail(10))
"""info()方法可以查看DataFrame的基本信息,包括行数、列数、每列的数据类型、非空值数量等"""
print(df.info())