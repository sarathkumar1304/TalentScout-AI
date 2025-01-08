# import streamlit as st


# class DataProcessor:
#     def manual_entry_form(self):
#         with st.form("manual_entry_form"):
#             name = st.text_input("Full Name")
#             email = st.text_input("Email Address")
#             phone = st.text_input("Phone Number")
#             experience = st.number_input("Years of Experience", min_value=0, step=1)
#             position = st.text_input("Desired Position")
#             location = st.text_input("Current Location")
#             tech_stack = st.text_area("Tech Stack (comma-separated)").split(",")
#             submit = st.form_submit_button("Submit")
#             if submit:
#                 self.display_submitted_data(
#                 name, email, phone, experience, position, location, tech_stack
#             )
#         return tech_stack


#     @staticmethod
#     def display_submitted_data(name, email, phone, experience, position, location, tech_stack):
#         """Displays the submitted form data."""
#         st.markdown("### Submitted Information")
#         st.write(f"**Full Name:** {name}")
#         st.write(f"**Email Address:** {email}")
#         st.write(f"**Phone Number:** {phone}")
#         st.write(f"**Years of Experience:** {experience}")
#         st.write(f"**Desired Position:** {position}")
#         st.write(f"**Current Location:** {location}")
#         st.write(f"**Tech Stack:** {', '.join(tech_stack)}")

            
    
        

import streamlit as st

class ManualEntry:
    def manual_entry_form(self):
        with st.form("manual_entry_form"):
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            phone = st.text_input("Phone Number")
            experience = st.number_input("Years of Experience", min_value=0, step=1)
            position = st.text_input("Desired Position")
            location = st.text_input("Current Location")
            tech_stack = st.text_area("Tech Stack (comma-separated)").split(",")
            submit = st.form_submit_button("Submit")
            
            # Check if any field is empty
            if submit:
                missing_fields = []
                
                # Check for empty fields
                if not name:
                    missing_fields.append("Full Name")
                if not email:
                    missing_fields.append("Email Address")
                if not phone:
                    missing_fields.append("Phone Number")
                if experience == 0:
                    missing_fields.append("Years of Experience")
                if not position:
                    missing_fields.append("Desired Position")
                if not location:
                    missing_fields.append("Current Location")
                if not tech_stack or all(not tech.strip() for tech in tech_stack):
                    missing_fields.append("Tech Stack")
                
                if missing_fields:
                    # Show a message if any fields are missing
                    st.warning(f"Please provide details for the following fields: {', '.join(missing_fields)}")
                else:
                    self.display_submitted_data(name, email, phone, experience, position, location, tech_stack)
                    return tech_stack
        

    def display_submitted_data(self, name, email, phone, experience, position, location, tech_stack):
        st.success("Data Submitted Successfully!")
        st.write(f"**Name:** {name}")
        st.write(f"**Email:** {email}")
        st.write(f"**Phone:** {phone}")
        st.write(f"**Experience:** {experience} years")
        st.write(f"**Position:** {position}")
        st.write(f"**Location:** {location}")
        st.write(f"**Tech Stack:** {', '.join(tech_stack)}")
