# HTML 批量转 PDF 工具

一个用于将指定文件夹中的 HTML 文件批量转换为 PDF 的 Python 脚本，适用于 Windows 系统，适合微信公众号文章保存、归档等用途。

---

## 📂 文件结构

```
项目目录/
├── html_to_pdf.py        # 主程序脚本
├── README.md             # 使用说明
├── PDF/                  # 转换后的 PDF 文件将保存于此（自动创建）
└── *.html                # 待转换的 HTML 文件
```

---

## ✅ 功能说明

- 将指定目录下的 `.html` 文件批量转换为 `.pdf`
- 支持限制转换数量，便于调试或分批执行
- 自动创建输出目录（PDF）
- 使用 `pdfkit` + `wkhtmltopdf`，兼容性强、效果稳定

---

## 💻 依赖安装

1. 安装 Python 依赖：

```bash
pip install pdfkit
```

2. 安装 `wkhtmltopdf`：

- 下载地址：[https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html)
- 安装后将 `wkhtmltopdf.exe` 加入系统环境变量（或在脚本中手动指定路径）

---

## ⚙️ 使用方法

1. 修改 `html_to_pdf.py` 中的路径配置：
   - `input_dir` 为 HTML 文件所在目录
   - `output_dir` 为 PDF 输出目录
   - 可设置 `max_convert = None` 以转换全部文件

2. 运行脚本：

```bash
python html_to_pdf.py
```

3. 转换结果将保存在 `PDF/` 文件夹中。

---

## 📝 示例配置片段

```python
# 示例配置
input_dir = Path(r'D:\临时文件\微信公众号批量下载工具3.5\下载\哥飞')
output_dir = input_dir / 'PDF'
max_convert = 10  # None 表示转换全部
```

---

## 🛠 常见问题

- **找不到 `wkhtmltopdf`**：
  - 请确认已安装并添加到环境变量，或通过 `pdfkit.configuration()` 指定其路径。

- **部分 HTML 样式不正确**：
  - 请检查 HTML 是否依赖 JS 动态渲染，`wkhtmltopdf` 主要适用于静态内容。

---

## 📌 版权说明

本脚本仅用于个人学习与归档用途，请勿用于非法或商业传播。
