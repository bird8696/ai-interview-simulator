import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

template = PromptTemplate(
    input_variables=["role", "skill"],
    template="당신은 {role} 직무의 면접관입니다. 지원자의 {skill} 역량을 평가할 수 있는 현실적인 질문 하나만 만들어주세요."
)

question_chain = template | llm
