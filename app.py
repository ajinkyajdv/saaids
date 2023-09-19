import streamlit as st
import pandas as pd

# Create a dictionary for navigation items
navigation_items = {
    "Home": "Home",
    "Events": "Events",
    "Registration": "Registration",
    "Admin": "Admin",
}

# Function to load and save event data to a CSV file
def load_event_data():
    try:
        df = pd.read_csv("events.csv")
    except FileNotFoundError:
        df = pd.DataFrame({"Event": [], "Date": [], "Time": []})
    return df

def save_event_data(df):
    df.to_csv("events.csv", index=False)

# Function to load and save registration data to a CSV file
def load_registration_data():
    try:
        df = pd.read_csv("registrations.csv")
    except FileNotFoundError:
        df = pd.DataFrame({"Event": [], "First Name": [], "Last Name": [], "Email": []})
    return df

def save_registration_data(df):
    df.to_csv("registrations.csv", index=False)

# Load event data and registration data
events_df = load_event_data()
registrations_df = load_registration_data()

# Create a selectbox for navigation
selected_item = st.selectbox("Navigation", list(navigation_items.keys()))

# User Authentication (in Admin section)
if selected_item == "Admin":
    password = st.text_input("Enter Admin Password", type="password")
    if password != "AJ":
        st.warning("Incorrect Admin Password. Access Denied!")
        st.stop()  # Stop execution if the password is incorrect.

# Define the title and add a logo (replace 'logo.png' with your logo file)
st.title("Student Association of AI & DS")
#st.image("C:/Users/ajayj/OneDrive/Desktop/saaids/logo.png", use_column_width=True)

# Home Section
if selected_item == "Home":
    st.header("Welcome to the Student Association of AI:robot_face: & DS:bar_chart:")
    st.write("""
     The Student Association of Artificial Intelligence and Data Science at Terna Engineering College is a dynamic and vibrant organization that serves as the epicenter for all activities related to the Artificial Intelligence (AI) and Data Science department. Committed to fostering a holistic educational experience, this association brings together students passionate about cutting-edge technologies and data-driven insights.

**Mission:**
Our mission is to create a thriving community of AI and Data Science enthusiasts within the college. We aim to facilitate knowledge sharing, skill development, and a sense of camaraderie among students interested in these fields.

**Key Objectives:**

**Academic Excellence:** We strive to promote excellence in academics by organizing workshops, seminars, and guest lectures by industry experts and professors. These events provide students with the latest insights and trends in AI and Data Science.

**Technical Competitions:** To encourage innovation and creativity, we organize technical competitions, hackathons, and coding challenges. These events provide a platform for students to apply their knowledge and skills in practical scenarios.

**Cultural Diversity:** Beyond the technical aspects, we celebrate the rich cultural diversity of our members. Cultural festivals, food fairs, and traditional events are organized to foster cross-cultural interactions and appreciation.

**Sports and Fitness:** We believe in a well-rounded education, and physical fitness is an integral part of it. We organize sports tournaments, fitness camps, and recreational activities to promote a healthy lifestyle.

**Community Outreach:** We are committed to giving back to society. Our association engages in community service initiatives and partners with organizations to apply AI and Data Science for social good.

**Events and Activities:**

**Tech Talks:** Regular talks by industry experts and professors on AI and Data Science topics.

**Hackathons:** Competitive coding events where participants can showcase their programming skills.

**Cultural Festivals:** Celebrations of different cultures through music, dance, and cuisine.

**Sports Tournaments:** Organized sporting events for students to compete and stay active.

**Workshops:** Hands-on workshops to learn practical skills in AI and Data Science.

**Community Service:** Initiatives aimed at using AI and Data Science for social and environmental causes.

In summary, the Student Association of Artificial Intelligence and Data Science at Terna Engineering College is a dynamic platform that not only enhances the technical proficiency of its members but also fosters cultural exchange and promotes a well-rounded educational experience. We are dedicated to creating future leaders in AI and Data Science who are not only technically proficient but also socially responsible and culturally aware.

    """)

# Events Section
elif selected_item == "Events":
    st.header("Events")
    # Display a list of events
    st.write(events_df)

# Registration Section
elif selected_item == "Registration":
    st.header("Registration")
    # Create a registration form (customize as needed)
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email")
    event_to_register = st.selectbox("Select an event to register:", events_df["Event"])
    if st.button("Register"):
        # Handle registration logic (e.g., store data in a database)
        registration_data = pd.DataFrame(
            {"First Name": [first_name], "Last Name": [last_name], "Email": [email], "Event": [event_to_register]})
        st.write(registration_data)
        registrations_df = pd.concat([registrations_df, registration_data], ignore_index=True)
        registrations_df.to_csv("registrations.csv", index=False)
        st.success(f"Registered for '{event_to_register}' successfully!")

# Admin Section
elif selected_item == "Admin":
    st.header("Admin Panel")
    # Add event management options here (add/delete events with date and time)
    st.subheader("Manage Events")

    # Display the current event data
    st.write(events_df)

    # Admins can add a new event with date and time
    new_event = st.text_input("New Event Name")
    new_date = st.date_input("New Event Date")
    new_time = st.time_input("New Event Time")
    if st.button("Add Event"):
        if new_event and new_date and new_time:
            new_event_row = pd.DataFrame({"Event": [new_event], "Date": [new_date.strftime("%Y-%m-%d")], "Time": [new_time.strftime("%H:%M")]})
            events_df = pd.concat([events_df, new_event_row], ignore_index=True)
            events_df.to_csv("events.csv", index=False)
            st.success(f"Event '{new_event}' added successfully!")

    # Admins can delete an event
    event_to_delete = st.selectbox("Select an event to delete:", events_df["Event"])
    if st.button("Delete Event"):
        events_df = events_df[events_df["Event"] != event_to_delete]
        events_df.to_csv("events.csv", index=False)
        st.success(f"Event '{event_to_delete}' deleted successfully!")

    # Admins can view registered students for each event
    st.subheader("View Registered Students by Event")
    event_to_view = st.selectbox("Select an event to view registrations:", events_df["Event"])
    st.write("Registered Students:")
    event_registrations = registrations_df[registrations_df["Event"] == event_to_view]
    st.write(event_registrations)

# Optionally, you can add more sections and functionality as needed
