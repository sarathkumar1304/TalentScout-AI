import streamlit as st 

def home_ui():
    st.title("TalentScout - Hiring Assistant Chatbot 🤖")
    st.write("""
    Welcome to **TalentScout**, your AI-powered hiring assistant! 🎉
    This tool simplifies the hiring process by leveraging the power of AI to:
    - Parse resumes and extract candidate details.
    - Generate tailored technical questions based on a candidate's expertise.
    - Collect and save answers for structured analysis.
    
    Navigate using the sidebar to:
    - Upload a candidate's resume for automated parsing.
    - Enter candidate details manually for question generation.
    
    Let's revolutionize the hiring process together! 🚀
    """)
    st.image(
        "https://via.placeholder.com/800x400.png?text=Welcome+to+TalentScout",
        use_container_width=True,
    )



def about_me():
    st.title("About Me 🙋‍♂️ ")
    st.write("""
Hello! 👋 I'm **R. Sarath Kumar**, and I'm thrilled to have you here! I’m a dedicated and passionate professional in **Data Science** and **Machine Learning** 🤖.  
With a strong foundation in statistics, machine learning, and MLOps, I love transforming data into valuable insights and building predictive models that solve real-world problems. My work spans across multiple domains, and I’m always excited to explore new tools and techniques to make data-driven decisions more effective and impactful.

Feel free to browse through my projects, where you’ll find some of the most exciting applications of AI and machine learning, and don't hesitate to reach out if you’d like to connect or discuss potential collaborations!
""")



    st.subheader("Contact Information")
    
    
    st.write("🔗LinkedIn: [LinkedIn](https://www.linkedin.com/in/r-sarath-kumar-666084257)") 
    st.write("🔗Github:[Github](https://www.github.com/sarathkumar1304)") 

    
    st.write("📧 Email: [sarathkumarrathnam@gmail.com](mailto:sarathkumarrathnam@gmail.com)")  
    
    st.write("📞 Phone: 7780651312")  