import streamlit as st
from components import *

st.title("Cover Page Generating Engine:")
st.subheader("Information Form:")

form = cover_page_form.Form()
form.run()

st.subheader("🎨 Choose your designs here:")
t=template.Template()

if "cover_page_details" in st.session_state:
    col1, col2, col3 = st.columns(3)

    details = st.session_state["cover_page_details"]
        
    with col1:
        st.image("assets/images/template1.png", caption="Template 1")
        if st.button("Generate PDF", key="template1"):
            t.template1(
                details["stream"], details["sem"], details["univ"], details["roll"],
                details["reg"], details["paper_name"], details["paper_code"], details["sub"]
            )
        
        st.image("assets/images/template4.png", caption="Template 4")
        if st.button("Generate PDF", key="template4"):
            t.template4(
                details["stream"], details["sem"], details["univ"], details["roll"],
                details["reg"], details["paper_name"], details["paper_code"], details["sub"]
            )
    
    with col2:
        st.image("assets/images/template2.png", caption="Template 2")
        if st.button("Generate PDF", key="template2"):
            t.template2(
                details["stream"], details["sem"], details["univ"], details["roll"],
                details["reg"], details["paper_name"], details["paper_code"], details["sub"]
            )
        
        st.image("assets/images/template5.png", caption="Template 5")
        if st.button("Generate PDF", key="template5"):
            t.template5(
                details["stream"], details["sem"], details["univ"], details["roll"],
                details["reg"], details["paper_name"], details["paper_code"], details["sub"]
            )

    with col3:
        st.image("assets/images/template3.png", caption="Template 3")
        if st.button("Generate PDF", key="template3"):
            t.template3(
                details["stream"], details["sem"], details["univ"], details["roll"],
                details["reg"], details["paper_name"], details["paper_code"], details["sub"]
            )
        
        st.image("assets/images/template6.png", caption="Template 6")
        if st.button("Generate PDF", key="template6"):
            t.template6(
                details["stream"], details["sem"], details["univ"], details["roll"],
                details["reg"], details["paper_name"], details["paper_code"], details["sub"]
            )
            
else:
    st.info("📝 Please submit the form above to unlock the design section.")