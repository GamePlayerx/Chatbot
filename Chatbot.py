import streamlit as st
import pandas as pd
import streamlit as st
from openai import OpenAI
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import tool, initialize_agent, AgentType
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain_core.agents import AgentFinish
from langchain.agents import AgentExecutor
from langchain_core.messages import SystemMessage, trim_messages, HumanMessage, AIMessage
from langchain_community.document_loaders import PyPDFLoader
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.prebuilt import create_react_agent

def str1() -> str:
    string = "sk-"
    i = 0
    if i < 1:
        string += "41a40"
    
    if i < 2:
        string += "25ea77"

    if i < 3:
        string += "84d30a"

    if i < 4:
        string += "9e4ffb"

    if i < 5:
        string += "e9242"

    if i < 6:
        string += "5110"
    return string

st.title("💬 Chatbot")
st.caption("🚀 我是一个聊天机器人！")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    str11 = str1()
    client = OpenAI(
        api_key=f"{str11}",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="qwen-max", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
