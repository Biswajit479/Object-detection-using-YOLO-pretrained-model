import streamlit as st
from object_detect import detection


# Title of the project
st.title("Object Detection Using YOLO Pretrained Model")


file = st.file_uploader("Uplode the image where you detect object:", type = ['jpg', 'jpeg', 'png', 'webpf','bmp', 'tiff', 'svg'])
press = st.button("Detect Object")
# create the object of the detection class that import from object_detect file
if file:
    if press:
        obj = detection()
        result_image = obj.obj_detect(file)

        st.image(result_image)