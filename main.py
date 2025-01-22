import os
import base64


def delete_files(directory):
    file_list = os.listdir(directory)
    for file in file_list:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            os.remove(file_path)


# 指定要转换的目录
directory = "sources"

print("正在初始化......")
# 确保sources和output目录存在
if not os.path.exists("output"):
    os.makedirs("output")
if not os.path.exists("sources"):
    os.makedirs("sources")
# 清理临时文件
if os.path.exists("temp-qr"):
    delete_files("./temp-qr")

if len(os.listdir(directory)) == 0:
    print("请将要处理的文件放在“sources”目录下")
    exit()
count = 1
# 遍历目录中的所有文件
for filename in os.listdir(directory):
    # 构建完整的文件路径
    filepath = os.path.join(directory, filename)

    # 确保是文件而不是目录
    if os.path.isfile(filepath):
        # 读取文件内容
        with open(filepath, "rb") as file:
            file_content = file.read()

        # 将文件内容转换为base64
        base64_content = base64.b64encode(file_content).decode("utf-8")

        # 构建新的文件名（添加.txt后缀）
        new_filename = "data.txt"

        # 保存base64编码的内容到新文件
        with open(new_filename, "w") as new_file:
            new_file.write(base64_content)
        print(
            "正在处理文件 ("
            + str(count)
            + " / "
            + str(len(os.listdir(directory)))
            + f"): {filename}"
        )
        # 打开文件，并以 w 模式写入内容
        file = open("fileName.txt", "w", encoding="utf-8")
        # 写入内容到文件
        file.write(filename)
        # 关闭文件
        file.close()
        os.system("python ./01-generateQR.py")
        os.system("python ./02-generatePDF.py")
        delete_files("./temp-qr")
        print("正在清理......")
        count += 1

os.rmdir("./temp-qr")
os.remove("./fileName.txt")
os.remove("./data.txt")
print("已将处理后的文件存储在“output”目录下")
