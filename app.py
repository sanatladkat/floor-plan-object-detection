import streamlit as st
from ultralytics import YOLO
import PIL
import helper
import setting

def main():
    """
    Main function for the Streamlit app.
    """
    setting.configure_page()

    # Creating sidebar
    with st.sidebar:
        st.header("Image Configuration")     # Adding header to sidebar
        # Adding file uploader to sidebar for selecting images
        source_img = st.sidebar.file_uploader(
            "Choose an image...", type=("jpg", "jpeg", "png"))

        # Model Options
        confidence = setting.get_model_confidence()

        # Multiselect for selecting labels
        available_labels = ['Column', 'Curtain Wall', 'Dimension', 'Door', 'Railing', 'Sliding Door', 'Stair Case', 'Wall', 'Window']
        selected_labels = setting.select_labels(available_labels)

    # Creating main page heading
    st.title("Floor Plan Object Detection using YOLOv8")

    # Creating two columns on the main page
    col1, col2 = st.columns(2)

    # Adding image to the first column if image is uploaded
    with col1:
        if source_img:
            # Opening the uploaded image
            uploaded_image = PIL.Image.open(source_img)
            # Adding the uploaded image to the page with a caption
            st.image(source_img,caption="Uploaded Image",use_column_width=True)
        else:
            st.warning("Please upload an image.")

    model = YOLO('best.pt')

    if st.sidebar.button('Detect Objects'):
        if not source_img:
            st.warning("Please upload an image before detecting objects.")
        else:
            res = model.predict(uploaded_image, conf=confidence)
            filtered_boxes = [box for box in res[0].boxes if model.names[int(box.cls)] in selected_labels]
            res[0].boxes = filtered_boxes
            res_plotted = res[0].plot()[:, :, ::-1]
            with col2:
                st.image(res_plotted, caption='Detected Image',use_column_width=True)
                # Count detected objects and display counts
                object_counts = helper.count_detected_objects(model, filtered_boxes)
                st.write("\n\nDetected Objects and their Counts:")
                for label, count in object_counts.items():
                    st.write(f"{label}: {count}")

                # Generate and provide download link for CSV
                csv_file = helper.generate_csv(object_counts)
                st.download_button(
                    label="Download CSV",
                    data=csv_file,
                    file_name='detected_objects.csv',
                    mime='text/csv'
                )

if __name__ == "__main__":
    main()
