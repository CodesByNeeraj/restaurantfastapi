from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key_raj = os.getenv("OPENAI_API_KEY")

def create_restaurant(input):
    llm = OpenAI(temperature = 1,openai_api_key=openai_api_key_raj)
    
    name_prompt = PromptTemplate(input_variables=['cuisine'],template="Give me a creative name for a {cuisine} restaurant that I am planning to open")
    
    name_chain = LLMChain(llm=llm,prompt = name_prompt,verbose = True, output_key = "name")
    
    menuitems_prompt = PromptTemplate(input_variables=["name"],template="Generate the menu items according to the restaurant {name}")
    
    menu_chain = LLMChain(llm=llm,prompt = menuitems_prompt,verbose=True,output_key=["menu_items"])
    
    final_chain = SequentialChain(chains=[name_chain,menu_chain],input_variables=['cuisine'],output_variables=['name','menu_items'])
    
    result = final_chain.invoke({"cuisine":str(input)})
    
    return result
                                  
                                  
    
    

