import os
import requests
from dotenv import load_dotenv

# 加载环境变量（用于安全存储 API Key）
load_dotenv()
API_KEY = os.getenv("DEEPSEEK_API_KEY", "你的DeepSeek API Key")

def chat_with_deepseek(user_input):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": user_input}],
        "temperature": 0.7,
        "max_tokens": 2048
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"请求失败: {response.status_code} - {response.text}"

if __name__ == "__main__":
    print("DeepSeek Chatbot 已启动！输入 'quit' 退出。")
    while True:
        user_msg = input("你: ")
        if user_msg.lower() == "quit":
            print("再见！")
            break
        reply = chat_with_deepseek(user_msg)
        print(f"Bot: {reply}")
