import os
from pathlib import Path
import pdfkit

# 设置路径
input_dir = Path(r'you path')
output_dir = input_dir / 'PDF'
output_dir.mkdir(exist_ok=True)

# 设置最大转换数量（None 表示全部）
max_convert = None  # 设置为 None 可全部转换

# 如果 wkhtmltopdf 没在系统环境变量中，手动指定路径
config = pdfkit.configuration(wkhtmltopdf=r'you path\wkhtmltopdf.exe')

def convert_html_to_pdf(input_path, output_path):
    try:
        pdfkit.from_file(str(input_path), str(output_path), configuration=config)
        print(f"✅ 转换成功: {input_path.name}")
    except Exception as e:
        print(f"❌ 转换失败: {input_path.name}, 错误: {e}")

def main():
    html_files = list(input_dir.glob('*.html'))
    if max_convert is not None:
        html_files = html_files[:max_convert]

    if not html_files:
        print("⚠️ 没有找到 HTML 文件")
        return

    for html_file in html_files:
        pdf_file = output_dir / (html_file.stem + '.pdf')
        convert_html_to_pdf(html_file, pdf_file)

if __name__ == "__main__":
    main()
