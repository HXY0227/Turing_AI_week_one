import pandas as pd
import numpy as np
random_array = np.random.random(5000).reshape(1000, 5)
df = pd.DataFrame(random_array, columns=['a', 'b', 'c', 'd', 'e'])
print("生成的DataFrame:")
print(df)
column_sums = df.sum()
min_column = column_sums.idxmin()
print(f"\n各列的和：")
print(column_sums)
print(f"列和最小的列名： {min_column}")
