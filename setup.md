## Install python and download

Install python 3.x

`git clone https://github.com/aether-sky/skynet.git`

## Setup npm

install nvm:

- windows: https://github.com/coreybutler/nvm-windows
- max: brew install nvm
- linux: apt-get install nvm

`nvm install latest`

`nvm use <whatever number it installed>`

## To run sveltekit (frontend):

(from inside skynet/skynet-frontend/)

`npm install`
`npm run dev`

It should tell you the address where it's hosted.

## Setup venv in skynet/

`cd skynet/`

`python -m venv venv`

activate (on mac/linux): `source venv/bin/activate`

activate (on windows): `./venv/Scripts/Activate`

Once activated you can install the pip packages needed to run everything (which I totally wrote down a list of):

`pip install fastapi uvicorn azure-identity azure-ai-inference azure-storage-blob azure-mgmt-resource dotenv`

## To run the server:

`uvicorn main:app --reload` (from inside skynet/skynet-ai)

## To run the ai api script (skynet/skynet-ai/azureai.py):

create a file called `.env` in skynet/skynet-ai/

add a line `AZURE_API_KEY=(my secret api key with no quotes)`

Then it should just work with `python azureai.py`. You have to modify the file currently to change the prompt and the request.
