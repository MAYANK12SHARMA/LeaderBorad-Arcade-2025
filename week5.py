import streamlit as st
import pandas as pd


def week5():

    data2 = [
        [
            "1",
            "Machine Learning Operations (MLOps) with Vertex AI: Model Evaluation",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/1080?utm_source=gcaf-site&utm_medium=website&utm_campaign=arcade-facilitator25)",
        ],
        [
            "2",
            "Infrastructure and Application Modernization with Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/266)",
        ],
        [
            "3",
            "Machine Learning Operations (MLOps) with Vertex AI: Model Evaluation",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/1080)",
        ],
        [
            "4",
            "AI Infrastructure: Introduction to AI Hypercomputer",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/1404)",
        ],
        [
            "5",
            "Infrastructure and Application Modernization with Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/266)",
        ],
        [
            "6",
            "Responsible AI: Applying AI Principles with Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/388)",
        ],
        [
            "7",
            "Exploring Data Transformation with Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/267)",
        ],
        [
            "8",
            "Gen AI Agents: Transform Your Organization",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/1267)",
        ],
        [
            "9",
            "Building Complex End to End Self-Service Experiences in Dialogflow CX",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/1103)",
        ],
    ]

    # Convert to DataFrame
    df = pd.DataFrame(data2, columns=["S. No", "Course Name", "Badge"])

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(df[0:5].to_markdown(index=False), unsafe_allow_html=True)
    with col2:
        st.markdown(df[5:].to_markdown(index=False), unsafe_allow_html=True)
