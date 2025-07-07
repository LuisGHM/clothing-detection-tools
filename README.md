# YOLO Dataset Tools for Fashion Detection

A collection of useful tools for preparing fashion datasets, developed by **Styles.AI** during our computer vision research phase.

## 🎯 About

These tools were originally developed for fashion item detection using YOLO models. While we've since evolved our approach to classification + generative AI for outfit creation, we're open-sourcing these tools to help the computer vision community.

## ✨ Features

### 🏷️ Semi-Automatic Labeling
- **`autoAnnotation/semi_auto_labeler_yolo.py`** - Interactive tool that uses a pre-trained YOLO model to suggest annotations
- Shows predicted bounding boxes with confidence scores
- Manual review workflow: Save (S), Delete (D), or Skip (Q)
- Automatically generates YOLO format labels

### 🧹 Data Cleaning
- **`cleaning/remove_duplicates.py`** - Removes duplicate images using SHA-256 hash comparison
- Resizes images to fixed dimensions for consistent hashing
- Safely deletes duplicates while preserving originals

### 🔄 Format Conversion
- **`conversion_tools/convert_webp_to_jpg.py`** - Batch converts WebP images to JPG format
- Automatically deletes original WebP files after conversion
- Handles RGB conversion for compatibility

### 📊 Dataset Management
- **`data_split/split_yolo_by_class_id.py`** - Intelligently splits dataset maintaining class distribution
- 80/20 train/validation split by class
- Moves both images and corresponding label files
- Provides detailed statistics per class

### 🔗 Data Synchronization
- **`labelsimgs/sync_labels_and_images.py`** - Ensures consistency between images and labels
- Removes orphaned label files
- Reports missing correspondences

### 🚀 Training Pipeline
- **`train_yolo_detector.py`** - Complete YOLO training setup with optimized parameters
- Advanced augmentation settings
- Early stopping and learning rate scheduling

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/yolo-dataset-tools.git
cd yolo-dataset-tools

# Install dependencies
pip install -r requirements.txt
```

### Requirements
```txt
ultralytics>=8.0.0
opencv-python>=4.5.0
Pillow>=8.0.0
PyYAML>=5.4.0
```

## 📖 Usage

### Semi-Automatic Labeling
```python
# Update paths in the script
python autoAnnotation/semi_auto_labeler_yolo.py
```
**Controls:**
- `S` - Save image and generated labels
- `D` - Delete current image
- `Q` - Quit the tool

### Remove Duplicates
```python
# Update folder_path in the script
python cleaning/remove_duplicates.py
```

### Convert WebP to JPG
```python
# Update input_dir and output_dir in the script
python conversion_tools/convert_webp_to_jpg.py
```

### Split Dataset by Class
```python
# Update folder paths in the script
python data_split/split_yolo_by_class_id.py
```

### Sync Images and Labels
```python
# Update directory paths in the script
python labelsimgs/sync_labels_and_images.py
```

### Train YOLO Model
```python
# Ensure data.yaml is configured
python train_yolo_detector.py
```

## 📁 Project Structure

```
yolo-dataset-tools/
├── autoAnnotation/
│   └── semi_auto_labeler_yolo.py
├── cleaning/
│   └── remove_duplicates.py
├── conversion_tools/
│   └── convert_webp_to_jpg.py
├── data_split/
│   └── split_yolo_by_class_id.py
├── labelsimgs/
│   └── sync_labels_and_images.py
├── train_yolo_detector.py
├── data.yaml (example configuration)
└── README.md
```

## ⚙️ Configuration

Most scripts require updating file paths. Look for these sections in each script:

```python
# Update these paths according to your setup
input_folder = "path/to/your/images"
output_folder = "path/to/your/output"
model_path = "path/to/your/model.pt"
```

## 🎨 Fashion Classes

The example `data.yaml` includes 86 fashion categories covering:
- **Tops**: T-shirts, shirts, sweaters, hoodies, etc.
- **Bottoms**: Jeans, trousers, skirts, shorts, etc.
- **Footwear**: Sneakers, boots, heels, sandals, etc.
- **Accessories**: Bags, hats, etc.

## 🤝 Contributing

We welcome contributions! Please feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 🙏 Acknowledgments

- Developed by the **Styles.AI** team
- Built with [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- Part of our journey in fashion AI research

## 📞 Contact

- **Styles.AI** - [Website](https://www.stylestia.com.br/)
- Questions? Open an issue or reach out to our team

---

*These tools represent an important step in our AI journey. While we've moved to more advanced classification and generative approaches for outfit creation, we hope these tools help other teams working on fashion computer vision projects.*
