import traceback
import streamlit as st
from slide_gen import generate_presentation

def create_ui():
    st.write("""
# PowerPoint Generator
### Creating PowerPoint slides on your topic
""")

    # Sidebar for template selection
    template_option = st.sidebar.radio(
        "Choose a PowerPoint Template",
        ("Blank", "lon_boardroom", "Urban_monochrome")
    )

    content = st.text_area(label="Enter your topic:", height=40)

    if content:
        try:
            # Pass the selected template to the function
            filename = generate_presentation(content, template_option)
            st.success(f"File generated successfully: {filename}")
            st.write("If you can't find the file in the default location, check your Documents folder.")
        except Exception as e:
            st.error("Error generating slides.")
            st.error(str(e))
            st.error(traceback.format_exc())

if __name__ == "__main__":
    create_ui()