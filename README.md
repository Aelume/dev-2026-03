# Python 电商零售数据清洗

## 项目简介

这个项目使用 Python 和 pandas 对 Online Retail II 数据集做基础清洗，清理掉明显无效的数据后导出结果文件，并生成一份简单的统计报告。

## 实现内容

- 读取原始数据（`scripts/data/online_retail_II.csv`）
- 删除完全重复的记录
- 删除 `Customer ID` 为空的记录
- 删除 `Quantity <= 0` 的记录
- 删除 `Price <= 0` 的记录
- 将 `InvoiceDate` 转换为日期时间格式
- 导出清洗后的结果到 `output/cleaned_retail.csv`
- 输出统计信息到终端、`output/summary.json` 和 `output/summary.txt`

## 实现说明

### 1. 数据读取

使用 `pandas.read_csv()` 读取 `scripts/data/online_retail_II.csv`。

### 2. 数据清洗

按顺序执行以下清洗步骤：

1. **删除重复记录** — 使用 `drop_duplicates()` 删除完全相同的行
2. **删除空客户** — 使用 `dropna(subset=["Customer ID"])` 删除 Customer ID 为空的记录
3. **删除无效数量** — 过滤掉 `Quantity <= 0` 的记录（退货、取消等）
4. **删除无效价格** — 过滤掉 `Price <= 0` 的记录
5. **日期格式转换** — 使用 `pd.to_datetime()` 将 InvoiceDate 转为标准日期时间类型

每一步都记录了删除的行数，用于统计报告。

### 3. 导出结果

清洗后的数据导出到 `output/cleaned_retail.csv`，统计信息同时写入 `summary.json` 和 `summary.txt`。

### 4. 统计信息

统计结果通过三种方式输出：
- 终端打印
- `output/summary.json`（结构化数据）
- `output/summary.txt`（可读文本）

### 本地运行结果

以下结果基于当前仓库中的 `scripts/data/online_retail_II.csv`：

| 指标 | 数值 |
|------|------|
| 原始数据总行数 | 1,067,371 |
| 删除重复记录数 | 34,335 |
| 删除空 Customer ID 记录数 | 235,151 |
| 删除 Quantity<=0 记录数 | 18,390 |
| 删除 Price<=0 记录数 | 70 |
| 清洗后数据总行数 | 779,425 |
| 总共删除记录数 | 287,946 |

## 运行方式

1. 创建并激活虚拟环境（下面示例使用 conda）：

```bash
conda create -n dev-2026-03 python=3.12
conda activate dev-2026-03
```

2. 安装依赖：

```bash
pip install -r requirements.txt
```

3. 准备数据（运行下载脚本）：

```bash
python scripts/download_data.py
```

4. 运行程序：

```bash
python main.py
```

程序运行后会在终端输出统计信息，并在 `output/` 目录下生成结果文件。

## 项目结构

```
.
├── main.py                # 主程序：数据清洗逻辑
├── requirements.txt       # 依赖列表
├── README.md              # 本说明文件
├── output/                # 输出目录
│   ├── cleaned_retail.csv # 清洗后的数据
│   ├── summary.json       # 统计信息（JSON）
│   └── summary.txt        # 统计信息（文本）
└── scripts/               # 辅助脚本
    ├── download_data.py   # 数据下载脚本
    └── data/              # 原始数据目录
        └── online_retail_II.csv
```
