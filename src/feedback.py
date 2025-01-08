import streamlit as st

from textblob import TextBlob  # Install using: pip install textblob
def feed_back():
    # Collect user feedback
    st.write("---")
    st.write("### Chatbot Feedback")
    feedback = st.text_area("Additional Feedback:")
    
    if st.button("Submit Feedback"):
        # Show thank you message after submitting feedback
        st.success("Thank you for your feedback!")
        
        # Perform sentiment analysis on the provided feedback
        predict_sentiment(feedback)


        # Optionally, save or store feedback data
        # feedback_data = {
        #     "rating": rating,
        #     "feedback": feedback,
        # }
        # st.write("Feedback Data:", feedback_data)

    return feedback

def predict_sentiment(feedback):
    if feedback:  # Only perform sentiment analysis if feedback is provided
        # Analyze sentiment
        analysis = TextBlob(feedback)
        sentiment_score = analysis.sentiment.polarity
        
        # Predict sentiment
        if sentiment_score > 0:
            sentiment = "Positive 😊"
        elif sentiment_score < 0:
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"
        
        # Display sentiment analysis result
        st.write(f"Sentiment Analysis Result: **{sentiment}**")
        # st.write(f"Sentiment Score: {sentiment_score}")

# Running the feedback function
# feed_back()
