from pathlib import Path
import shutil
import kagglehub

DATASET = "mashlyn/online-retail-ii-uci"
TARGET_DIR = Path("data")


def main():
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    downloaded_path = Path(kagglehub.dataset_download(DATASET))

    print(f"数据已下载到缓存目录: {downloaded_path}")

    copied = 0
    for item in downloaded_path.rglob("*"):
        if item.is_file():
            target = TARGET_DIR / item.name
            shutil.copy2(item, target)
            copied += 1

    print(f"已复制 {copied} 个文件到 {TARGET_DIR.resolve()}")
    print("现在你可以继续编写并运行 main.py 进行数据清洗。")


if __name__ == "__main__":
    main()
