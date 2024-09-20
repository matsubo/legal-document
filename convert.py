import sys
import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def convert_markdown(input_file):
    # 入力ファイルを読み込む
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # OpenAI APIにリクエストを送信
    response = chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "このファイルは契約書で法務文書です。タイトルや見出しをmarkdownで表現するようにフォーマットしてください。契約書のタイトルは見出し1，条項は見出し2を使うようにしてください。重要な文書なので文章の内容は変更しないでください。見出しやタイトルのマークアップだけを行ってください。また、見出しと同時に箇条書きに関しても可能ならばMarkdownで箇条書きにしてください。"},
            {"role": "user", "content": content}
        ],
        model="gpt-4o",
    )

    # 変換された内容を取得
    converted_content = response.choices[0].message.content

    # 出力ファイルに書き込む
    with open('out.md', 'w', encoding='utf-8') as file:
        file.write(converted_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: OPENAI_API_KEY=xxx python convert.py input_file.md")
        sys.exit(1)

    input_file = sys.argv[1]
    convert_markdown(input_file)
    print(f"{input_file} を変換し、結果を out.md に保存しました。")
