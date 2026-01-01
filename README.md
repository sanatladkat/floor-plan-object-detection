# Architectural Floor Plan Object Detection

[![DOI](https://zenodo.org/badge/774683487.svg)](https://doi.org/10.5281/zenodo.18112721)  
**DOI**: [10.5281/zenodo.18112721](https://doi.org/10.5281/zenodo.18112721)

## Overview

This project aims to develop an object detection system for architectural floor plans using the YOLOv8 model. The system was trained to detect various elements commonly found in floor plans, such as columns, walls, doors, windows, etc. Given an input image of a floor plan, the system will accurately identify and label these elements.

![Streamlit App Demo](WebUI.gif)

## Dataset

The dataset consisted of labeled images of architectural floor plans, categorized into classes such as 'Column', 'Wall', 'Door', etc. Each image is accompanied by its corresponding label file specifying the location and class of each object within the image.  
[Floor Plan Dataset on Roboflow](https://universe.roboflow.com/walldetect-f9eio/floor_plan_multiple)

## Technology Stack

- **YOLOv8**: Object detection model architecture
- **PyTorch**: Deep learning framework for model training and inference
- **YAML**: Configuration file format for dataset organization
- **torchvision**: Library for image transformations and dataset handling
- **Streamlit**: Web UI

## Use Cases

- **Architectural Design**: Architects and designers can use the system to automatically analyze floor plans and extract key elements for design optimization.
- **Construction Planning**: Construction companies can utilize the system for automated analysis of floor plans to streamline construction planning and resource allocation.
- **Real Estate**: Real estate agencies can leverage the system to quickly evaluate and classify properties based on floor plan features, aiding in property management and sales.

## Benefits

- **Efficiency**: Automated object detection reduces manual effort and time required for analyzing floor plans.
- **Accuracy**: The YOLOv8 model provides high accuracy in detecting and classifying architectural elements.
- **Scalability**: The system can be easily scaled to handle large datasets and real-time processing of floor plan images.

## Scope

### Development Phases:

1. **Data Preparation**: Collect and preprocess the dataset, including image resizing, labeling, and organization according to the YAML file structure.
2. **Model Training**: Train the YOLOv8 model using the prepared dataset to learn to detect architectural elements in floor plans.
3. **Evaluation and Optimization**: Evaluate the trained model's performance using validation data and fine-tune hyperparameters for optimal results.
4. **Integration**: Integrate the trained model into an application or service for real-world usage, providing an intuitive interface for users to upload floor plan images and receive object detection results.
5. **Deployment**: Deploy the application to a production environment, ensuring scalability, reliability, and performance.

## Web UI

![Streamlit App Demo](WebUI.gif)

This Streamlit web application allows users to upload images containing floor plans and perform object detection using the YOLOv8 model. Detected objects are displayed on the uploaded image along with their counts. Users can adjust the confidence threshold for object detection and export the detected objects and their counts to a CSV file.

## Getting Started

To run this application locally, follow these steps:

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/architectural-floor-plan-object-detection.git
    ```

2. Navigate to the project directory.
   ```bash
   cd architectural-floor-plan-object-detection
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```
5. Access the application in your web browser (usually at `http://localhost:8501`).

## Usage

1. Upload an image containing a floor plan.
2. Adjust the confidence threshold using the slider in the sidebar.
3. Click the "Detect Objects" button to perform object detection.
4. Detected objects will be displayed on the uploaded image along with their counts.
5. Click the "Export to CSV" button to export the detected objects and their counts to a CSV file.

## Configuration

This project uses a `config.yaml` file for configuring model parameters such as:

* **confidence_threshold**: The minimum confidence score for detecting objects (default: `0.5`).
* **model_weights**: Path to the pre-trained model (default: `best.pt`).

Example of `config.yaml`:

```yaml
confidence_threshold: 0.5
model_weights: best.pt
```

## FAQ

**Q1: How can I improve the model's accuracy?**
A1: You can try training with more data or adjusting the hyperparameters in the config file.

**Q2: Can I use a custom floor plan dataset for training?**
A2: Yes! You can upload your dataset to Roboflow and follow the instructions on how to format it for YOLOv8.

**Q3: How do I change the confidence threshold?**
A3: You can adjust the confidence threshold in the sidebar of the Streamlit app or modify it in the `config.yaml` file.

## Contributing

We welcome contributions! If you'd like to contribute to this project:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request for review

Please follow the code style outlined in `.editorconfig` and ensure all tests pass before submitting your pull request.

## Running Tests

To run tests on your local machine:

1. Install the test dependencies:

   ```bash
   pip install -r requirements-test.txt
   ```
2. Run the tests using `pytest`:

   ```bash
   pytest tests/
   ```

## Acknowledgements

* **YOLOv8**: [Ultralytics YOLO](https://github.com/ultralytics/yolov5)
* **Streamlit**: [Streamlit Documentation](https://docs.streamlit.io/)
* **Pillow**: [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
* **Dataset**: [Roboflow - Floor Plan Dataset](https://universe.roboflow.com/walldetect-f9eio/floor_plan_multiple)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use this project, please cite it as:

**MLA Style**:  
Ladkat, Sanat N. *Architectural Floor Plan Object Detection*. 2024, [https://doi.org/10.5281/zenodo.18112721](https://doi.org/10.5281/zenodo.18112721).

**APA Style**:  
Ladkat, S. N. (2024). *Architectural Floor Plan Object Detection*. Zenodo. [https://doi.org/10.5281/zenodo.18112721](https://doi.org/10.5281/zenodo.18112721).

**BibTeX**:
```bibtex
@misc{ladkat2024architectural,
  author = {Sanat N. Ladkat},
  title = {Architectural Floor Plan Object Detection},
  year = {2024},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.18112721},
  url = {https://doi.org/10.5281/zenodo.18112721}
}
```