from expression_api import apply_expression_to_image

# 감정 문자열 → 표정 파라미터 딕셔너리로 변환
def emotion_to_expression(emotion: str):
    # 감정 문자열을 소문자로 통일
    emotion = emotion.lower()

    if "긍정" in emotion:
        return dict(
            smile=1,
            woo=0,
            wink=0,
            eyebrow=0.2,
            blink=0,
            aaa=0
        )
    elif "부정" in emotion:
        return dict(
            smile=0,
            woo=1,
            wink=0,
            eyebrow=-1.0,   # 찡그린 눈썹
            blink=1,
            aaa=0.3,        # 살짝 입 벌림
            rotate_pitch=0,
            rotate_yaw=-10, # 고개 살짝 삐딱하게
            rotate_roll=0
        )
    else:  # 중립
        return dict(
            smile=0,
            woo=0,
            wink=0,
            eyebrow=0,
            blink=0,
            aaa=0
        )

# 실제 표정 적용 함수
def change_face_by_emotion(emotion, image_path, save_path):
    params = emotion_to_expression(emotion)
    apply_expression_to_image(image_path, save_path, **params)
