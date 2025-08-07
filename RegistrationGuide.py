import streamlit as st


def app():
    st.markdown(
        """
        <style>
            @font-face {
                font-family: 'Poppins';
                src: url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
            }
        </style>
        <h1 style='text-align: center; font-family: Poppins, sans-serif; color: #FF5733; font-weight:600; padding: 20px; font-size: 36px;'>
            🎯 Google Cloud Arcade Facilitator 2025 Guide
        </h1>
        """,
        unsafe_allow_html=True,
    )

    # Facilitator Information
    st.markdown(
        """
        <div style='background-color: #2D2D2D; padding: 15px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #FFC107;'>
            <h3 style='color: #FFC107; margin: 0;'>📋 Facilitator Information</h3>
            <p style='margin: 10px 0; color: #E1E1E1;'><strong>Facilitator:</strong> <a href='https://www.linkedin.com/in/mayanksharmams/' target='_blank' style='color: #4FC3F7;'>Mayank Sharma</a></p>
            <p style='margin: 5px 0; background-color: #1E1E1E; color: #FFD700; padding: 8px; border-radius: 5px; display: inline-block;'><strong>Referral Code:</strong> <span style='font-family: monospace; font-size: 16px; font-weight: bold;'>GCAF25C2-IN-LWW-AM7</span></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Profile Setup Section
    st.markdown(
        """
        <h2 style='text-align: center; font-family: Poppins, sans-serif; color: #3498DB; font-weight:600; padding: 15px;'>
            🔧 Profile Setup
        </h2>
        """,
        unsafe_allow_html=True,
    )

    profile_setup_steps = [
        {
            "step": "Step 1: Email ID Requirements",
            "content": "To participate in the program, your **email ID must be created on or after July 31, 2025**, and you must be 18 years or older at the time of creation. If not, please ensure you select an age of 18 or above when creating your Gmail ID to be eligible for participation.",
        },
        {
            "step": "Step 2: Create Google Cloud Skills Boost Account",
            "content": "Go to the [Google Cloud Skills Boost](https://www.cloudskillsboost.google/) and create your account with the **same email ID** that you created in Step 1.",
        },
        {
            "step": "Step 3: Access Profile Settings",
            "content": "Once you log in with the same email ID (Step 1), click on your **profile picture** in the top-left corner. Then click on the **settings** option.\n\n**Navigation:** Profile picture → Settings option",
            "image": "images/image3.png",
        },
        {
            "step": "Step 4: Find Leaderboards & Leagues",
            "content": "Scroll down until you are able to see **Leaderboards & Leagues** section in the settings.",
            "image": "images/image12.png",
        },
        {
            "step": "Step 5: Enable All Checkboxes",
            "content": "Click on **all the checkboxes** in the Leaderboards & Leagues section as shown below. Then click on **Update Settings**.",
            "image": "images/image4.png",
        },
        {
            "step": "Step 5b: Save Public Profile",
            "content": "When you click on update settings, you will see **Google Cloud Skills Boost public profile**. **Save it** - This is most important for your participation.",
            "image": "images/image6.png",
        },
        {
            "step": "Step 6: Subscribe to Arcade",
            "content": "Go to the Arcade website: [Arcade | Google Cloud Skills Boost](https://go.cloudskillsboost.google/arcade). Then click on the **Subscribe Here** button.",
            "image": "images/image5.png",
        },
        {
            "step": "Step 7: Fill Initial Form",
            "content": "Fill the form with the **same Email ID** that you created in Step 1. Enter the same email address consistently.",
            "image": "images/image7.png",
        },
        {
            "step": "Step 8: Complete Registration",
            "content": "Click on next, fill the rest of the form. Go through all the steps and make sure you have done everything correctly.",
        },
        {
            "step": "Step 9: Wait for Form Opening",
            "content": "If you have completed all the steps, wait till **August 4, 2025, 5pm** for the registration form to open.",
        },
    ]

    for step_info in profile_setup_steps:
        with st.expander(step_info["step"]):
            st.markdown(step_info["content"])
            if "image" in step_info:
                st.image(
                    step_info["image"],
                    caption=f"Screenshot for {step_info['step']}",
                    use_container_width=True,
                )

    # Registration Form Prerequisites
    st.markdown(
        """
        <h2 style='text-align: center; font-family: Poppins, sans-serif; color: #E74C3C; font-weight:600; padding: 15px;'>
            📋 Registration Form Prerequisites
        </h2>
        """,
        unsafe_allow_html=True,
    )
    data = """
        <div style='background-color: #2D2D2D; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #E74C3C;'>
            <h3 style='color: #FF6B6B; margin-top: 0;'>🚨 Important Instructions Before Registration! 🚨</h3>
            <p style='color: #E1E1E1;'><strong>Please ensure you have ALL the following information ready before filling out the registration form:</strong></p>
            <ul style='margin: 15px 0; padding-left: 20px; color: #E1E1E1;'>
                <li>✅ <strong>Google Cloud Skills Boost Profile URL</strong> (see Step 5)</li>
                <li>✅ <strong>Correct Email Address</strong> (see Step 1 - avoid typos!)</li>
                <li>✅ <strong>Referral Code:</strong> <span style='background-color: #FFEB3B; color: #000; padding: 3px 6px; border-radius: 3px; font-family: monospace;'>GCAF25C2-IN-LWW-AM7</span> (double-check, no mistakes!)</li>
                <li>✅ Save all this info somewhere safe (WhatsApp, Notes, Notepad, etc.)</li>
                <li>✅ Double-check spelling and avoid trailing spaces</li>
            </ul> 
            <div style='background-color: #FF9800; color: #000; padding: 10px; border-radius: 5px; margin: 10px 0;'>
                <p style='margin: 0;'><strong>⚠️ Note:</strong> Incorrect or incomplete information, or errors in the referral code, may lead to disqualification from the program.</p>
            </div>
            <div style='background-color: #2196F3; color: #FFF; padding: 10px; border-radius: 5px; margin: 10px 0;'>
                <p style='margin: 0;'><strong>🕐 Registration Deadline:</strong> August 4, 2025, 12:00 PM – The form will be closed after this time.</p>
            </div>
            <p style='margin-bottom: 0; color: #E1E1E1;'>👉 Limited slots available! Register as soon as possible and carefully. Be ready at 5:00 PM, August 4.</p>
        </div>
        """

    st.markdown(
        data,
        unsafe_allow_html=True,
    )

    # Form Filling Process
    st.markdown(
        """
        <h2 style='text-align: center; font-family: Poppins, sans-serif; color: #2ECC71; font-weight:600; padding: 15px;'>
            📝 Form Filling Process
        </h2>
        """,
        unsafe_allow_html=True,
    )

    form_filling_steps = [
        {
            "step": "Step 10: Open Registration Form",
            "content": "Click on the Link to open the Form: [Form Link](https://docs.google.com/forms/d/e/1FAIpQLSfzuDW9xrckFAbbK8BgBpyFI_iyzjXdCHcngS-pmw3HQ4qPAQ/viewform)",
        },
        {
            "step": "Step 11: Sign In",
            "content": "Sign in with the **email address** you used in Step 1. Then click on **next** to proceed further.",
            "image": "images/image10.png",
        },
        {
            "step": "Step 12: Accept Terms",
            "content": "Click on **'Yes, I accept the terms and Conditions.'** Then click on **next**.",
            "image": "images/image8.png",
        },
        {
            "step": "Step 13: Fill Personal Information",
            "content": "Fill in **Email ID** (Step 1), **Name**, **Gender**, **Country**, **Identity**, and **Year of graduation**. See below step for referral code.",
        },
        {
            "step": "Step 14: Most Important Step",
            "content": "**Click yes** on the checkbox for important agreements. This is a crucial step that must not be missed.",
            "image": "images/image13.png",
        },
        {
            "step": "Step 15: Enter Referral Code",
            "content": "Fill the **referral code**: `GCAF25C2-IN-LWW-AM7` and click on **option 1** of the next question. **Note:** Copy without any mistake. Then click on **Next**.",
            "image": "images/image11.png",
        },
        {
            "step": "Step 16: Enter Public Profile",
            "content": "Enter the **Public profile URL** (from Steps 3, 4, 5). Copy it and then paste it carefully.",
            "image": "images/image15.png",
        },
        {
            "step": "Step 17: Submit Form",
            "content": "Click on **next** and fill the rest of the form. Don't do anything after next, just fill the required fields and click on **Submit**.",
        },
    ]

    for step_info in form_filling_steps:
        with st.expander(step_info["step"]):
            st.markdown(step_info["content"])
            if "image" in step_info:
                st.image(
                    step_info["image"],
                    caption=f"Screenshot for {step_info['step']}",
                    use_container_width=True,
                )

    # Post-Registration Process
    st.markdown(
        """
        <h2 style='text-align: center; font-family: Poppins, sans-serif; color: #9B59B6; font-weight:600; padding: 15px;'>
            ✉️ Post-Registration Process
        </h2>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style='background-color: #333; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #9B59B6;'>
            <h3 style='color: #BB86FC; margin-top: 0;'>📧 Email Verification</h3>
            <p style='color: #E1E1E1;'>After filling out the form, you will receive an email at your registered email ID (Step 1). Open the email, where you will find a copy of the form. Review the form and locate the referral code section.</p>
            <p style='color: #E1E1E1;'><strong>If the referral code is shown correctly, then well done - you have completed all the steps!</strong></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Add email verification screenshot
    st.image(
        "images/image2.png",
        caption="Email verification - Referral code confirmation",
        use_container_width=True,
    )

    post_registration_steps = [
        {
            "step": "Step 17: Confirmation Email",
            "content": "You will get a **confirmation email within 24-48 hours**. After receiving the confirmation email, **watch the following video carefully**. It's crucial to follow the steps exactly as shown.\n\n**Video Link:** [Credit Redemption Guide](https://youtu.be/5qDvS0yLTds?si=B99X68FRdFBQVYn8)",
        },
        {
            "step": "Step 18: Verify Credits",
            "content": "Once you've followed the video instructions, your **Cloud Skills Boost account** should display either **609 or 644 credits**.\n\n**If you got the credits, please report it to the group.**",
        },
    ]

    for step_info in post_registration_steps:
        with st.expander(step_info["step"]):
            st.markdown(step_info["content"])
            if "image" in step_info:
                st.image(
                    step_info["image"],
                    caption=f"Screenshot for {step_info['step']}",
                    use_container_width=True,
                )

    # Important Notes Section
    st.markdown(
        """
        <h2 style='text-align: center; font-family: Poppins, sans-serif; color: #F39C12; font-weight:600; padding: 15px;'>
            ⚠️ Important Notes & Tips
        </h2>
        """,
        unsafe_allow_html=True,
    )

    important_notes = [
        {
            "title": "🎯 Key Requirements",
            "content": "• Email must be created on or after July 31, 2025\n• Age must be 18+ at the time of creation\n• Use the SAME email ID throughout all steps\n• Double-check all information before submitting",
        },
        {
            "title": "🔑 Referral Code",
            "content": "**GCAF25C2-IN-LWW-AM7**\n\n⚠️ Copy this exactly - no spaces, no typos!\n⚠️ Incorrect referral code = disqualification",
        },
        {
            "title": "📅 Important Dates",
            "content": "• **Registration Opens:** August 4, 2025 at 5:00 PM\n• **Registration Closes:** August 4, 2025 at 12:00 PM (next day)\n• **Confirmation Email:** Within 24-48 hours after registration",
        },
        {
            "title": "💡 Pro Tips",
            "content": "• Save all information in a safe place before starting\n• Have your Google Cloud Skills Boost profile ready\n• Test your profile URL before submitting\n• Be ready exactly at 5:00 PM on August 4th\n• Limited slots available - register quickly!",
        },
    ]

    for note in important_notes:
        with st.expander(note["title"]):
            st.markdown(note["content"])

    # Contact Information
    st.markdown(
        """
        <div style='background-color: #2D2D2D; padding: 20px; border-radius: 10px; margin: 30px 0; border-left: 5px solid #4CAF50;'>
            <h3 style='color: #4CAF50; margin-top: 0;'>💬 Need Help?</h3>
            <p style='color: #E1E1E1;'>If you have any questions, feel free to ask in the group. The facilitator is here to help you! 😊</p>
            <p style='color: #E1E1E1;'><strong>Facilitator:</strong> <a href='https://www.linkedin.com/in/mayanksharmams/' target='_blank' style='color: #4FC3F7;'>Mayank Sharma</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style='text-align: center; margin: 30px 0; padding: 20px; background-color: #2D2D2D; border-radius: 10px;'>
            <h3 style='color: #4CAF50; margin: 0;'>🎓 Good Luck with Your Registration!</h3>
            <p style='margin: 10px 0; color: #E1E1E1;'>Follow all steps carefully and you'll be part of the Google Cloud Arcade Facilitator Program 2025!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
