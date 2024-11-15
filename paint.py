import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar


periods = 365

# 读取数据
data = pd.read_csv('data.dat', delim_whitespace=True, names=["date", "datetime", "length"])  # 读取存储了角度的 TXT 文件
len_data = len(data)
end_date = data.loc[len_data - 1, "date"]
date_range = pd.date_range(end=end_date, periods=periods)
df = pd.DataFrame({"date": date_range, "value": [0] * len(date_range)})

# 数据处理
i = 0
while i < len_data - 1:
    if data.loc[i, "date"] not in date_range:
        break
    length1 = data.loc[i, "length"]
    date = data.loc[i, "date"]
    day = df[df["date"] == data.loc[i, "date"]].index
    while i < len_data - 1:
        i += 1
        if data.loc[i, "date"] != date:
            length2 = data.loc[i, "length"]
            break
    if i == len_data - 1:
        length2 = data.loc[i, "length"]
    df.loc[day, "value"] = length2 - length1

# 提取年份、月份、星期几
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.weekday  # Monday=0, Sunday=6

# 计算从开始日期到当前日期的周序号
df["week_index"] = (((df["date"] - df["date"].min()).dt.days + df["day"][0]) // 7)

# 使用 pivot_table 将数据整理为 heatmap 格式
heatmap_data = df.pivot_table(index="day", columns="week_index", values="value", aggfunc=np.sum)

# 找出每个月的第一个周序号，用于在 x 轴上显示月份
month_changes = df.groupby(["year", "month"])["week_index"].min().sort_values()
month_labels = [calendar.month_abbr[month] for _, month in month_changes.index]
month_ticks = month_changes.values

# 绘图
plt.figure(figsize=(15, 2.22))
sns.heatmap(heatmap_data, cmap="Greens", linewidths=0.1, linecolor="gray", cbar=False, yticklabels=False)
#sns.heatmap(heatmap_data, cmap="Greens", linewidths=0.1, linecolor="gray", cbar=False, yticklabels=False, vmax=3500)

# 在 NaN 格子上画斜线
for (i, j), value in np.ndenumerate(heatmap_data.isna()):
    if value:  # 检查是否是 NaN
        #plt.fill([j, j + 1, j + 1, j], [i, i, i + 1, i + 1], color="lightgray", edgecolor="none")  # 填充浅灰色矩形
        plt.plot([j, j+1], [i, i+1], color="gray", lw=2)  # 绘制左上到右下的斜线

# 设置标签和格式
plt.yticks(ticks=np.arange(7) + 0.5, labels=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], rotation=0)
plt.xticks(ticks=month_ticks, labels=month_labels, rotation=30, ha="right", fontsize=10)
plt.title("GitHub-like Contribution Heatmap")

# 调整图形布局
plt.subplots_adjust(bottom=0.2)
plt.show()
