from langchain_groq import ChatGroq
from prompts import PromptManager 

class InternshipMatcher:
    def __init__(self):
        self.llm = ChatGroq(model_name = "openai/gpt-oss-120b", temperature = 0.2)
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
        