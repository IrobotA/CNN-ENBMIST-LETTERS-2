import numpy as np
import streamlit as st
from PIL import Image, ImageOps
import tensorflow as tf
import pandas as pd

model = tf.keras.models.load_model('cnn.h5')

def import_and_predict(image_data, model):
    
        size = (28,28)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = image.convert('RGB')
        image = np.asarray(image)
        image = (image.astype(np.float32) / 255.0)
        image2_reshape = image.reshape(-1,28,28,1)

        prediction = model.predict(image2_reshape)
        res=np.argmax(prediction,axis=1) 
        
        
        return res 
#mettre prediction a la place de res pour avoir les pourcentages

model = tf.keras.models.load_model('cnn.h5')

st.write("""
         # Letter prédiction
         """
         )

st.write("This is a simple image classification web app to predict letter")

file = st.file_uploader("Please upload an image file", type=["jpg", "png"])
#
if file is None:
    st.text("You haven't uploaded an image file(jpg or png)")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)
    
    if np.argmax(prediction) == 0:
        st.write("A")
    elif np.argmax(prediction) == 1:
        st.write("B")
    elif np.argmax(prediction) == 2:
        st.write("C")
    elif np.argmax(prediction) == 3:
        st.write("D")
    elif np.argmax(prediction) == 4:
        st.write("E")
    elif np.argmax(prediction) == 5:
        st.write("F")
    elif np.argmax(prediction) == 6:
        st.write("G")
    elif np.argmax(prediction) == 7:
        st.write("H")
    elif np.argmax(prediction) == 8:
        st.write("I")
    elif np.argmax(prediction) == 9:
        st.write("J")
    elif np.argmax(prediction) == 10:
        st.write("K")
    elif np.argmax(prediction) == 11:
        st.write("L")
    elif np.argmax(prediction) == 12:
        st.write("M")
    elif np.argmax(prediction) == 13:
        st.write("N")
    elif np.argmax(prediction) == 14:
        st.write("O")
    elif np.argmax(prediction) == 15:
        st.write("P")
    elif np.argmax(prediction) == 16:
        st.write("Q")
    elif np.argmax(prediction) == 17:
        st.write("R")
    elif np.argmax(prediction) == 18:
        st.write("S")
    elif np.argmax(prediction) == 19:
        st.write("T")
    elif np.argmax(prediction) == 20:
        st.write("U")
    elif np.argmax(prediction) == 21:
        st.write("V")
    elif np.argmax(prediction) == 22:
        st.write("W")
    elif np.argmax(prediction) == 23:
        st.write("X")
    elif np.argmax(prediction) == 24:
        st.write("Y")
    elif np.argmax(prediction) == 25:
        st.write("Z")
    else:
        st.write("")

    #st.write(prediction)
#décocher cette ligne pour voir les pourcentages