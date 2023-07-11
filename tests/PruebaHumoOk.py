#!/usr/bin/env python
# coding: utf-8

# In[16]:


import unittest
import os
from skimage.io import imread
from skimage.transform import resize


# In[17]:


class TestLoadImage(unittest.TestCase):

    def setUp(self):
        self.train_dir = 'GlaucomaTest/Fundus_Train_Val_Data/Fundus_Scanes_Sorted/Train'
        self.mapping = {
            0: 'Glaucoma_Negative',
            1: 'Glaucoma_Positive'
        }

    def test_smoke_test_load_image(self):
        row = {'Glaucoma': 0, 'Filename': '001.jpg'}

        folder_name = self.mapping[row['Glaucoma']]
        folder_path = os.path.join(self.train_dir, folder_name)
        image_path = os.path.join(folder_path, row['Filename'])

        try:
            im = imread(image_path)
            im = resize(im, (224, 224))  # Tamaño de imagen de ejemplo

            # Verificar si la imagen se ha cargado correctamente
            self.assertIsNotNone(im)
        except FileNotFoundError as e:
            self.fail(f"Archivo no encontrado: {image_path}")


# In[18]:


if __name__ == '__main__':
    unittest.main()


# In[ ]:




