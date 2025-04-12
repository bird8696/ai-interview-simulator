import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.3,
    api_key=os.getenv("OPENAI_API_KEY")
)

template = PromptTemplate(
    input_variables=["question", "answer"],
    template="""
다음은 면접 질문과 그에 대한 답변입니다.

질문: {question}
답변: {answer}

다음 기준으로 평가해주세요:
1. 논리성
2. 전문성
3. 커뮤니케이션 능력
4. 직무 적합성

각 항목을 5점 만점으로 점수화하고, 총점과 피드백을 제공하세요.
마지막 줄에 감정 요약: 긍정적 / 부정적 중 하나를 작성하세요.
"""
)

evaluator_chain = template | llm
