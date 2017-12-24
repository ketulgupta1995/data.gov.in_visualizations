import matplotlib.pyplot as plt
import data_ops

df=data_ops.make_data_frame()
plt.figure()

# print(df.columns)
df[data_ops.col_list[1:]]=df[data_ops.col_list[1:]].apply(data_ops.pd.to_numeric, args=('ignore',))
print(data_ops.pd.isnull(df[data_ops.col_list[1]]))
print(df[data_ops.col_list[1]].tolist())
print(df.info())

df.plot(kind='pie',x='Name of City',y='All Accidents - 2011')
plt.show();
# plt.plot()
