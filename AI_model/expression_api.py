import requests
import base64
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv

# .env 로딩 및 API 키 불러오기
load_dotenv()
API_KEY = os.getenv("SEGMIND_API_KEY")

# 이미지 → base64 인코딩
def image_file_to_base64(image_path):
    with open(image_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

# Segmind API 호출 함수
def apply_expression_to_image(
    image_path,
    save_path,
    smile=0,
    woo=0,
    wink=0,
    eyebrow=0,
    aaa=0,
    blink=0,
    rotate_pitch=0,
    rotate_yaw=0,
    rotate_roll=0
):
    url = "https://api.segmind.com/v1/expression-editor"
    headers = {
        "x-api-key": API_KEY
    }

    image_base64 = image_file_to_base64(image_path)

    payload = {
        "image": image_base64,
        "image_format": "png",
        "image_quality": 95,
        "sample_parts": "OnlyExpression",

        # 표정 관련 파라미터
        "smile": smile,
        "woo": woo,
        "wink": wink,
        "eyebrow": eyebrow,
        "aaa": aaa,
        "blink": blink,

        # 고개 각도 조절
        "rotate_pitch": rotate_pitch,
        "rotate_yaw": rotate_yaw,
        "rotate_roll": rotate_roll,

        # 기본값 유지
        "pupil_x": 0,
        "pupil_y": 0,
        "eee": 0
    }

    # API 호출
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img.save(save_path)
        os.startfile(save_path)
        print(f"[✅] 이미지 저장 완료: {save_path}")
    else:
        print(f"[❌] Segmind 요청 실패: {response.status_code}")
        print(response.text)
