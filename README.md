


  
  
  
  


📝 Text Summarizer

  Summarize long texts instantly using AI.
  Minimal UI. Lightning fast. Open source.


## 🚀 Overview

Text Summarizer is a modern web app that turns long articles, reports, or documents into crisp, meaningful summaries—instantly.  
Paste any text, click, and get the gist. No coding required.

- ⚡ **Fast, high-quality summaries**
- 🤖 **Powered by Hugging Face Transformers**
- 🌈 **Minimal, distraction-free UI**
- 📝 **Perfect for students, professionals, and anyone who reads a lot**

## 🖥️ Demo



## 📦 Installation

**1. Clone this repository**
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

**2. (Optional) Create a virtual environment**
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```
_or, manually:_
```bash
pip install torch gradio transformers
```

## ▶️ Usage

```bash
python textsummary.py
```
- The Gradio web interface will open in your browser.
- Paste or type any text and click **Submit** to see the summary.

## 📝 Example

**Input:**
```text
Donald John Trump (born June 14, 1946) is an American politician, media personality, and businessman who is the 47th president of the United States...
```

**Output:**
```text
Donald Trump is the 47th president of the United States, previously serving as the 45th president from 2017 to 2021.
```

## 🗂️ Project Structure

```text
.
├── textsummary.py           # Main application script
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── Models/                  # (Optional) Local model files
```

## ✨ Features

- **Abstractive Summarization:**  
  Uses `sshleifer/distilbart-xsum-12-6` for human-like summaries.
- **Instant Results:**  
  No waiting, no nonsense.
- **Minimal UI:**  
  Clean, responsive, and mobile-friendly.
- **Plug & Play:**  
  Just run and use.

## ⚙️ Customization

- **Change the model:**  
  Edit `model_path` in `textsummary.py` to use any Hugging Face summarization model.
- **Tweak the UI:**  
  Change Gradio interface labels and layout as you like.

## ❓ Troubleshooting

- **Missing model files?**  
  Make sure your model directory contains `pytorch_model.bin` or `model.safetensors` and other required files.
- **Gradio not installed?**  
  Run:
  ```bash
  pip install gradio
  ```
- **CUDA/CPU issues?**  
  Check your PyTorch installation and hardware compatibility.

## 🤝 Credits

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Gradio](https://gradio.app/)
- [PyTorch](https://pytorch.org/)

## 📄 License

MIT License


  ✨ Fork it. Star it. Use it. Summarize smarter! ✨


