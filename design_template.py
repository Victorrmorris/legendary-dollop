import streamlit as st

st.title("Civilian Job Design Template")

options = ["Unit Supply Specialist"]
Military_Occupational_Specialty = st.multiselect("Select your MOS title", options, default=["Unit Supply Specialist"])

military_experience = st.number_input("Enter your military experience level (in years)", min_value=0, max_value=40, value=0)

options = ["Resource Management and Operations", "Coordination and Time Management", "Management of Financial and Material Resources", "Project Management", "Problem-Solving"]

skills = st.multiselect("Select your transferable knowledge and skills", options, default=["Resource Management and Operations"])

options = ["Working with people", "Service Orientation", "Self Management", "Attention to Detail", "Trustworthiness"]
           
attitudes = st.multiselect("Select your transferrable attitudes and beliefs", options, default=["Working with people"])

options = ["Information technology", "Construction", "Drink manufacturing", "Personal services", "Direct retail", "Finishing contracting", "Real estate", "Trucking", "Architectural engineering", "Healthcare", "Financial services", "Transportation"]
           
industries = st.multiselect("Select your ideal civilian industries", options, default=["Information technology"])

options = ["Career development and advancement", "Adequate total compensation","Meaningful work", "Workplace flexibility","Reliable and supportive people at work", "support for health and well being", "sustainable work expectations", "caring and inspiring leaders", "inclusive and welcoming community", "geographic ties and travel demands", "safe workplace environment", "resource accessibility"]

employee_experience_factors = st.multiselect("Select your ideal civilian employee experience factors", options, default=["Adequate total compensation"])

options = ["1-20 employees", "21-100 employees", "101-200 employees", "201-500 employees", "501-1000 employees", "1001+ employees"]

ideal_company_size = st.multiselect("Select your ideal company size", options, default=["1001+ employees"])

options = ["Supply Chain Manager", "Financial Manager", "Market Research Analyst", "Logistician", "Management Analyst"]

ideal_civilian_roles = st.multiselect("Select civilian roles to explore", options, default=["Supply Chain Manager"])

options = ["Sales, Communication and Marketing of Products", "Customer Experience", "Data Analysis", "Teaching and Training", "Developing alliances, contacts or partnerships"]

ideal_civilian_work_activties = st.multiselect("Select your ideal civilian work activities", options, default=["Customer Experience"])

minimum_expected_salary = st.number_input("Enter your minimum expected salary (in dollars)", min_value=0, max_value=150000, value=0)


st.button("Submit")
agreement = st.checkbox("Test")
if agreement:
    st.write("You selected: ", skills)
    st.write("Military experience: ", military_experience, " years")
