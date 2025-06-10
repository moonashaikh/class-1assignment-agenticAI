# def main():
#     print("Hello from first-agent!")


# if __name__ == "__main__":
#     main()
#  install dotenv use command uv add python-dotenv
from dotenv import load_dotenv
import os
from agents import Agent , AsyncOpenAI ,OpenAIChatCompletionsModel ,RunConfig ,Runner


load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
# Check if the API key is present; if not, raise an error
if not openrouter_api_key:
    raise ValueError("OPENROUTER_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1",
)

model = OpenAIChatCompletionsModel(
#    model , replace if needed
    model="sarvamai/sarvam-m:free",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
     
agent = Agent(
    name = "Writer Agent",
    instructions = "You are a writer agent generate stories,poems , essay etc" 
)

#  runner function fro run agents

response = Runner.run_sync(
    agent,
    input = "Write a short essay on Quaid-e-azam in simple english",
run_config = config

)

print(response)
 
