# dev-2026-03

## 题目名称

Python 电商零售数据清洗：完成基础清洗并导出结果

## 这是一道什么题

这道题主要考查：

- Python 基础使用
- pandas 读取数据
- 基础数据清洗
- 文件导出
- 简单结果统计
- README 说明能力

本题不要求复杂数据分析，不要求画图，不要求机器学习。

重点是：

- 你能不能把一份真实但有脏数据的数据表洗干净
- 你能不能把结果导出来
- 你能不能简单说明你做了什么

---

## 数据集

本题使用的数据集链接：

- <https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci>

为了方便开始，本仓库额外提供了一个下载脚本，你可以用 `kagglehub` 自动下载数据。

---

## 如果这是模板仓库，你应该怎么开始

### 第一步：使用模板创建你自己的仓库
在 GitHub 页面点击：

- `Use this template`
- 创建你自己的新仓库

### 第二步：克隆到本地

```bash
git clone <你的仓库地址>
cd <你的仓库名>
```

### 第三步：创建虚拟环境（必须）

请使用 `venv` 创建虚拟环境。

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 第四步：安装依赖

```bash
pip install -r requirements.txt
```

### 第五步：下载数据

本仓库提供了下载脚本：

```bash
python scripts/download_data.py
```

这个脚本会尝试使用 `kagglehub` 下载数据集，并把文件复制到：

```text
data/
```

如果你第一次使用 Kaggle 相关工具，可能需要先配置自己的 Kaggle 访问环境。

### 第六步：修改 `main.py`

本题重点完成：

- `main.py`

---

## 你的任务

你需要完成以下内容。

### 1. 读取原始数据
使用 Python 读取 `data/` 目录中的原始数据文件。

### 2. 完成基础数据清洗
至少完成以下清洗任务：

- 删除完全重复的记录
- 删除 `Customer ID` 为空的记录
- 删除 `Quantity` 小于等于 0 的记录
- 删除 `Price` 小于等于 0 的记录
- 把 `InvoiceDate` 转成正确的日期时间格式

### 3. 导出清洗后的结果
请把清洗后的结果导出到 `output/` 目录，例如：

```text
output/cleaned_retail.csv
```

### 4. 输出基础清洗统计信息
请额外输出一份简单统计信息，例如：

- 原始数据总行数
- 清洗后数据总行数
- 删除了多少重复数据
- 删除了多少空客户数据
- 删除了多少无效数量或价格数据

你可以选择下面任意一种方式输出：

- 直接打印到终端
- 写到 `output/summary.txt`
- 写到 `output/summary.json`

---

## 运行要求

你的程序至少应该能通过类似下面的方式运行：

```bash
python main.py
```

---

## 提交要求

你需要提交：

1. 完整源码
2. `README.md`
3. 清洗后的结果文件
4. 基础统计结果

---

## 评分与验收说明

详细内容请查看：

- [评分细则（面向 agent）](./docs/scoring.md)
- [验收清单](./docs/checklist.md)
- [学生 README 模板](./docs/student-readme-template.md)

---

## 给候选人的说明

这道题不是考你做复杂分析，而是看你能不能把基础数据处理做对。

请优先保证：

- 先创建并使用虚拟环境
- 程序可以运行
- 数据能正确读取
- 清洗步骤基本完成
- 结果能正确导出
- README 能说明做了什么

如果你之前没有真正做过数据清洗，也没关系。你可以先完成最基础版本，再慢慢补统计信息。