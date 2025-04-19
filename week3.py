import streamlit as st
import pandas as pd


def week3():

    data2 = [
        [
            "1",
            "Skills Boost Arcade Trivia April 2025 Week 3",
            "[Badge Link](https://www.cloudskillsboost.google/games/6092?utm_source=qwiklabs&utm_medium=lp&utm_campaign=arcade25-April-trivia)",
            "1q-trivia-04066",
        ],
    ]

    # Convert to DataFrame
    df2 = pd.DataFrame(
        data2, columns=["S. No", "Arcade Trivia/Game", "Badge Link", "access Code"]
    )

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown(df2.to_markdown(index=False), unsafe_allow_html=True)

    # Data for Google Cloud Badges
    data = [
        [
            "2",
            "Set Up a Google Cloud Network",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/641)",
            "[Solution]()",
        ],
        [
            "3",
            "Store, Process, and Manage Data on Google Cloud - Console",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/658)",
            "[Solution](https://www.youtube.com/playlist?list=PLHfVKuKwHnWOpaKFGfTSXt8NSxWS4929C)",
        ],
        [
            "4",
            "Networking Fundamentals on Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/748)",
            "[Solution](https://www.youtube.com/watch?v=1GEBx0OA1do&list=PLHfVKuKwHnWNo4lXUyfKHn0l8HNYjjm_O)",
        ],
        [
            "5",
            "Integrate BigQuery Data and Google Workspace using Apps Script",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/737)",
            "[Copy Lab Name & Paste youtube]()",
        ],
        [
            "6",
            "Create a Streaming Data Lake on Cloud Storage",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/705)",
            "[Copy Lab Name & Paste youtube]()",
        ],
        [
            "7",
            "Get Started with Looker",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/647)",
            "[Copy Lab Name & Paste youtube]()",
        ],
        [
            "8",
            "Implement DevOps Workflows in Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/716)",
            "[Solution](https://www.youtube.com/watch?v=XjVt3kPR_gQ&list=PLHfVKuKwHnWOHWSjdrpBcjUKW5_n4c704)",
        ],
    ]

    # Convert to DataFrame
    df = pd.DataFrame(
        data, columns=["S. No", "Badge Name", "Badge Link", "Solution Link"]
    )

    # Display Data in Two Columns

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(df[0:4].to_markdown(index=False), unsafe_allow_html=True)
    with col2:
        st.markdown(df[4:].to_markdown(index=False), unsafe_allow_html=True)
    col1, col2 = st.columns(2)
