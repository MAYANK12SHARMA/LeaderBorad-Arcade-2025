import streamlit as st
import pandas as pd


def may():

    data2 = [
        [
            "Skills Boost Arcade Trivia May 2025 Week 1",
            "[Badge Link](https://www.cloudskillsboost.google/games/6155)",
            "1q-trivia-05261",
        ],
        [
            "Level 1: Data Modeling and Reporting",
            "[Badge Link](https://www.cloudskillsboost.google/games/6152)",
            "1q-reporting-1292",
        ],
        [
            "Level 2: Data Exploration and Integration",
            "[Badge Link](https://www.cloudskillsboost.google/games/6153)",
            "1q-integrate-3522",
        ],
        [
            "Level 3: Building Blocks",
            "[Badge Link](https://www.cloudskillsboost.google/games/6154)",
            "1q-build-19221",
        ],
        [
            "Skills Boost Arcade Base Camp May 2025",
            "[Badge Link](https://www.cloudskillsboost.google/games/6151)",
            "1q-basecamp-5591",
        ],
    ]

    # Convert to DataFrame
    df2 = pd.DataFrame(
        data2, columns=["Arcade Trivia/Game", "Badge Link", "access Code"]
    )

    col1, col2, col3 = st.columns([2, 3, 2])
    with col2:
        st.markdown(df2.to_markdown(index=False), unsafe_allow_html=True)
