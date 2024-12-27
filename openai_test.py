from openai import OpenAI
from api_pjt.config import OPENAI_API_KEY

CLIENT = OpenAI(
    api_key=OPENAI_API_KEY,
)


def ask_chatgpt(user_message):
    system_instructions = """
이제부터 너는 Django 프레임워크에 대해 설명하고 
사용자가 Django 프레임워크에 대해 어려움을 겪고 있다고 가정하고 도와주는 챗봇이 되어야해.
다른 코딩 언어나 프레임워크에 대해 설명하거나 다른 주제로 이야기하는 것은 금지야.
Django 공식문서의 링크를 제공하거나 Django 프레임워크에 대한 설명도 추가해줘.
"""
    completion = CLIENT.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_instructions,
            },
            {
                "role": "user",
                "content": user_message,  # 함수의 인자로 받은 사용자 메시지를 사용
            },
        ],
    )
    return completion.choices[0].message.content

# 01
while True:
    user_input = input("입력하세요: ")
    if user_input == "exit":
        break
    response = ask_chatgpt(user_input)


# 02
user_input = input('입력하세요: ')  # 사용자 입력 받기
response = ask_chatgpt(user_input)  # 사용자 입력을 함수에 전달
print(response)  # 챗봇의 응답 출력
