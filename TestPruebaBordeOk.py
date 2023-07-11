#!/usr/bin/env python
# coding: utf-8

# In[4]:


import unittest
import os
from skimage.io import imread
from skimage.transform import resize


# In[5]:


class TestPruebaBorde(unittest.TestCase):

    def setUp(self):
        self.validation_dir = 'GlaucomaTest/Fundus_Train_Val_Data/Fundus_Scanes_Sorted/Validation'

    def test_conteo_imagenes(self):
        try:
            test_image_negative = os.listdir(os.path.join(self.validation_dir, 'Glaucoma_Negative'))
            test_image_positive = os.listdir(os.path.join(self.validation_dir, 'Glaucoma_Positive'))
            total_imagenes = len(test_image_negative) + len(test_image_positive)

            # Verificar que el recuento total de imágenes es mayor que cero
            self.assertGreater(total_imagenes, 0)

            # Verificar que el recuento total de imágenes es menor o igual a un valor específico
            self.assertLessEqual(total_imagenes, 100)
        except Exception as e:
            self.fail(f"Error al obtener el conteo de imágenes: {e}")


# In[6]:



if __name__ == '__main__':
    unittest.main()


# In[ ]:




