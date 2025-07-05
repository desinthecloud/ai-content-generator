import streamlit as st
import requests

st.title("👩🏾 AI Content Generator with Bedrock")
st.markdown("Enter a prompt and generate high-quality content using Amazon Bedrock + Claude.")

prompt = st.text_area("Your Prompt:", height=150)

if st.button("Generate"):
    if not prompt:
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating content..."):
            url = "https://qkp8i4hxg6.execute-api.us-east-1.amazonaws.com/prod/generate"  # <- Update this
            headers = {"Content-Type": "application/json"}
            payload = {"prompt": prompt}

            try:
                response = requests.post(url, json=payload)
                response.raise_for_status()
                result = response.json().get("response")
                st.subheader("📝 Generated Content")
                st.write(result)
            except requests.exceptions.RequestException as e:
                st.error(f"Error calling API: {e}")

