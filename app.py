import streamlit as st
from pathlib import Path
import sys

# Add the project root to the path
sys.path.append(str(Path(__file__).parent))

from utils.detector import WeedDetector
from utils.visualizer import display_results, display_statistics
from utils.config import MODEL_CONFIGS, KAGGLE_LINKS
import tempfile
import cv2

# Page configuration
st.set_page_config(
    page_title="Weed Detection System",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #2E7D32;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #558B2F;
        margin-bottom: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 1.1rem;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">🌿 Weed Detection System</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Upload images or videos to detect weeds using advanced AI models</p>', unsafe_allow_html=True)

# Initialize session state
if 'results' not in st.session_state:
    st.session_state.results = None

# Create tabs
tab1, tab2 = st.tabs(["🔍 Detection", "📊 Kaggle Notebooks"])

with tab1:
    # Model selection
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Model Configuration")
        selected_model = st.selectbox(
            "Select Detection Model",
            options=list(MODEL_CONFIGS.keys()),
            help="Choose the AI model for weed detection"
        )
        
        # Display model info
        model_info = MODEL_CONFIGS[selected_model]
        st.info(f"**Type:** {model_info['type']}\n\n**Description:** {model_info['description']}")
        
        confidence_threshold = st.slider(
            "Confidence Threshold",
            min_value=0.1,
            max_value=1.0,
            value=0.25,
            step=0.05,
            help="Minimum confidence score for detections"
        )
    
    with col2:
        st.subheader("Upload Media")
        upload_option = st.radio(
            "Select input type:",
            ["Image", "Video"],
            horizontal=True
        )
        
        if upload_option == "Image":
            uploaded_file = st.file_uploader(
                "Upload an image",
                type=['jpg', 'jpeg', 'png'],
                help="Supported formats: JPG, JPEG, PNG"
            )
        else:
            uploaded_file = st.file_uploader(
                "Upload a video",
                type=['mp4', 'avi', 'mov'],
                help="Supported formats: MP4, AVI, MOV"
            )
    
    # Detect button
    col_detect1, col_detect2, col_detect3 = st.columns([1, 1, 1])
    with col_detect2:
        detect_button = st.button("🚀 Detect Weeds", use_container_width=True, type="primary")
    
    if detect_button:
        # Initialize detector
        detector = WeedDetector(
            model_path=model_info['path'],
            confidence_threshold=confidence_threshold
        )
        
        # Check if file is uploaded, otherwise use sample
        if uploaded_file is None:
            st.warning("No file uploaded. Using sample image for detection...")
            sample_path = Path("sample_image.png")
            if sample_path.exists():
                input_source = str(sample_path)
                is_video = False
            else:
                st.error("Sample image not found at 'sample_image.png'. Please upload a file.")
                st.stop()
        else:
            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as tmp_file:
                tmp_file.write(uploaded_file.read())
                input_source = tmp_file.name
            is_video = upload_option == "Video"
        
        # Perform detection
        with st.spinner(f"Detecting weeds using {selected_model}..."):
            if is_video:
                results = detector.detect_video(input_source)
            else:
                results = detector.detect_image(input_source)
            
            st.session_state.results = results
    
    # Display results
    if st.session_state.results is not None:
        st.markdown("---")
        st.subheader("Detection Results")
        
        results = st.session_state.results
        
        if results['type'] == 'image':
            display_results(
                results['original'],
                results['annotated'],
                results['detections'],
                is_video=False
            )
        else:
            display_results(
                results['video_path'],
                results['output_path'],
                results['all_detections'],
                is_video=True
            )
        
        # Display statistics
        st.markdown("---")
        display_statistics(results['detections'] if results['type'] == 'image' else results['all_detections'])

with tab2:
    st.subheader("📚 Kaggle Notebook Links")
    st.markdown("Explore the training notebooks and experiments for each model:")
    
    # Create a nice layout for Kaggle links
    for model_name, link in KAGGLE_LINKS.items():
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{model_name}**")
                st.caption(MODEL_CONFIGS[model_name]['description'])
            with col2:
                st.link_button("Open Notebook", link, use_container_width=True)
            st.markdown("---")
    
    st.info("💡 **Tip:** These notebooks contain detailed information about model training, evaluation metrics, and implementation details.")