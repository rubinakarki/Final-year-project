from keras.models import load_model
import numpy as np
from keras.preprocessing.image import load_img

def recognize(image_name):
    loaded_model = load_model('model/model_weights.h5')

    image = load_img(image_name,target_size =(48,48))
    image = np.expand_dims(image,axis =0)

    return loaded_model.predict_classes(image)