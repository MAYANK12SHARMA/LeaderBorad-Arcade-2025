import streamlit as st
from utils import inject_heading, set_custom_style
import Leaderboard
import CheckYourStatus
import FAQ
import YourFacilitator
import WeeklyChallenge
import LabFreeCourse

# Set page configuration
st.set_page_config(page_title="Google Cloud Arcade Facilitator", layout="wide")

# Display the sidebar logo
# display_sidebar_logo()..

# Display the common heading on all tabs
inject_heading()

set_custom_style()

st.markdown(
    """
<div style='
    background-color: #f0f8ff;
    padding: 20px 25px;
    border-radius: 15px;
    border-left: 6px solid #4CAF50;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    font-family: sans-serif;
'>
    <h4 style='margin-bottom:10px;color:black;'>📢 Important Message</h4>
    <p style='margin:0; font-size: 16px; color: #333;font-weight: 800;'>
        I sincerely apologize, but my WhatsApp account has been unexpectedly banned due to reasons beyond my knowledge or control. I understand how important it is for us to stay connected, and I truly regret any inconvenience this may cause. <br><br>
        In the meantime, I kindly request you to stay updated and connected by joining my Telegram group and channel:
        <ul>
            <li style='margin: 5px 0;'><a href="https://t.me/+M8VNXYZnAMQwYjU9" target="_blank" style="color: Blue;font-weight: 700;">Telegram Group : For Discussion </a></li>
            <li style='margin: 5px 0;'><a href="https://t.me/googlecloudfacilitator2025" target="_blank" style="color: Blue;font-weight: 700;">Telegram Channel : For Annoucement</a></li>
        </ul>
        <br>
        <p style='margin: 0; font-size: 16px; color: #333;font-weight: 800;'>
        Your support means a lot to me. If possible, please consider sharing this message or the group link with others in the group so they can also stay informed and connected.
        </p>
        <br><br>
    </p>
</div>
    <br><br>

""",
    unsafe_allow_html=True,
)


# Create tabs for each section
tabs = st.tabs(
    [
        "Leaderboard",
        "Check Your Status",
        "Weekly Challenge",
        "Lab Free Courses",
        "FAQ",
        "Your Facilitator",
    ]
)

st.markdown(
    """
            <style>
                .stTabs [data-baseweb="tab-list"] {
                    display: flex;
                    justify-content: center;
                }
                .stTabs [data-baseweb="tab"] {
                    height: 40px;
                    white-space: pre-wrap;
                    width: 300px;
                }
                
            </style>
            """,
    unsafe_allow_html=True,
)


with tabs[0]:
    Leaderboard.app()

with tabs[1]:
    CheckYourStatus.app()

with tabs[2]:
    WeeklyChallenge.app()

with tabs[3]:
    LabFreeCourse.app()

with tabs[4]:
    FAQ.app()

with tabs[5]:
    YourFacilitator.app()
