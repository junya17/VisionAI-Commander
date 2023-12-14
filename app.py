from openai import OpenAI
from dotenv import load_dotenv
import base64
import requests
import subprocess
import os
import sys
import uuid

load_dotenv()
client = OpenAI(
    api_key = os.environ.get('OPENAI_API_KEY')
)

# ターミナルからの入力を取得（コマンドライン引数）
if len(sys.argv) > 1:
    user_input = sys.argv[1]
    image_height = sys.argv[2] 
    image_width = sys.argv[3]
    quality = sys.argv[4] 
else:
    user_input = "What’s in this image?"  # デフォルトのテキスト
    quality = "stndard",
    image_height = "1024",
    image_width = "1024"

if not client:
        print("OpenAI APIキーが設定されていません。")
        sys.exit(1)

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  
def capture_interactive_screenshot(file_path="screenshot.png"):
    """インタラクティブなスクリーンショットを取る関数"""
    try:
        subprocess.run(["screencapture", "-i", file_path])
        return file_path
    except Exception as e:
        print(f"スクリーンショットの取得に失敗しました: {e}")
        sys.exit(1)

caputre = capture_interactive_screenshot("selected_screenshot.png")

# Getting the base64 string
base64_image = encode_image(caputre)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {client.api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": user_input
        },
        {
          "type": "image_url",
          "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

try:
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"APIリクエスト中にエラーが発生しました: {e}")
    sys.exit(1)

response_json = response.json()
prompt_response= response_json['choices'][0]['message']['content']
print(prompt_response)

# DALL-E 3を使用して画像を生成
try:
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt_response,
        size=f"{image_height}x{image_width}",
        quality=quality,
        n=1,
    )
except Exception as e:
    print(f"画像生成中にエラーが発生しました: {e}")
    sys.exit(1)

image_url = response.data[0].url

try:
    response = requests.get(image_url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"画像ダウンロード中にエラーが発生しました: {e}")
    sys.exit(1)

if response.status_code == 200:
    unique_id = uuid.uuid4()
    file_name = f"downloaded_image_{unique_id}.png"
    with open(file_name, 'wb') as f:
        f.write(response.content)

# example
# python app.py "What type of animal is this?"
# python app.py "Can you describe this image?"
# python app.py "Is he strong?"

# prompt : python app.py "What's in this image?" 1792 1024 hd