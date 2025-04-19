import streamlit as st
import pandas as pd


def week2():

    data2 = [
        [
            "1",
            "Skills Boost Arcade Trivia April 2025 Week 2",
            "[Badge Link](https://www.cloudskillsboost.google/games/6079?utm_source=qwiklabs&utm_medium=lp&utm_campaign=arcade25-April-trivia)",
            "1q-trivia-04122",
        ],
        [
            "2",
            "Level 2: Cloud Infrastructure & API Essentials",
            "[Badge Link](https://www.cloudskillsboost.google/games/6065?utm_source=qwiklabs&utm_medium=lp&utm_campaign=level2-April-arcade25)",
            "1q-apicap-10000",
        ],
        [
            "3",
            "Level 3: The Arcade Quiz",
            "[Badge Link](https://www.cloudskillsboost.google/games/6063?utm_source=qwiklabs&utm_medium=lp&utm_campaign=level3-April-arcade25)",
            "1q-equiz-40233",
        ],
        [
            "4",
            "TechCare",
            "[Badge Link](https://www.cloudskillsboost.google/games/6080?utm_source=qwiklabs&utm_medium=lp&utm_campaign=special-April-arcade25)",
            "1q-techcare-0326",
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
            "5",
            "Get Started with Google Workspace Tools",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/676)",
            "[Solution](https://www.youtube.com/watch?v=t93hJjIYUWo)",
        ],
        [
            "6",
            "Use Functions, Formulas, and Charts in Google Sheets",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/776)",
            "[Solution](https://www.youtube.com/watch?v=XYhHlP5Tfrk)",
        ],
        [
            "7",
            "Build LookML Objects in Looker",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/639)",
            "[Solution](https://youtu.be/FsesF7Gh8tk?si=KdL1LjeEQqpmN_Iw)",
        ],
        [
            "8",
            "Deploy Kubernetes Applications on Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/663)",
            "[Solution](https://www.youtube.com/watch?v=F4h6EmSJkFM)",
        ],
        [
            "9",
            "Set Up an App Dev Environment on Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/637)",
            "[Solution](https://www.youtube.com/watch?v=lYPt_N54QbQ)",
        ],
        [
            "10",
            "Monitoring in Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/747)",
            "[Solution](https://www.youtube.com/watch?v=cZJn_C_Ry4w)",
        ],
        [
            "11",
            "Get Started with API Gateway",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/662)",
            "[Solution](https://www.youtube.com/watch?v=lZjb1Mgg3Tc)",
        ],
        [
            "12",
            "Prompt Design in Vertex AI",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/976)",
            "[Solution](https://www.youtube.com/playlist?list=PL5aOhqv5LVIpGYa_pR6PYmUk2kwd60xWC)",
        ],
        [
            "13",
            "The Basics of Google Cloud Compute",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/754)",
            "[Solution](https://youtu.be/l4GjFvPhU4Q?si=oAiB3uBByIN_snSK)",
        ],
        [
            "14",
            "Implement Load Balancing on Compute Engine",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/648)",
            "[Solution](https://www.youtube.com/watch?v=4oES1n_Reck&list=PL5aOhqv5LVIqMSMQ9XVa0Df5wyGaOoeoK&index=3)",
        ],
        [
            "15",
            "Get Started with Cloud Storage",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/725)",
            "[Solution](https://www.youtube.com/watch?v=sgXN29WmKSE)",
        ],
        [
            "16",
            "Get Started with Eventarc",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/727)",
            "[Solution](https://www.youtube.com/playlist?list=PLHfVKuKwHnWOdfKKlIqgBsh6chYtGi-9E)",
        ],
        [
            "17",
            "Get Started with Dataplex",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/726)",
            "[Solution](https://www.youtube.com/playlist?list=PLHfVKuKwHnWOL8WAfH5JOL8FEblPI36Zc)",
        ],
        [
            "18",
            "Tag and Discover BigLake Data",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/753)",
            "[Solution](https://www.youtube.com/watch?v=TaS_48JzzCQ&list=PLHfVKuKwHnWMGjggiFrQHRUXy3cLI3WQc)",
        ],
        [
            "19",
            "Use APIs to Work with Cloud Storage",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/755)",
            "[Solution](https://www.youtube.com/watch?v=xhYvBE5my2c&list=PLHfVKuKwHnWNQeWc_DtZai70is7K39pwV)",
        ],
    ]

    # Convert to DataFrame
    df = pd.DataFrame(
        data, columns=["S. No", "Badge Name", "Badge Link", "Solution Link"]
    )

    # Display Data in Two Columns

    st.success(
        """
        **Important Information**: Badges 5,6,7,8,9 and 10 are pre-assessment badges.
        When you click on the badge link, you’ll see options like _**start challenge**_ or _**go to the pre-assements**_ the ones shown in the image below. 
        Just click on them—you’ll be redirected to a lab If you complete just one lab, you will be able to claim whole badges.

        ✅ **Important**: Make sure to complete the lab in one go; otherwise, you won’t be able to claim the full badge.
        """
    )
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("img1.jpg", caption="Image Caption")
    with col2:
        st.image("img2.jpg", caption="Image Caption")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(df[0:8].to_markdown(index=False), unsafe_allow_html=True)
    with col2:
        st.markdown(df[8:15].to_markdown(index=False), unsafe_allow_html=True)
    col1, col2 = st.columns(2)
