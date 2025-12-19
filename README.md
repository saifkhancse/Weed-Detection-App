# 🌿 AI-Powered Weed Detection System

<div align="center">

**A comprehensive deep learning application for automated weed detection in agricultural fields using state-of-the-art YOLO models with supervised, semi-supervised, and self-supervised learning approaches.**

[Demo](#-demo) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Models](#-models) • [Notebooks](#-notebooks)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Demo](#-demo)
- [Features](#-features)
- [Models](#-models)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Notebooks](#-notebooks)
- [Technologies Used](#-technologies-used)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🌟 Overview

This project implements an end-to-end weed detection system using advanced computer vision techniques and deep learning models. The system provides real-time detection capabilities for both images and videos, with comprehensive analytics and visualizations.

### Key Highlights

- 🎯 **6 Pre-trained Models**: Choose from supervised, semi-supervised, and self-supervised learning approaches
- 📸 **Multi-format Support**: Process both images (JPG, PNG) and videos (MP4, AVI, MOV)
- 📊 **Rich Analytics**: Detailed statistics, interactive charts, and confidence metrics
- 🚀 **Easy to Use**: User-friendly web interface built with Streamlit
- 🔬 **Research-backed**: All models trained on comprehensive datasets with Kaggle notebooks included

---


## ✨ Features

### Core Functionality

- ✅ **Multiple Model Selection**: 6 different pre-trained models with varying architectures
- ✅ **Real-time Detection**: Fast inference on images and videos
- ✅ **Confidence Thresholding**: Adjustable confidence levels for detection sensitivity
- ✅ **Sample Image Support**: Automatic fallback to sample image for quick testing
- ✅ **Video Processing**: Frame-by-frame detection with annotated output

### Analytics & Visualization

- 📊 **Interactive Charts**: Plotly-powered visualizations
  - Confidence score distribution (histogram)
  - Confidence trends across detections (line chart)
  - Confidence range breakdown (bar chart)
  - Detection area distribution (histogram)
- 📈 **Statistical Metrics**:
  - Total detections count
  - Average, maximum, and minimum confidence scores
  - Bounding box area statistics
- 📥 **Data Export**: Download detection data as CSV
- 🎥 **Video Export**: Download annotated videos

### User Interface

- 🎨 **Clean Design**: Modern, intuitive interface with no sidebar clutter
- 📱 **Responsive Layout**: Works on desktop and tablet devices
- 🔗 **Kaggle Integration**: Direct links to all training notebooks
- 📚 **Comprehensive Documentation**: Built-in model descriptions and help text

---

## 🤖 Models

This repository includes 6 pre-trained models covering different learning paradigms:

### Supervised Learning Models

| Model | Description | Use Case |
|-------|-------------|----------|
| **YOLOv10n** | Fast and efficient baseline model | Quick detection with good accuracy |
| **YOLOv11n** | Improved architecture with better accuracy | Balanced speed and performance |
| **YOLOv12n** | Latest YOLO version with enhanced performance | Best accuracy for supervised approach |

### Semi-Supervised Learning

| Model | Description | Use Case |
|-------|-------------|----------|
| **Soft Teacher (Student)** | Uses pseudo-labeling techniques on unlabeled data | Leverages both labeled and unlabeled data |

### Self-Supervised Learning

| Model | Description | Use Case |
|-------|-------------|----------|
| **DINOv3+YOLOv12n** | DINO self-supervised pre-training + YOLO | Strong feature representations |
| **BYOL+YOLOv12n** | Bootstrap Your Own Latent + YOLO architecture | Robust learned features without labels |

All models are optimized for weed detection with `.pt` weight files included in the `weights/` directory.

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (for cloning the repository)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/weed-detection-system.git
cd weed-detection-system
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Using venv
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
# Check if all packages are installed
pip list
```

---

## 💻 Usage

### Running the Application

```bash
streamlit run app.py
```

The application will automatically open in your default browser at `http://localhost:8501`

### Using the Application

#### 1. **Detection Tab**

**Quick Test (No Upload):**
1. Select a model from the dropdown menu
2. Click **"🚀 Detect Weeds"** button
3. The app will use the sample image for detection

**Custom Image/Video:**
1. Select a model from the dropdown menu
2. Choose input type: **Image** or **Video**
3. Click **"Browse files"** to upload your media
4. Adjust **confidence threshold** (optional, default: 0.25)
5. Click **"🚀 Detect Weeds"**
6. View results with side-by-side comparison

#### 2. **Kaggle Notebooks Tab**

- Browse all training notebooks
- Click **"Open Notebook"** to view detailed implementations
- Explore model architectures, training procedures, and evaluation metrics

### Configuration

You can modify the confidence threshold (0.1 - 1.0) to adjust detection sensitivity:
- **Lower threshold (0.1-0.3)**: More detections, may include false positives
- **Medium threshold (0.3-0.6)**: Balanced detection
- **Higher threshold (0.6-1.0)**: Fewer but more confident detections

---

## 📁 Project Structure

```
weed-detection-system/
│
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── .gitignore                      # Git ignore rules
│
├── utils/                          # Utility modules
│   ├── __init__.py                # Package initialization
│   ├── config.py                  # Configuration and model settings
│   ├── detector.py                # YOLO detection logic
│   └── visualizer.py              # Visualization and statistics
│
├── weights/                        # Pre-trained model weights
│   ├── YOLOv10n_weed.pt
│   ├── YOLOv11n_weed.pt
│   ├── YOLOv12n_weed.pt
│   ├── Soft Teacher (Student)_weed.pt
│   ├── DINOv3+YOLOv12n_weed.pt
│   └── BYOL+YOLOv12n_weed.pt
│
├── notebooks/                      # Jupyter notebooks
│   ├── YOLOv10n_training.ipynb
│   ├── YOLOv11n_training.ipynb
│   ├── YOLOv12n_training.ipynb
│   ├── Soft_Teacher_training.ipynb
│   ├── DINOv3_YOLOv12n_training.ipynb
│   └── BYOL_YOLOv12n_training.ipynb
└── sample_image.png               # Sample image for testing
```

---

## 📓 Notebooks

All training notebooks are available both in this repository and on Kaggle:

### Supervised Learning

| Notebook | Repository | Kaggle Link |
|----------|-----------|-------------|
| YOLOv10n Training | [View](notebooks/YOLOv10n_training.ipynb) | [Open in Kaggle](https://www.kaggle.com/code/saifkhancse/weed-detection-using-supervised-learning-yolov10n) |
| YOLOv11n Training | [View](notebooks/YOLOv11n_training.ipynb) | [Open in Kaggle](https://www.kaggle.com/code/stone369/weed-detection-using-supervised-learning-yolov11n) |
| YOLOv12n Training | [View](notebooks/YOLOv12n_training.ipynb) | [Open in Kaggle](https://www.kaggle.com/code/saifkhancse/weed-detection-using-supervised-learning-yolov12n) |

### Semi-Supervised Learning

| Notebook | Repository | Kaggle Link |
|----------|-----------|-------------|
| Soft Teacher Training | [View](notebooks/Soft_Teacher_training.ipynb) | [Open in Kaggle](https://www.kaggle.com/code/saifkhancse/weed-detection-semi-sup-learning-soft-teacher) |

### Self-Supervised Learning

| Notebook | Repository | Kaggle Link |
|----------|-----------|-------------|
| DINOv3+YOLOv12n Training | [View](notebooks/DINOv3_YOLOv12n_training.ipynb) | [Open in Kaggle](https://www.kaggle.com/code/saifkhancse/weed-detection-using-ssl-dinov3-yolov12n) |
| BYOL+YOLOv12n Training | [View](notebooks/BYOL_YOLOv12n_training.ipynb) | [Open in Kaggle](https://www.kaggle.com/code/saifkhancse/weed-detection-using-ssl-byol-yolov12n) |

Each notebook contains:
- Data preprocessing steps
- Model architecture details
- Training configuration
- Evaluation metrics
- Visualization of results

---



## 🛠️ Technologies Used

### Core Technologies

- **[Python 3.8+](https://www.python.org/)**: Primary programming language
- **[Streamlit](https://streamlit.io/)**: Web application framework
- **[Ultralytics YOLO](https://github.com/ultralytics/ultralytics)**: Object detection framework
- **[OpenCV](https://opencv.org/)**: Computer vision library
- **[PyTorch](https://pytorch.org/)**: Deep learning framework (via Ultralytics)

### Data & Visualization

- **[Pandas](https://pandas.pydata.org/)**: Data manipulation and analysis
- **[NumPy](https://numpy.org/)**: Numerical computing
- **[Plotly](https://plotly.com/)**: Interactive visualizations
- **[Pillow](https://python-pillow.org/)**: Image processing

### Model Architectures

- **YOLOv10/v11/v12**: Latest YOLO object detection models
- **Soft Teacher**: Semi-supervised learning framework
- **DINOv3**: Self-supervised vision transformer
- **BYOL**: Bootstrap Your Own Latent self-supervised learning

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Contact

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

**Project Link**: [https://github.com/yourusername/weed-detection-system](https://github.com/yourusername/weed-detection-system)

---

## 🙏 Acknowledgments

- [Ultralytics](https://github.com/ultralytics/ultralytics) for the YOLO implementation
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Kaggle](https://www.kaggle.com/) for providing computational resources
- Agricultural research community for dataset contributions

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

Made with ❤️ by [Your Name](https://github.com/yourusername)

</div>
