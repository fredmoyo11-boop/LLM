import streamlit as st
import requests
import difflib
from typing import Dict, Any

# Configure the page
st.set_page_config(
    page_title="WritePro - AI Writing Assistant",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Main container styling */
    .main > div {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Header styling */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .main-header h1 {
        font-size: 3rem;
        margin: 0;
        font-weight: 700;
    }
    
    .main-header p {
        font-size: 1.2rem;
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
    }
    
    /* Section styling */
    .section-container {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
        border: 1px solid #e0e0e0;
    }
    
    /* Input area styling */
    .stTextArea textarea {
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        font-size: 14px;
    }
    
    .stTextArea textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Button styling */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    /* Radio button styling */
    .stRadio label {
        font-weight: 500;
    }
    
    /* Slider styling */
    .stSlider label {
        font-weight: 500;
    }
    
    /* Results section */
    .results-container {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
    }
</style>
""", unsafe_allow_html=True)

# Define the backend API URL
API_URL = "http://127.0.0.1:8000"


def send_text_for_assistance(text: str, mode: str, rephrase_style: str = None) -> Dict[str, Any]:
    """
    Send the text to the backend API for assistance.

    Parameters:
        text (str): The original text
        mode (str): The assistance mode ("proofread" or "rephrase")
        rephrase_style (str): The rephrase style if mode is "rephrase"

    Returns:
        Dict containing the API response (including assisted text)
    """
    payload = {
        "text": text,
        "mode": mode
    }
    if rephrase_style:
        payload["rephrase_style"] = rephrase_style

    try:
        response = requests.post(f"{API_URL}/assist", json=payload)
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error connecting to the backend: {e}")
        return {"assisted_text": ""}


def display_diff(original: str, revised: str) -> str:
    """
    Generate a diff view between original and revised text.

    Parameters:
        original (str): The original text
        revised (str): The revised text

    Returns:
        str: The diff text showing changes
    """
    diff = difflib.ndiff(original.splitlines(), revised.splitlines())
    return "\n".join(diff)


def main():
    """Main application function that sets up the Streamlit UI."""

    # Header Section
    st.markdown("""
    <div class="main-header">
        <h1>✍️ WritePro</h1>
        <p>Craft stunning essays effortlessly ✨</p>
    </div>
    """, unsafe_allow_html=True)

    # Create two columns for better layout
    left_col, right_col = st.columns([1, 1], gap="large")

    with left_col:
        # Input section
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.subheader("📝 Your Draft")
            
        original_text = st.text_area(
            "Enter your report draft here:",
            height=300,
            placeholder="Start typing your essay or report here...",
            help="Paste or type your draft text that you'd like to improve",
            key="original_text"
        )
        st.markdown('</div>', unsafe_allow_html=True)

        # Controls section
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.subheader("⚙️ Assistance Settings")

        # Mode selection
        mode = st.radio(
            "Select assistance type:",
            options=["proofread", "rephrase"],
            index=0,
            help="• **Proofread**: Fix grammar and spelling errors\n• **Rephrase**: Rewrite text in different styles",
            horizontal=True
        )

        # Rephrase style dropdown (only show when rephrase is selected)
        rephrase_style = None
        if mode == "rephrase":
            rephrase_style = st.selectbox(
                "Choose rephrase style:",
                options=["formal", "casual", "concise", "creative"],
                index=0,
                help="• **Formal**: Professional and academic tone\n• **Casual**: Friendly and conversational\n• **Concise**: Shorter and more direct\n• **Creative**: More engaging and expressive"
            )

        # Process button
        st.markdown("<br>", unsafe_allow_html=True)
        process_button = st.button(
            "🚀 Enhance My Writing", use_container_width=True)

        st.markdown('</div>', unsafe_allow_html=True)

    with right_col:
        # Results section
        if process_button:
            if not original_text.strip():
                st.warning("⚠️ Please enter some text first.")
            else:
                with st.spinner("✨ Processing your text..."):
                    response = send_text_for_assistance(
                        original_text, mode, rephrase_style)
                    assisted_text = response.get("assisted_text", "")

                # Display results
                if assisted_text:
                    st.markdown('<div class="results-container">',
                                unsafe_allow_html=True)
                    st.subheader("✨ Enhanced Text")
                    st.text_area(
                        "Your improved text:",
                        value=assisted_text,
                        height=200,
                        help="This is your enhanced text with AI improvements"
                    )
                    st.markdown('</div>', unsafe_allow_html=True)

                    # Differences section
                    st.markdown('<div class="section-container">',
                                unsafe_allow_html=True)
                    st.subheader("🔍 Changes Made")
                    diff_text = display_diff(original_text, assisted_text)
                    st.text_area(
                        "Detailed changes:",
                        value=diff_text,
                        height=150,
                        help="Lines starting with '-' were removed, lines starting with '+' were added"
                    )

                    # Enhancement note
                    st.info(
                        "💡 **Coming Soon**: Visual side-by-side comparison with highlighting!")
                    st.markdown('</div>', unsafe_allow_html=True)
        else:
            # Placeholder content when no processing
            st.markdown('<div class="section-container">',
                        unsafe_allow_html=True)
            st.subheader("📋 Instructions")
            st.markdown("""
            **How to use WritePro:**
            
            1. **Enter your text** in the draft area on the left
            2. **Choose assistance type**:
               - *Proofread*: Fix grammar and spelling
               - *Rephrase*: Rewrite in different styles
            3. **Select style** (if rephrasing):
               - *Formal, Casual, Concise, or Creative*
            4. **Click 'Enhance My Writing'** to get results
            
            Your enhanced text will appear here along with a detailed view of all changes made.
            """)
            st.markdown('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
