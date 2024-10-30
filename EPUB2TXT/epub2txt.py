import os
from ebooklib import epub
from bs4 import BeautifulSoup

def epub_to_txt(epub_path):
    try:
        book = epub.read_epub(epub_path)
        output_txt = ""

        for item in book.get_items():
            if item.media_type == 'application/xhtml+xml':
                content = item.get_content()
                soup = BeautifulSoup(content, features="html.parser")
                text = soup.get_text()
                output_txt += text + "\n"

        return output_txt

    except Exception as e:
        print(f"Error processing {epub_path}: {e}")
        return ""

def save_to_txt(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(content)

if __name__ == '__main__':
    # 定义EPUB和TXT文件夹路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    epub_folder = os.path.join(current_dir, "EPUB")
    txt_folder = os.path.join(current_dir, "TXT")

    # 确保输出TXT文件夹存在
    os.makedirs(txt_folder, exist_ok=True)

    # 遍历EPUB文件夹中的每个EPUB文件
    for filename in os.listdir(epub_folder):
        if filename.endswith('.epub'):
            epub_file = os.path.join(epub_folder, filename)
            txt_file = os.path.join(txt_folder, f"{os.path.splitext(filename)[0]}.txt")

            # 从EPUB文件中提取文本
            txt_content = epub_to_txt(epub_file)

            # 将文本保存到TXT文件
            if txt_content:
                save_to_txt(txt_file, txt_content)
                print(f"转换成功：{epub_file} -> {txt_file}")
            else:
                print(f"转换失败：{epub_file}")
