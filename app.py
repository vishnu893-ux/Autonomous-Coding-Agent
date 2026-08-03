import streamlit as st
from ai_client import (
    generate_code,
    explain_code,
    generate_documentation
)

st.set_page_config(
    page_title="Autonomous Coding Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Autonomous Coding Agent")

st.write("Generate code using Gemini AI")

language = st.selectbox(
    "Programming Language",
    [
        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript",
        "HTML/CSS",
        "SQL"
    ]
)

prompt = st.text_area(
    "Enter your coding prompt",
    height=200,
    placeholder="Example: Write a Python program to reverse a string."
)
full_prompt = f"""
Generate {language} code for:

{prompt}
"""

if st.button("🚀 Generate Code"):

    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:

        with st.spinner("Generating..."):

            response = generate_code(full_prompt)
            st.session_state["generated_code"] = response

        st.success("Generated Successfully!")

        st.session_state["generated_code"] = response

if "generated_code" in st.session_state:

    st.markdown("## 💻 Generated Code")

    st.code(
        st.session_state["generated_code"],
        language=language.lower()
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📖 Explain Code"):

            with st.spinner("Explaining..."):
                explanation = explain_code(
                    st.session_state["generated_code"]
                )

            st.subheader("📚 Code Explanation")
            st.write(explanation)

    with col2:
        if st.button("📝 Generate Documentation"):

            with st.spinner("Generating Documentation..."):
                documentation = generate_documentation(
                    st.session_state["generated_code"]
                )

            st.subheader("📄 Documentation")
            st.markdown(documentation)

    st.download_button(
        "📥 Download Code",
        st.session_state["generated_code"],
        "generated_code.txt",
        "text/plain"
    )

