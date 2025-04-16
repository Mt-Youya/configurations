import pandas as pd

# 使用二维列表结构组织数据，每行对应一条记录
data = [
]

# 创建DataFrame时指定列名
df = pd.DataFrame(data[1:], columns=data[0])

# 导出Excel时保留电话号码的完整格式
df.to_excel("text_to_excel.xlsx", index=False)