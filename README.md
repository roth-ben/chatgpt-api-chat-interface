# ChatGPT API - Assistant Interface
This Python project provides a simple interface to interact with the OpenAI ChatGPT APIs, allowing users to chat with both the 3.5-turbo and 4.0-turbo models.

## Prerequisites
- Docker
- Python 3.x
- Conda
- Gradio client (refer to [Gradio client documentation](https://www.gradio.app/guides/getting-started-with-the-python-client))
- An API key from OpenAI (refer to [OpenAI API documentation](https://platform.openai.com/docs/introduction)) 

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/openai-chatgpt-python-client.git
   ```

2. Start docker environment:
   ```bash
   docker run -it --name chatgpt-assistant -p 7860:7860 -e GRADIO_SERVER_NAME=0.0.0.0 continuumio/miniconda3 /bin/bash
    ```

3. Install required dependencies:
   ```bash
   apt update -y
   conda create -n chatgpt-api python=3.11 -y
   conda activate chatgpt-api
   conda install -c conda-forge openai gradio -y
   ```

## Usage

1. Set your OpenAI API key as an environment variable:

    ```bash    
    export OPENAI_API_KEY='your-api-key'
    ```
   
2. Run the script `chatgpt-api-assistant.py`:

     ```python
     python chatgpt-api-assistant.py
     ```

3. Open a browser and navigate to [http://localhost:7860/](http://localhost:7860/). You can now add in your own custom system preamble to set the tone of the model. Choose your model, and enter your prompt.

**Note:** Ensure that you comply with [OpenAi's use case policy](https://beta.openai.com/policies/use-case-policy) while using this tool.

Feel free to contribute by submitting pull requests or reporting issues in this repository!
