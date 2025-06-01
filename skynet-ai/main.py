import subprocess
import os

from typing import Any
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()

apikey = os.getenv("RUNPOD_API_KEY")
TEMPLATE_ID = "j6sjrvfa7lv5mq"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": apikey
}

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify e.g. ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def run_ollama_via_ssh(command):
    cmd_str = 'ollama run llama3 "%s"' % command
    host = "157.157.221.29"  # Replace with actual pod IP or hostname
    key_filepath = os.getenv('RUNPOD_KEY_FILEPATH')
    username = 'root'
    port = '43518'
    ssh_command = [
        "ssh",
        '-t',
        "-i", key_filepath,
        "-p", port,
        f"{username}@{host}",
        cmd_str
    ]

    try:
        # result = subprocess.run(ssh_command,capture_output=True,text=True,check=True)
        print(' '.join(ssh_command))
        result = subprocess.run(ssh_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        print("SSH command executed successfully.")
        for line in result.stdout:
            print(line, end='')
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)
        return None

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = "") -> dict[str, Any]:
    return {"item_id": item_id, "q": q}

# Define a request model
class TextInput(BaseModel):
    text: str

@app.post("/query")
async def receive_text(data: TextInput):
    # `data.text` will be the string from the request body
    print("Received text:", data.text)
    run_ollama_via_ssh(data.text)
    # You can return any response
    return {"message": f"Received: {data.text}"}