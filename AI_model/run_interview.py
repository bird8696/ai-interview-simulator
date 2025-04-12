import os
from question_generator import question_chain
from answer_evaluator import evaluator_chain
from emotion_to_image import change_face_by_emotion

# 이미지 경로 처리
BASE_DIR = os.path.dirname(__file__)
image_path = os.path.join(BASE_DIR, "download.png")
save_path = os.path.join(BASE_DIR, "output.png")

# 1. 질문 생성
question = question_chain.invoke({
    "role": "프론트엔드 개발자",
    "skill": "React"
}).content.strip()
print(f"[❓ 질문] {question}")

# 2. 답변 입력
answer = input("[🗣️ 답변 입력] > ")

# 3. 평가 + 감정 추출
result = evaluator_chain.invoke({
    "question": question,
    "answer": answer
}).content.strip()
print("\n[📊 평가 결과]\n", result)

# 4. 감정만 추출
emotion_line = result.strip().splitlines()[-1]
emotion = emotion_line.replace("감정 요약:", "").strip()

# 5. 표정 이미지 생성
change_face_by_emotion(emotion, image_path=image_path, save_path=save_path)
