Sentiment Analysis Bot

This Python program analyzes the sentiment of text input by users using the TextBlob library. It categorizes the sentiment as either positive, negative, or neutral, and assigns an emoji accordingly.

 Installation

Before running the program, make sure to install the required libraries:

bash
pip install textblob


 Usage

1. Clone the repository to your local machine.
2. Navigate to the repository directory.
3. Run the sentiment_analysis_bot.py file.

bash
python sentiment_analysis_bot.py


4. Enter text when prompted to get sentiment analysis.

 How it Works

The program utilizes the TextBlob library to perform sentiment analysis on user input. It categorizes the sentiment based on the polarity of the input text. If the polarity is above a certain threshold, the sentiment is considered positive, and a happy emoji is displayed. If the polarity is below another threshold, the sentiment is considered negative, and an angry emoji is displayed. Otherwise, a neutral emoji is displayed.

Configuration

You can adjust the sensitivity of the sentiment analysis by modifying the sensitivity parameter in the run_bot() function. This parameter determines the threshold for classifying sentiment as positive or negative.

Example

plaintext
Enter text to get sentiment analysis:
YOU: I love sunny days at the beach
BOT: 😊 (0.5)

