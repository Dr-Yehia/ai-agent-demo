# sentiment_analysis.py

def analyze_sentiment(text):
    positive_words = ["good", "great", "happy", "excellent", "amazing"]
    negative_words = ["bad", "sad", "terrible", "horrible", "worst"]
    
    text = text.lower()
    score = 0

    for word in positive_words:
        if word in text:
            score += 1

    for word in negative_words:
        if word in text:
            score -= 1

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

# Example
if __name__ == "__main__":
    print(analyze_sentiment("The product is amazing but the shipping was bad."))
