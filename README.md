# Instagram Caption & Hashtag Generator

Upload any image and get AI-generated captions and hashtags instantly. Built for content creators who want to stop staring at a blank caption box.

---

## What it does

- Upload a JPG, JPEG, or PNG image
- Get 3–5 caption suggestions generated from the image content
- Get relevant hashtag recommendations automatically
- Clean Streamlit UI — no technical knowledge needed to use it

---

## Why I built this

I kept seeing content creators spending 10–15 minutes writing captions for photos. This tool does it in under 3 seconds using computer vision + NLP. Two versions included — one uses a pre-trained model file, one calls the AI model directly (no `.pkl` file needed).

---

## Tech stack

- **Image understanding:** BLIP (Salesforce) via Hugging Face Transformers
- **Text processing:** NLTK
- **UI:** Streamlit
- **Language:** Python 3.10+

---

## Installation

```bash
git clone https://github.com/swaraj-d3v/instagram_caption_and_similarity_generator
cd instagram_caption_and_similarity_generator
pip install -r requirements.txt
```

---

## Usage

```bash
# Version 1 — uses pre-trained model file
streamlit run app.py

# Version 2 — direct AI inference, no .pkl needed
streamlit run app1.py
```

Upload your image → get captions and hashtags instantly.

---

## Demo

![App demo](demoelephant.png)

---

## Project structure

```
instagram_caption_and_similarity_generator/
├── app.py              # Streamlit app (model file version)
├── app1.py             # Streamlit app (direct inference version)
├── utils.py            # Helper functions
├── models/
│   └── caption_model.pkl
├── data/
│   └── captions.txt
├── requirements.txt
├── setup.ps1           # Windows setup script
└── .gitignore
```

---

## Author

**Swaraj Vijay Shinde**  
Final Year B.Tech — Data Science  
[LinkedIn](https://www.linkedin.com/in/swaraj-shinde-3b8631223) · [GitHub](https://github.com/swaraj-d3v)

---

## License

MIT
