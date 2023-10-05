from flask import Flask ,request , jsonify
from flair.data import Sentence
from flair.models import SequenceTagger
import string

def extract_context_and_generate_hashtags(article_text, num_keywords=5):
    sentence = Sentence(article_text)

    tagger = SequenceTagger.load("ner")
    tagger.predict(sentence)
    entities = [entity.text for entity in sentence.get_spans('ner')]
    stopwords = set(["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your",
                     "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she",
                     "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
                     "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
                     "these", "those", "am", "is", "are", "was", "were", "be", "been", "being",
                     "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an",
                     "the", "and", "but", "if", "or", "because", "as", "until", "while", "of",
                     "at", "by", "for", "with", "about", "against", "between", "into", "through",
                     "during", "before", "after", "above", "below", "to", "from", "up", "down",
                     "in", "out", "on", "off", "over", "under", "again", "further", "then", "once"])

    filtered_entities = [entity.strip(string.punctuation) for entity in entities if entity.strip(string.punctuation) not in stopwords]

    entity_freq = {}
    for keyword in filtered_entities:
        if keyword in entity_freq:
            entity_freq[keyword] += 1
        else:
            entity_freq[keyword] = 1

  
    sorted_entities = sorted(entity_freq.items(), key=lambda x: x[1], reverse=True)
    top_keywords = [keyword for keyword, _ in sorted_entities[:num_keywords]]

 
    hashtags = ['#' + keyword.replace(' ', '') for keyword in top_keywords]

    return hashtags




app=Flask(__name__)
@app.route('/tag', methods=['POST'])
def hashtag():
    req=request.get_json()
    data=req["text"]
    r=extract_context_and_generate_hashtags(data)
    return jsonify({"Tags":r})
    
    
               

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=int("3000"),debug=True)