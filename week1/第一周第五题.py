import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

file_path = r'C:\Users\黄小悠\Desktop\附件.xlsx'
df = pd.read_excel(file_path)

fleets = df['车队编码'].unique()

for fleet in fleets:
    fleet_data = df[df['车队编码'] == fleet]

    plt.figure(figsize=(10, 6))
    plt.scatter(fleet_data['在途时长'], fleet_data['自有变动成本'], label='自有变动成本')
    plt.scatter(fleet_data['在途时长'], fleet_data['外部承运商成本'], label='外部承运商成本')

    plt.xlabel('在途时长')
    plt.ylabel('成本')
    plt.title(f'{fleet} 成本分析')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

stats = df.describe().T[['max', 'min', 'mean', '50%']]
stats.columns = ['最大值', '最小值', '平均值', '中位数']
print("各数据统计量: ")
print(stats)

df['总成本'] = df['自有变动成本'] + df['外部承运商成本']
df['时均成本'] = df['总成本'] / df['在途时长']

plt.figure(figsize=(10, 6))
plt.bar(df['车队编码'].unique(), df.groupby('车队编码')['时均成本'].min())
plt.xlabel('车队编码')
plt.ylabel('最佳时均成本')
plt.title('各车队最佳时均成本对比')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()