import numpy as np
from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render
from keras.applications import vgg16
from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing.image import img_to_array, load_img
from tensorflow.python.keras.backend import set_session

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
import django
django.setup()


from core.models import Image


def index(request):
    if request.method == "POST":
        image_db = Image()
        file = request.FILES["imageFile"]
        file_name = default_storage.save(file.name, file)
        file_url = default_storage.path(file_name)
        image_db.path = file_url

        #
        # https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/load_img
        #
        image = load_img(file_url, target_size=(224, 224))
        numpy_array = img_to_array(image)
        image_batch = np.expand_dims(numpy_array, axis=0)
        processed_image = vgg16.preprocess_input(image_batch.copy())

        with settings.GRAPH1.as_default():
            set_session(settings.SESS)
            predictions = settings.IMAGE_MODEL.predict(processed_image)

        label = decode_predictions(predictions, top=5)
        image_db.predictions = label
        image_db.save()
        context = {"image_path": file_url, "predictions": label}
        return render(request, "index.html", context)

    else:
        return render(request, "index.html")
