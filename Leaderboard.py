import streamlit as st
import pandas as pd

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
        unsafe_allow_html=True,
    )
    st.info("Leaderboard will be available soon. Please check back later.")
    return

    # 1. Upload CSV
    # uploaded_file = None

    # 2. Read into DataFrame
    # if uploaded_file is not None:
    #     df = pd.read_csv(uploaded_file)
    #     if df.empty:
    #         st.info("Leaderboard will be available soon. Please check back later.")
    #         return

    #     df = df.drop(
    #         columns=[
    #             "User Email",
    #             "Google Cloud Skills Boost Profile URL",
    #             "Names of Completed Lab-free Courses",
    #             "Names of Completed Trivia Games",
    #             "Names of Completed Arcade Games",
    #             "Names of Completed Skill Badges",
    #             "Milestone Earned",
    #             "Access Code Redemption Status",
    #         ]
    #     )

    #     # 3. Build a Styler with a hover rule
    #     df["Total"] = (
    #         (df["# of Skill Badges Completed"] // 2)
    #         + df["# of Trivia Games Completed"]
    #         + df["# of Arcade Games Completed"]
    #     )
    #     df["Total"] = df["Total"].astype(int)
    #     df = df.sort_values(by=["Total"], ascending=False)

    #     # Add bonus points based on specific Total values
    #     def calculate_bonus(total):
    #         if total >= 13 and total <= 22:
    #             return 2
    #         elif total >= 22 and total <= 30:
    #             return 8
    #         elif total >= 30:
    #             return 25
    #         else:
    #             return 0

    #     df["Bonus"] = df["Total"].apply(calculate_bonus)
    #     df["Final Arcade Points"] = df["Total"] + df["Bonus"]
    #     df = df.reset_index(drop=True)
    #     st.dataframe(df, use_container_width=True, height=2000, width=800)
    # else:
    #     st.info("Please upload a CSV file to view the leaderboard.")
    #     return


def data():
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
        unsafe_allow_html=True,
    )
    st.info("Leaderboard will be available soon. Please check back later.")
    return


if __name__ == "__main__":
    data()
