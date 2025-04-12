# 🧠 AI Interview Simulator

AI 면접관처럼 질문하고, 답변을 평가하고, 감정에 따라 표정을 바꾸는 인터랙티브 시뮬레이터입니다.  
LangChain + OpenAI + Segmind API를 활용하여 자연스러운 대화형 면접 경험을 제공합니다.

![ai-face](./output.png)

---

## 🚀 주요 기능

- 🎯 GPT를 이용한 직무별 면접 질문 생성
- 🧠 답변에 대한 GPT 기반 평가 + 감정 분석
- 😐 감정에 따른 AI 면접관의 표정 변화 (Segmind Expression API 활용)
- 💾 향후 확장: UI 연동(Streamlit), 다중 질문 반복, 결과 저장

---

## 📦 설치 방법

```bash
git clone https://github.com/your-username/ai-interview-simulator.git
cd ai-interview-simulator
python -m venv venv
venv\Scripts\activate   # or source venv/bin/activate
pip install -r requirements.txt
```

---

🔐 환경변수 (.env 파일)
루트 디렉토리에 .env 파일을 만들고 다음 내용을 넣으세요:
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
SEGMIND_API_KEY=SG-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
👉 API 키는 OpenAI와 Segmind에서 발급받을 수 있습니다.

---

🧪 실행 방법

python run_interview.py
실행 흐름:

  1. 직무 및 기술 기반 질문 자동 생성

  2. 사용자 답변 입력

  3. GPT 평가 + 감정 추출

  4. 감정에 따라 AI 면접관 표정 변화 이미지 생성

---

📁 프로젝트 구조
```bash
ai-interview-simulator/
├── run_interview.py         # 전체 시뮬레이션 실행 파일
├── question_generator.py    # 질문 생성 체인
├── answer_evaluator.py      # 답변 평가 체인
├── emotion_to_image.py      # 감정 → 표정 매핑
├── expression_api.py        # Segmind API 연동
├── download.png             # 기본 이미지
├── output.png               # 표정 결과 이미지
├── .env                     # API 키 (업로드 금지)
├── requirements.txt
└── README.md
```

---

💡 향후 개선
 Streamlit 기반 웹 UI 연동

 면접 질문 루프 기능

 답변 녹음 + TTS 기능 추가

 평가 내역 저장 (CSV / DB)

---
