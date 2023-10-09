from flask import Flask ,request , jsonify
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

# Function to extract main context and generate hashtags using NLTK
def extract_context_and_generate_hashtags(article_text, num_keywords=5):
    # Tokenize the article text into words
    words = word_tokenize(article_text.lower())

    # Remove punctuation and stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.strip(string.punctuation) for word in words if word.strip(string.punctuation) not in stop_words]

    # Calculate word frequencies
    word_freq = nltk.FreqDist(filtered_words)

    # Get the top keywords
    top_keywords = [word for word, freq in word_freq.most_common(num_keywords)]

    # Generate hashtags from the top keywords
    hashtags = ['#' + keyword.replace(' ', '') for keyword in top_keywords if keyword]

    return hashtags





app=Flask(__name__)
@app.route('/tag', methods=['POST'])
def hashtag():
    req=request.get_json()
    data=req["text"]
    r=extract_context_and_generate_hashtags(data)
    return jsonify({"Tags":r})
    
    
               

if __name__ == "__main__":
    app.run(debug=True)