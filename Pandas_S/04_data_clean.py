import pandas as pd

"""pandas只默认将NAN和N/A识别为缺失值,如果数据中有其他的缺失值表示,需要使用na_values参数指定"""
missing_values = ["n/a", "na", "--"]
data=pd.read_csv("Pandas_S/property-data.csv",na_values=missing_values)

print(data)

"""这一列中有一个数据使用的是na表示缺失，没有missing_values指定的时候，isnull少检测了一个"""
print(data["NUM_BEDROOMS"])
print(data["NUM_BEDROOMS"].isnull())

"""dropna()方法可以删除缺失值所在的行,如果想删除缺失值所在的列,可以使用axis=1参数"""
new_df=data.dropna()
print(new_df.to_string())

"""inplace=True参数表示在原来的DataFrame上进行修改,不需要再赋值给一个新的变量"""
data.dropna(inplace=True)
print(data.to_string())

"""fillna()方法可以用指定的值替换缺失值,也可以使用前一个或后一个非缺失值进行填充"""

df = pd.read_csv('Pandas_S/property-data.csv')
num_cols=df.select_dtypes(include=['number']).columns
df[num_cols]=df[num_cols].fillna(123456)
str_cols=df.select_dtypes(include=['string']).columns
df[str_cols]=df[str_cols].fillna('123456')
print(df.to_string())
print(df.dtypes)


df = pd.read_csv('Pandas_S/property-data.csv')
"""mean()方法可以计算数值型列的平均值,median()方法可以计算数值型列的中位数,mode()方法可以计算数值型列的众数"""
df["ST_NUM"] = df["ST_NUM"].fillna(df["ST_NUM"].mean())
print(df.to_string())

df = pd.read_csv('Pandas_S/property-data.csv')
df["ST_NUM"] = df["ST_NUM"].fillna(df["ST_NUM"].median())
print(df.to_string())

df = pd.read_csv('Pandas_S/property-data.csv')
df["ST_NUM"] = df["ST_NUM"].fillna(df["ST_NUM"].mode()[0])
print(df["ST_NUM"].mode())
print(df.to_string())



person = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]  
}
df = pd.DataFrame(person)
"""duplicated()方法可以判断每一行是否是重复的,返回一个布尔值的Series,True表示重复,False表示不重复"""
print(df.duplicated())
df.drop_duplicates(inplace=True)
print(df.to_string())


data = {'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)
print(df.to_string())
"""独热编码"""
df_encoded = pd.get_dummies(df, columns=['City'])
print(df_encoded.to_string())

from sklearn.preprocessing import StandardScaler

data = {'Age': [25, 30, 35, 40, 45],
        'Salary': [50000, 60000, 70000, 80000, 90000]}
df = pd.DataFrame(data)

scaler = StandardScaler()
df_scaled =scaler.fit_transform(df)
print(df.to_string())

print(df.iloc[0:3,0])