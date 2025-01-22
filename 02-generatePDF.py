from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# 注册字体
pdfmetrics.registerFont(TTFont("MSYaHei", "./MSYaHei.ttf"))

# A4纸尺寸
a4_width, a4_height = A4

# 每张图片的尺寸
img_width = a4_width / 4
img_height = a4_width / 4

# 计算总共有多少张图片
total_images = len(
    [
        name
        for name in os.listdir("./temp-qr")
        if name.startswith("qr_code_") and name.endswith(".png")
    ]
)

# 计算需要多少页PDF
total_pages = (total_images - 1) // 20 + 1

# 读取文件名
with open("fileName.txt", "r", encoding="utf-8") as file:
    fileName = file.read()

# 创建PDF
c = canvas.Canvas("./output/" + fileName + ".pdf", pagesize=A4)
PAGE_WIDTH = c._pagesize[0]
PAGE_HEIGHT = c._pagesize[1]
for page in range(total_pages):
    print("\r正在生成 PDF (" + str(page + 1) + " / " + str(total_pages) + ")", end="")
    for i in range(20):  # 每页6张图片
        c.setFont("MSYaHei", 14)
        c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 20, fileName)
        c.drawCentredString(PAGE_WIDTH / 2, 10, "Page " + str(page + 1))
        index = page * 20 + i
        if index >= total_images:
            break  # 如果所有图片都已添加，则跳出循环
        # 计算当前图片的坐标
        padding_y = (a4_height - img_height * 5) / 2
        x = (i % 4) * img_width
        y = a4_height - (i // 4 + 1) * img_height - padding_y
        # 打开图片并放置到PDF中
        img_path = f"./temp-qr/qr_code_{index}.png"
        c.drawImage(img_path, x, y, width=img_width, height=img_height)
    c.showPage()  # 创建新页面
print("")

# 保存PDF
c.save()
