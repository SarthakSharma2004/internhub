import streamlit as st
from matcher import InternshipMatcher
from samples import SAMPLE_PROFILE, SAMPLE_INTERNSHIP

st.set_page_config(page_title="Internship Match AI", layout="centered")

matcher = InternshipMatcher()


#---------------------------------------------------
# Streamlit UI
#----------------------------------------------------
def home():
    """Home section of the application."""

    st.title("🎯 InternHub - Internship Match Analyzer")
    st.subheader("Welcome! Let's analyze your profile.")
    st.markdown("<br><br>", unsafe_allow_html=True)

#---------------------------------------------------
# User Input
#---------------------------------------------------

def profile():
    """Handles user input and interaction."""

    use_sample = st.checkbox("⚡ Use sample data for testing")

    if use_sample:
        # Use predefined sample data
        student_profile = SAMPLE_PROFILE
        internship_description = SAMPLE_INTERNSHIP

        st.success("Sample data loaded!")

    else:
        # Manual input mode
        skills = st.text_input("Skills (comma separated)", placeholder="Add your skills here...")
        experience = st.selectbox("Experience", ["0-1", "2-5", ">5"])
        education = st.text_input("Education", placeholder="eg. B.Tech CSE, 4th Year, XYZ University")
        projects = st.text_input("Projects", placeholder="eg. Built a web app for XYZ Company")
        other_achievements = st.text_input("Other Achievements (Optional)", placeholder="eg. Won a hackathon")

        student_profile = f"""
Skills: {skills}
Experience: {experience}
Education: {education}
Projects: {projects}
Others: {other_achievements}
"""

        st.markdown("<br><br>", unsafe_allow_html=True)

        internship_description = st.text_area("Enter the internship description")

    # Analyze button (common for both modes)
    if st.button("Analyze"):
        if not student_profile or not internship_description:
            st.warning("Please fill in all required fields.")
        else:
            with st.spinner("Analyzing..."):
                result = matcher.analyze(student_profile, internship_description)

                st.subheader("🔍 Analysis Result")
                st.write(result)



#---------------------------------------------------
# Main function
#---------------------------------------------------

if __name__ == "__main__":
    home()
    profile()












