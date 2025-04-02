import streamlit as st
# import pandas as pd
# from utils import load_data

def app():
    st.markdown(
    """
    <style>
        @font-face {
            font-family: 'Poppins';
            src: url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        }
    </style>
    <h2 style='text-align: center; font-family: Poppins, sans-serif; color: #8E44AD; font-weight:600; padding: 10px;'>
        🏆 LeaderBoard
    </h2>
    """,
    unsafe_allow_html=True
)

    st.write("Available soon")
    # st.write("Below is the leaderboard data. Use the filters to refine the displayed rows.")
    
    # # Load CSV data
    # df = load_data()
    
    # # Filter by Name substring if the column exists
    # if "Name" in df.columns:
    #     name_filter = st.text_input("Filter by Name", key="leaderboard_name")
    #     if name_filter:
    #         filtered_df = df[df["Name"].str.contains(name_filter, case=False, na=False)]
    #     else:
    #         filtered_df = df.copy()
    # else:
    #     filtered_df = df.copy()
    
    # # Filter by minimum Score if the column exists
    # if "Score" in df.columns:
    #     min_score = st.number_input("Minimum Score", value=0, key="leaderboard_score")
    #     filtered_df = filtered_df[filtered_df["Score"] >= min_score]
    
    # st.dataframe(filtered_df)
