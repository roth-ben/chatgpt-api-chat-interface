from openai import OpenAI
import gradio

client = OpenAI()
MODELS = ["gpt-3.5-turbo", "gpt-4-turbo"]
DEFAULT_SYSTEM_ROLE = "You are a helpful assistant."

system_message = {"role": "system", "content": DEFAULT_SYSTEM_ROLE}
messages = [system_message]

def CustomChatGPT(system_message_input, model, user_input):
    if(system_message_input != system_message["content"]):
        messages.clear()
        messages.append(system_message)
        messages[0]["content"] = system_message_input

    messages.append({
        "role": "user",
        "content": user_input
    })

    gpt_response = client.chat.completions.create(
        model = model,
        messages = messages,
        temperature = 0,
        frequency_penalty = 2.0
    )

    messages.append({
        "role": "assistant",
        "content": gpt_response.choices[0].message.content
    })

    return gpt_response.choices[0].message.content

def clear_messages():
    messages.clear()
    messages.append(system_message)

# Launch ChatGPT demo page
with gradio.Blocks() as demo:
    with gradio.Row():
        with gradio.Column():
            system_role_message = gradio.Textbox(label="System Role", value=system_message["content"])
            model_selection = gradio.Radio(MODELS, value=MODELS[0], label="Model")
            prompt = gradio.Textbox(label="Prompt")

            with gradio.Row():
                clear_button = gradio.Button("Clear")
                submit_button = gradio.Button("Submit", variant="primary")

        response = gradio.Textbox(label="Response")

    clear_button.click(fn = clear_messages)
    submit_button.click(fn=CustomChatGPT, inputs=[system_role_message, model_selection, prompt], outputs=response)

    prompt.submit(fn=CustomChatGPT, inputs=[system_role_message, model_selection, prompt], outputs=response)

demo.launch()
