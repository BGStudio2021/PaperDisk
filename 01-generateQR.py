import qrcode
from PIL import Image
import os


def generate_qrcode(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)


def split_text(text, max_chars):
    chunks = []
    for i in range(0, len(text), max_chars):
        chunks.append(text[i : i + max_chars])
    return chunks


def main():
    # 确保temp-qr目录存在
    if not os.path.exists("temp-qr"):
        os.makedirs("temp-qr")

    # 读取txt文件内容
    with open("data.txt", "r", encoding="utf-8") as file:
        content = file.read()

    # 分片文本
    max_qr_chars = 2048  # 减少分片大小以避免超出容量
    text_chunks = split_text(content, max_qr_chars)

    # 生成二维码
    for i, chunk in enumerate(text_chunks):
        file_name = os.path.join("temp-qr", f"qr_code_{i}.png")
        generate_qrcode(chunk, file_name)
        print(
            f"\r正在生成 QR 码 (" + str(i + 1) + " / " + str(len(text_chunks)) + ")",
            end="",
        )
    print("")


if __name__ == "__main__":
    main()
