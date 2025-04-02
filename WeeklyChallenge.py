import streamlit as st
import pandas as pd


def app():
    # Weekly Challenges Heading
    st.markdown(
        """
        <style>
            @font-face {
                font-family: 'Poppins';
                src: url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
            }
        </style>
        <h2 style='text-align: center; font-family: Poppins, sans-serif; color: #E74C3C; font-weight:600; padding: 10px;'>
            ⚡ Weekly Challenges
        </h2>
        """,
        unsafe_allow_html=True,
    )

    # Challenge Duration Heading
    st.markdown(
        """
        <h2 style='text-align: center; font-family: Poppins, sans-serif; color: #D35400; font-weight:600; padding: 10px;'>
            🚀 Challenge from April 2 to April 8
        </h2>
        """,
        unsafe_allow_html=True,
    )

    # Data for Google Cloud Badges
    data = [
        [
            "1",
            "Analyze BigQuery Data in Connected Sheets",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/632?catalog_rank=%7B%22rank%22%3A49%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ7ffSTLYXXzHARXDqMRDCO9)",
        ],
        [
            "2",
            "Analyze Images with the Cloud Vision API",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/633?catalog_rank=%7B%22rank%22%3A66%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ5yZ5jbp1oHO1jc2cjCLnh5)",
        ],
        [
            "3",
            "Analyze Sentiment with Natural Language API",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/667?catalog_rank=%7B%22rank%22%3A73%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ4d0iiXtKI-yZV68uH42-e9)",
        ],
        [
            "4",
            "Analyze Speech and Language with Google APIs",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/634?catalog_rank=%7B%22rank%22%3A62%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ7V0KxGcgjO5ZySQA5HNJ8m)",
        ],
        [
            "5",
            "App Building with AppSheet",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/635?catalog_rank=%7B%22rank%22%3A52%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ5LUEH1yNyrR6AEjU3DRXjN)",
        ],
        [
            "6",
            "App Engine: 3 Ways",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/671?catalog_rank=%7B%22rank%22%3A58%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ68ij2ch5MfZU4Rp5kOzM5t)",
        ],
        [
            "7",
            "Automate Data Capture at Scale with Document AI",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/674?catalog_rank=%7B%22rank%22%3A37%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ5tPadaYpfGSKDVWcGQ0APX)",
        ],
        [
            "8",
            "Build Google Cloud Infrastructure for AWS Professionals",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/687?catalog_rank=%7B%22rank%22%3A45%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ6ydk7_V2ioOGJoWfSYsfRE)",
        ],
        [
            "9",
            "Build Google Cloud Infrastructure for Azure Professionals",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/688?catalog_rank=%7B%22rank%22%3A46%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ4Har7DhVqdqZVg_hjxNYXA)",
        ],
        [
            "10",
            "Create a Secure Data Lake on Cloud Storage",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/704?catalog_rank=%7B%22rank%22%3A63%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ5hNVlRslMPqnFz1ysYGw9F)",
        ],
        [
            11,
            "Build Real World AI Applications with Gemini and Imagen",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/1076?catalog_rank=%7B%22rank%22%3A83%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ7IWI1lt-l2in9ToxNLz5hE)",
        ],
        [
            12,
            "Cloud Functions: 3 Ways",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/696?catalog_rank=%7B%22rank%22%3A55%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ5_SpnV8E2Y9zBUpXxSHeps)",
        ],
        [
            13,
            "Cloud Speech API: 3 Ways",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/700?catalog_rank=%7B%22rank%22%3A75%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ6erxmi1eQzZKt2-X6DrMpl)",
        ],
        [
            14,
            "Configure Service Accounts and IAM Roles for Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/702?catalog_rank=%7B%22rank%22%3A77%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ62ag1lO7gN42Ft64NJotPe)",
        ],
        [
            15,
            "Using the Google Cloud Speech API",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/756?catalog_rank=%7B%22rank%22%3A71%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ6LHKTlUg959p5Tum1R3A3z)",
        ],
    ]

    # Convert to DataFrame
    df = pd.DataFrame(
        data, columns=["S. No", "Badge Name", "Badge Link", "Solution Link"]
    )

    # Display Data in Two Column

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(df[0:8].to_markdown(index=False), unsafe_allow_html=True)
    with col2:
        st.markdown(df[8:15].to_markdown(index=False), unsafe_allow_html=True)

    data2 = [
        [
            "16",
            "The Arcade Base Camp April",
            "[Badge Link](https://www.cloudskillsboost.google/games/6059?utm_source=qwiklabs&utm_medium=lp&utm_campaign=basecamp-April-arcade25)",
            "1q-basecamp-9932",
        ],
        [
            "17",
            "Trivia April 2025 Week 1",
            "[Badge Link](https://www.cloudskillsboost.google/games/6058?utm_source=qwiklabs&utm_medium=lp&utm_campaign=arcade25-April-trivia)",
            "1q-trivia-01202",
        ],
        [
            "18",
            "Level 1: Application Development and Security with GCP",
            "[Badge Link](https://www.cloudskillsboost.google/games/6064?utm_source=qwiklabs&utm_medium=lp&utm_campaign=level1-April-arcade25)",
            "1q-appdevscr-4912",
        ],
    ]

    # Convert to DataFrame
    df2 = pd.DataFrame(
        data2, columns=["S. No", "Arcade Trivia/Game", "Badge Link", "access Code"]
    )
    
    col1,col2,col3 = st.columns([1,3,1])
    with col2: 
        st.markdown(df2.to_markdown(index=False), unsafe_allow_html=True)

    # Important Notes Section
    st.markdown(
        """
        ### 📌 **Important Notes**  
        - ✅ **Complete all the Badges, Trivia, and Games Before the deadline.**  
        - 🎯 *Plan your daily lab completions efficiently. You can perform 15 labs per days.*  
        - 📅 **Deadlines are strict!** Complete your tasks on time! I am not responsible of any failure** 
        - 🏆 **To find the labs solution, Copy the lab name or Lab code (below lab name) and paste it on Youtube. (Siggested Channel : quick Lab, Cloud Hustlers, Btechy)**
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    app()
