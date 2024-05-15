import PIL
import pandas as pd

def count_detected_objects(model, filtered_boxes):
    """
    Count detected objects and return a dictionary of counts.
    """
    object_counts = {}
    for box in filtered_boxes:
        # Extract class label of detected object
        label = model.names[int(box.cls)]
        # Update count in dictionary
        object_counts[label] = object_counts.get(label, 0) + 1
    return object_counts

def generate_csv(object_counts):
    """
    Generate CSV data from detected object counts.
    """
    csv_data = pd.DataFrame(list(object_counts.items()), columns=['Label', 'Count'])
    csv_file = csv_data.to_csv(index=False)
    return csv_file
