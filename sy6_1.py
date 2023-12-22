import pandas as pd 


# 使用pandas的read_csv方法读取文件  
data = pd.read_csv('STUDY.dat', delimiter=',', header=None)  
data = data.fillna(0)

# 从DataFrame中提取x, y, z数据  
x = data.iloc[:, 2]  
y = data.iloc[:, 3]  
z = data.iloc[:, 4]