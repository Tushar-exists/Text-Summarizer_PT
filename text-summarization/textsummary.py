import torch
import gradio
from torch.utils.tensorboard import summary
# Use a pipeline as a high-level helper
from transformers import pipeline

model_path = (
    "../.venv/Models/models--sshleifer--distilbart-xsum-12-6/snapshots/5b2e376c845c201ddc34ec0e55fd1ad9890ba5ee")

text_summary = pipeline("summarization", model=model_path, torch_dtype=torch.bfloat16)


def Summary(input):
    output = text_summary(input)
    return output[0]['summary_text']


gradio.close_all()

demo = gradio.Interface(fn=Summary,
                    inputs=[gradio.Textbox( label = "Input text to summarize",lines=6)],
                    outputs=[gradio.Textbox(label = "Summarized text",lines=4)],
                    title="Text Summarization ",
                    description="Summarizes the text to get hands on overview of the data")
demo.launch()
