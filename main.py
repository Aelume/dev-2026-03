import json
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "scripts" / "data"
OUTPUT_DIR = BASE_DIR / "output"


def display_path(path):
    """将路径格式化为相对仓库根目录的显示形式。"""
    return path.relative_to(BASE_DIR).as_posix()


def load_data(data_dir=DATA_DIR):
    """读取 data/ 目录下的 CSV 数据文件。"""
    csv_path = Path(data_dir) / "online_retail_II.csv"
    if not csv_path.exists():
        raise FileNotFoundError(f"数据文件不存在：{csv_path}")
    df = pd.read_csv(csv_path)
    return df


def clean_data(df):
    stats = {}
    total_rows = len(df)
    stats["原始数据总行数"] = total_rows

    # 1. 删除完全重复的记录
    before = len(df)
    df = df.drop_duplicates()
    duplicates_removed = before - len(df)
    stats["删除重复记录数"] = duplicates_removed

    # 2. 删除 Customer ID 为空的记录
    before = len(df)
    df = df.dropna(subset=["Customer ID"])
    empty_customer_removed = before - len(df)
    stats["删除空Customer ID记录数"] = empty_customer_removed

    # 3. 删除 Quantity <= 0 的记录
    before = len(df)
    df = df[df["Quantity"] > 0]
    invalid_quantity_removed = before - len(df)
    stats["删除Quantity<=0记录数"] = invalid_quantity_removed

    # 4. 删除 Price <= 0 的记录
    before = len(df)
    df = df[df["Price"] > 0]
    invalid_price_removed = before - len(df)
    stats["删除Price<=0记录数"] = invalid_price_removed

    # 5. 把 InvoiceDate 转成日期时间格式
    df = df.copy()
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    stats["清洗后数据总行数"] = len(df)
    stats["总共删除记录数"] = total_rows - len(df)

    return df, stats


def export_results(df, stats, output_dir=OUTPUT_DIR):
    """将清洗后的数据和统计信息导出到 output/ 目录。"""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 导出清洗后的 CSV
    cleaned_csv_path = output_dir / "cleaned_retail.csv"
    df.to_csv(cleaned_csv_path, index=False)
    print(f"清洗后数据已导出到：{display_path(cleaned_csv_path)}")

    # 导出统计信息到 summary.json
    summary_json_path = output_dir / "summary.json"
    with open(summary_json_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    print(f"统计信息已导出到：{display_path(summary_json_path)}")

    # 同时导出一份 summary.txt 便于查看
    summary_txt_path = output_dir / "summary.txt"
    with open(summary_txt_path, "w", encoding="utf-8") as f:
        f.write("===== 数据清洗统计报告 =====\n\n")
        for key, value in stats.items():
            f.write(f"{key}：{value}\n")
    print(f"统计信息已导出到：{display_path(summary_txt_path)}")


def print_stats(stats):
    """将统计信息打印到终端。"""
    print("\n===== 数据清洗统计报告 =====\n")
    for key, value in stats.items():
        print(f"  {key}：{value}")
    print()


def main():
    # 读取数据
    print("正在读取数据...")
    df = load_data()
    print(f"数据读取完成，共 {len(df)} 行。")

    # 数据清洗
    print("正在进行数据清洗...")
    df_cleaned, stats = clean_data(df)
    print("数据清洗完成。")

    # 打印统计信息
    print_stats(stats)

    # 导出结果
    print("正在导出结果...")
    export_results(df_cleaned, stats)
    print("\n所有任务完成！")


if __name__ == "__main__":
    main()
