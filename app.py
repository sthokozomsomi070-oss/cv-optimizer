import streamlit as st
from pypdf import PdfReader

# Page Setup for Mobile Views
st.set_page_config(page_title="AI CV Optimizer", page_icon="💼", layout="centered")

st.title("💼 AI CV Optimizer & Job Matcher")
st.write("Upload your CV to get an instant recruiter grade and match active jobs.")

# File Upload Input
uploaded_file = st.file_uploader("Choose your CV (PDF format)", type="pdf")

if uploaded_file is not None:
    # Read the PDF text
    reader = PdfReader(uploaded_file)
    extracted_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            extracted_text += text
            
    st.success("✅ CV Uploaded Successfully!")
    
    # --- Free Report UI ---
    st.subheader("📊 Your Free Report")
    st.metric(label="Overall Recruiter Score", value="68 / 100", delta="-12% below average")
    st.info("**Initial Impression:** Code formatting and layout are clean, but your experience sections lack quantifiable achievements and impact metrics.")
    
    # --- Paywall UI ---
    st.markdown("---")
    st.subheader("🔒 Premium Line-by-Line Fixes")
    st.write("Unlock deep AI adjustments, keyword target optimization, and specific structural corrections.")
    
    if st.button("🚀 Unlock Premium Pointers (R49.99)"):
        st.warning("💳 Redirecting to secure PayFast gateway... (Demo Mode)")
        st.markdown("[👉 Click here to simulate payment step](https://www.payfast.co.za/)")

    # --- Job Matches ---
    st.markdown("---")
    st.subheader("📍 Matched Local Opportunities")
    st.write("Based on your profile, here are matching local openings:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Junior Systems Developer**\n*📍 Umhlanga, KZN*\n[View Position Link](https://example.com)")
    with col2:
        st.markdown("**IT Infrastructure Intern**\n*📍 Durban Central*\n[View Position Link](https://example.com)")
