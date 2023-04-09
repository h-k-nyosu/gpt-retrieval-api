from langchain.agents import Tool
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain import OpenAI
from langchain.agents import initialize_agent
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings


class ChatService:
    def __init__(self):
        embedding = OpenAIEmbeddings()
        db = Chroma(persist_directory="db", embedding_function=embedding)
        tools = [
            Tool(
                name="LangChain Documents",
                func=db.similarity_search,
                description="use the database to find LangChain documents to answer your question about langChain",
            ),
        ]
        memory = ConversationBufferMemory(memory_key="chat_history")
        llm = OpenAI(temperature=0)
        self.agent_chain = initialize_agent(
            tools,
            llm,
            agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
            verbose=True,
            memory=memory,
        )

    def chat(self, input: str) -> str:
        return self.agent_chain.run(input=input)
