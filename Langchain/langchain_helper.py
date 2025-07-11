import os
from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType


load_dotenv(dotenv_path='.env')

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature = 0.7, openai_api_key = OPENAI_API_KEY)

    #Prompt Template that gives predefined instruction rather than mentioning it in every prompt
    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template = "I have a {animal_type} pet and I want a cool name where the color of the pet is {pet_color}. Suggest 5 cool names"
    )

    name_chain = LLMChain(llm = llm, prompt = prompt_template_name, output_key = 'pet_name')
    response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})
    return response

def langchain_agent():
    llm = OpenAI(temperature = 0.6)
    tools = load_tools(['wikipedia', 'llm-math'], llm = llm)

    agent = initialize_agent(
        tools, llm, agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True
    )

    result = agent.run(
        "Use the **wikipedia** tool to look up “average lifespan of a dog” and give me the numeric value in years. "
        "Then use the **Calculator** tool to multiply that number by 3. "
        "Return only the final number."
    )

    print(result)

if __name__ == '__main__':
    print(generate_pet_name("cow", 'black'))
    langchain_agent()