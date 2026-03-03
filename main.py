# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain_openai import ChatOpenAI

# from langchain_openai import OpenAI
# llm = OpenAI(model="gpt-4o-mini")
# result = llm.invoke("내가 좋아하는 동물은 무엇일까?")
# print(result)

# langchain.llms -> langchain_openai로 써야하고,
# langchain_openai의 OpenAI는 LangChain 0.3+ 규격의 LLM 인터페이스를 따르고,
# 여기서는 .predict() 메서드가 아니라 .invoke() 를 써야 합니다.
########################
chat_model = ChatOpenAI()

st.title('인공지능 시인')

content = st.text_input('시의 주제를 입력해주세요.')

if st.button('시 작성 요청하기'):
    with st.spinner("시 작성 중....."):
        result = chat_model.invoke(content + "에 대한 시를 써줘.")
        st.write(result.content)

########################


