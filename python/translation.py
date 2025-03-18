import pandas as pd
import json
import os

# 获取桌面路径（Windows系统可能是 'C:\\Users\\用户名\\Desktop'）
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Excel 文件路径，请根据实际文件名修改
excel_file = os.path.join(desktop_path, "顺欣达客户端翻译内容.xlsm")

# 读取 Excel 文件中所有的 Sheet，返回一个字典，键为 sheet 名称，值为对应的 DataFrame
xls = pd.read_excel(excel_file, sheet_name=None)

# 用于存储所有 Sheet 转换后的数据
result_all = {}

# 遍历所有 Sheet
for sheet_name, df in xls.items():
    sheet_result = {}
    # 遍历每一行数据
    for index, row in df.iterrows():
        # 假设第二列为中文，第三列为英文（注意：DataFrame 的列索引从 0 开始）
        key = row.iloc[1]
        value = row.iloc[2]
        sheet_result[key] = value
    # 将当前 Sheet 的结果存入总字典中
    result_all[sheet_name] = sheet_result

# 保存所有 Sheet 的数据到 JSON 文件（中文内容正常显示）
json_file = os.path.join(desktop_path, "translate.json")
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(result_all, f, ensure_ascii=False, indent=4)

print("JSON 文件已保存到：", json_file)
