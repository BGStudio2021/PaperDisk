# PaperDisk
使用二维码在 A4 纸张上存储数据。  
## 使用方法  
1. 安装依赖：`pip install reportlab pillow qrcode`
2. 运行`main.py`，按照提示将需要处理的文件放在`sources`文件夹中再次运行
3. 在`output`文件夹查看处理结果，进行后续的打印操作
### 读取方法  
读取步骤需要手动操作，比较耗时。如需读取上述处理过的文件，请将所有的二维码从左至右、从上至下逐个扫描，并将扫描结果按顺序拼接得到 base64 编码，然后使用工具将编码转换为文件。当然，如果你感兴趣，可以开发专门的读取工具。
