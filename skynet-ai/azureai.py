import os
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

load_dotenv()
apikey = os.getenv("AZURE_API_KEY")

if not apikey:
    raise ValueError("AZURE_API_KEY environment variable is not set.")

endpoint = "https://skynet-lambda3-lb-resource.services.ai.azure.com/models"
model_name = "Llama-3.3-70B-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(apikey),
    api_version="2024-05-01-preview"
)
prompt = "Purposefully misunderstand the question."
request = "I am going to Paris, what should I see?"

response = client.complete(
    messages=[
        SystemMessage(content=prompt),
        UserMessage(content=request),
    ],
    max_tokens=2048,
    temperature=0.8,
    top_p=0.1,
    presence_penalty=0.0,
    frequency_penalty=0.0,
    model=model_name
)
print(request)
print()
print(response.choices[0].message.content)