# setup.ps1 - Project folder setup script

# Create main project folder structure
mkdir models -ErrorAction SilentlyContinue
mkdir data -ErrorAction SilentlyContinue
mkdir outputs -ErrorAction SilentlyContinue

# Create required files
ni app.py -ItemType File -Force
ni requirements.txt -ItemType File -Force
ni utils.py -ItemType File -Force
ni .\data\captions.txt -ItemType File -Force
ni .\models\caption_model.pkl -ItemType File -Force
