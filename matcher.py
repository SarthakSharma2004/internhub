from langchain_groq import ChatGroq
from prompts import PromptManager 
from config import get_settings

settings = get_settings()

class InternshipMatcher:
    def __init__(self):
        self.llm = ChatGroq(model_name = "openai/gpt-oss-120b", api_key = settings.GROQ_API_KEY ,temperature = 0.2)
        self.prompt = PromptManager.get_prompt()

    def analyze(self, student_profile, internship_description):
            
        user_input = f"""
Student Profile:
{student_profile}

Internship Description:
{internship_description}

"""

        chain = self.prompt | self.llm

        response = chain.invoke({"input" : user_input})

        return response.content
        