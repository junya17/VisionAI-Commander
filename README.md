# VisionAI-Commander

VisionAI-Commander is an innovative application that integrates the power of OpenAI's GPT-4 and DALL-E models to analyze and generate images based on interactive screenshots. This tool allows users to capture a screenshot, analyze it using GPT-4, and generate a new image based on the analysis using DALL-E 3.

## Features

- **Interactive Screenshot Capture**: Easily capture screenshots for analysis.
- **GPT-4 Integration**: Analyze screenshots using OpenAI's advanced GPT-4 model.
- **DALL-E 3 Image Generation**: Generate images based on the textual description provided by GPT-4.
- **Customizable Image Parameters**: Set image height, width, and quality.

## Installation

Ensure you have Python 3.11.5 installed and set up on your system.

1. Clone the repository:
   ```bash
   git clone https://github.com/junya17/VisionAI-Commander.git

2. Navigate to the cloned directory:
   ```bash
   cd VisionAI-Commander```
   
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

1. Run the application:
  ```bash
  python app.py [Your Query] [Image Height] [Image Width] [Quality]
```
Example: 
  ```bash
  python app.py "Describe this image" 1024 786 standard
```

2. Follow the on-screen instructions to capture a screenshot.
3. The application will analyze the screenshot and generate an image based on the analysis.

