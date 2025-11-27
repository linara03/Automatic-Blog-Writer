from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_blog_post(topic):

    template = """
    You are a professional blog writer.
    Write a detailed, well-structured blog post about the topic: "{topic}".

    The blog must include:
    - A catchy introduction
    - Well-organized sections with headings
    - Practical insights or examples
    - A clear conclusion
    """

    prompt = PromptTemplate.from_template(template)

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=OPENAI_API_KEY    
    )

    final_prompt = prompt.format(topic=topic)

    response = llm.invoke(final_prompt)   

    return response.content
