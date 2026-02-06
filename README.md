# Image Captioning & Hashtag Recommender

Upload an image and get **recommended captions and hashtags** instantly! This project uses state-of-the-art AI models to generate relevant captions and hashtags based on the content of your images.

---

## Features

- Upload any image (JPG, JPEG, PNG) and get recommendations.  
- **Caption Recommendation:** Generate creative captions automatically.  
- **Hashtag Recommendation:** Suggest relevant hashtags for better reach.  
- Interactive GUI built with **Streamlit**.  
- Fast and easy to use for Instagram content creators.

---

## Demo

![App Demo](demoelephant.png)  <img width="466" height="715" alt="Screenshot 2025-09-27 190630" src="https://github.com/user-attachments/assets/dbf1af1d-07e0-47e0-b993-b412a149b44e" />



---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/swarajshinde12/instagram_caption_recommender.git
cd instagram_caption_recommender

# Install dependencies:

python -m pip install -r requirements.txt

Usage

Run the Streamlit app:

streamlit run app.py


Upload your image.

See caption and hashtag recommendations instantly.

Folder Structure
instagram_caption_recommender/
│
├─ app.py               # Main Streamlit app
├─ utils.py             # Helper functions
├─ models/
│   └─ caption_model.pkl  # Pre-trained model
├─ data/
│   └─ captions.txt     # Caption dataset
├─ requirements.txt     # Python dependencies
├─ setup.ps1            # Setup script (Windows)
└─ .gitignore           # Ignore unnecessary files

Technologies Used

Python 3.13

Streamlit

Hugging Face Transformers (BLIP)

NLTK (text processing)

scikit-learn / Pickle (model handling)

License

This project is licensed under the MIT License.

Made with ❤️ by Swaraj Shinde


Most imp o can do this without txt and pkl by using ai ill give that code too as app1.py check that out

