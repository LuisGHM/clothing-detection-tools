import logging
from ultralytics import YOLO

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def get_augmentation_settings():
    return {
        'flipud': 0.5,  # 50% chance of vertical flip
        'fliplr': 0.5,  # 50% chance of horizontal flip
        'hsv_h': 0.015,  # Hue adjustment
        'hsv_s': 0.7,  # Saturation adjustment
        'hsv_v': 0.4,  # Exposure adjustment
        'translate': 0.1,  # Random translation
        'scale': 0.5,  # Random scaling
        'shear': 0.0,  # No shear
        'perspective': 0.0,  # No perspective
        'erasing': 0.1,  # Increased random erasing
        'mosaic': 0.3,  # Always use mosaic augmentation
        'auto_augment': 'randaugment',  # Add auto-augment
        'mixup': 0.2,  # Add mixup augmentation
    }

def get_training_params():
    return {
        'epochs': 200,  # Reduced epochs for early stopping
        'batch': 32,  # Adjust batch size based on GPU memory
        'lr0': 0.002,  # Initial learning rate
        'weight_decay': 0.01,
        'dropout': 0.1,
        'augment': True,
        'patience': 15,  # Increase patience for early stopping
        'save_period': 10,
        'conf': 0.6,  # Confidence threshold
        'iou': 0.5,  # IOU threshold for NMS
        'cos_lr': True,  # Use cosine learning rate scheduler
        'freeze': [0, 1],  # Freeze initial layers
    }

def main():
    setup_logging()

    data_config_path = "data.yaml"

    # Load the model directly from the .pt file
    model = YOLO("yolo11n.pt")

    augmentation_settings = get_augmentation_settings()
    training_params = get_training_params()

    try:
        model.train(data=data_config_path, **training_params, **augmentation_settings)
        logging.info("Model training completed successfully.")
    except Exception as e:
        logging.error(f"Error during training: {e}")

if __name__ == '__main__':
    main()
