import requests
import base64
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
import os

# 🔐 API 키 .env에서 불러오기
load_dotenv()
API_KEY = os.getenv("SEGMIND_API_KEY")

# ✅ 이미지 파일을 base64로 변환
def image_file_to_base64(image_path):
    with open(image_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

# ✅ Segmind Expression Editor API 호출
def apply_expression_to_image(image_path, save_path, smile=1, wink=0, woo=0):
    url = "https://api.segmind.com/v1/expression-editor"
    headers = {
        "x-api-key": API_KEY
    }

    base64_image = image_file_to_base64(image_path)

    payload = {
        "aaa": 0,
        "blink": 0,
        "eee": 0,
        "eyebrow": 0,
        "image": base64_image,
        "image_format": "png",
        "image_quality": 95,
        "pupil_x": 0,
        "pupil_y": 0,
        "rotate_pitch": 0,
        "rotate_roll": 0,
        "rotate_yaw": 0,
        "sample_parts": "OnlyExpression",
        "smile": smile,
        "wink": wink,
        "woo": woo
    }

    print(f"[📤] 표정 적용 중... smile={smile}, wink={wink}, woo={woo}")

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image.save(save_path)
        print(f"[✅] 이미지 저장 완료: {save_path}")
        os.startfile(save_path)  # Windows만 가능. Mac은 open, Linux는 xdg-open
    else:
        print(f"[❌] 요청 실패: {response.status_code}")
        print(response.text)

# ▶️ 실행 예시
if __name__ == "__main__":
    apply_expression_to_image(
        image_path="E:/AI_Simulation/AI_model/download.png",
        save_path="E:/AI_Simulation/AI_model/output_smile.png",
        smile=1, wink=0, woo=0  # ➜ happy 표현
    )
