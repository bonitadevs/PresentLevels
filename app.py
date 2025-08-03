import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="PresentLevels", layout="centered")

st.title("PresentLevels")
st.subheader("Your Smart IEP Goal & Objective Builder")

with st.form("iep_form"):
    student_name = st.text_input("Student Name")
    grade = st.selectbox("Grade", ["K", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
    disability = st.selectbox("Primary Disability", ["SLD", "Autism", "ED", "ID", "Other Health Impairment", "Speech/Language", "Other"])
    goal_area = st.selectbox("Focus Area", ["Reading", "Math", "Writing", "Behavior", "Executive Function", "Social Skills"])
    specific_need = st.text_area("Describe the student's specific need")

    # ✅ These need to stay inside the form
    common_accommodations = st.multiselect(
        "Select key accommodations (you can pick more than one):",
        [
            "Graphic organizers",
            "Repeated directions",
            "Extended time",
            "Preferential seating",
            "Visual supports",
            "Checklists",
            "Breaks between tasks",
            "Use of calculator",
            "Small group instruction"
        ]
    )

    custom_accommodation = st.text_input("Any additional accommodation(s)? (Optional)")

    submitted = st.form_submit_button("Generate IEP Goal")

if submitted:
    st.success(f"Here's a drafted IEP goal for {student_name}:")

    end_date = (datetime.now() + timedelta(days=365)).strftime("%B %Y")
    accuracy = "80% accuracy in 4 out of 5 trials"

    all_accommodations = common_accommodations.copy()
    if custom_accommodation:
        all_accommodations.append(custom_accommodation)

    accommodations_text = ", ".join([acc.lower() for acc in all_accommodations])

    goal = f"Given {accommodations_text}, {student_name} will demonstrate improved {goal_area.lower()} skills related to {specific_need.lower()}, with at least {accuracy}, by {end_date}."

    objectives = [
        f"1. With teacher support, {student_name} will complete {goal_area.lower()} tasks addressing {specific_need.lower()} with {accuracy}.",
        f"2. {student_name} will increase independence in {goal_area.lower()} tasks by using strategies (e.g., {accommodations_text}) across multiple settings.",
        f"3. {student_name} will show progress on {goal_area.lower()} IEP benchmarks with reduced prompting over 6 weeks."
    ]

    st.markdown(f"**Goal:** {goal}")
    st.markdown("**Objectives:**")
    for obj in objectives:
        st.markdown(f"- {obj}")
