import streamlit as st
import pandas as pd


def app():
    # Weekly Challenges Heading

    st.markdown(
        """
        ### 📌 **Important Notes**  
        - ✅ **Complete all the Badges, Trivia, and Games Before the deadline.**  
        - 🎯 *Plan your daily lab completions efficiently. You can perform 15 labs per days.*  
        - 📅 **Deadlines are strict!** Complete your tasks on time! I am not responsible of any failure** 
        - 🏆 **To find the labs solution, Copy the lab name or Lab code (below lab name) and paste it on Youtube. (Suggested Channel : quick Lab, Cloud Hustlers, Btechy)**
        """,
        unsafe_allow_html=True,
    )

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

    week2()
    week1()


def week1():

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
            "Get Started with Pub/Sub",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/728)",
            "[Solution](https://www.youtube.com/watch?v=nDDIobuamAo)",
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

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown(df2.to_markdown(index=False), unsafe_allow_html=True)


# Important Notes Section


def week2():

    # Challenge Duration Heading
    st.markdown(
        """
            <h2 style='text-align: center; font-family: Poppins, sans-serif; color: #D35400; font-weight:600; padding: 10px;'>
                🚀 Challenge from April 9 to April 15
            </h2>
            """,
        unsafe_allow_html=True,
    )
    
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
    col1,col2 = st.columns([1,1])
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



# Important Notes Section


if __name__ == "__main__":
    app()
