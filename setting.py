import streamlit as st

def configure_page():
    """
    Configure Streamlit page settings.
    """
    st.set_page_config(
        page_title="Object Detection using YOLOv8",  # Setting page title
        page_icon="🏡",     # Setting page icon
        layout="wide",      # Setting layout to wide
        initial_sidebar_state="expanded"    # Expanding sidebar by default
    )

def get_model_confidence():
    """
    Get model confidence from user input.
    """
    confidence = float(st.slider(
        "Select Model Confidence", 25, 100, 40)) / 100
    return confidence

def select_labels(available_labels):
    """
    Select labels from available options.
    """
    selected_labels = st.multiselect(
        "Select Labels",
        available_labels
    )
    if not selected_labels:
        selected_labels = available_labels
    return selected_labels
