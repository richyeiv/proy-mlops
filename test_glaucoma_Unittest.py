#!/usr/bin/env python
# coding: utf-8

# # Framework de pruebas unitarias `Unittest`
# Las pruebas unitarias o unit testing son una forma de comprobar que un fragmento de código funciona correctamente. Varías de las clasificaciones vistas en este tutorial forman parte de la clasificación de pruebas unitarias. Un trabajo de programación de calidad usualmente requiere la mitad de tiempo para codificar y la mitad de tiempo para crear las pruebas unitarias necesarias para probar el correcto funcionamiento del codigo, para esto se sugiere utilizar un framework de pruebas como `Unittest`, `PyTest` o `Robot`.
# 
# Hay varias razones para utilizar un framework de pruebas:
# - Si tiene muchos casos de prueba, el framework de pruebas le evitará escribir mucho código.
# - El framework proporciona una forma uniforme de informar los resultados de las pruebas y gestionar las fallas de las pruebas.
# - Un framework de pruebas puede informarle sobre la cobertura de código para que sepa qué pruebas agregar.
# 
# Esta vez, usaremos el framework `Unittest`. Este es un paquete de Python separado. El uso de este framework requiere lo siguiente:
# 1. Importar el módulo unittest
# 2. Definir una clase que herede de `unittest.TestCase`
# 3. Escribir funciones que ejecuten el código que se probará y comprobar los resultados.
# 
# El último elemento tiene dos subpartes:
# - Primero, debemos identificar qué métodos de la clase que hereda de `unittest.TestCase` son pruebas. Usted indica que método debe ejecutarse como una prueba haciendo que el nombre del método comience con la palabra "test".
# 
# - Segundo, los "métodos de prueba" deben comunicar al framework los resultados obtenidos de la evaluación de la salida del código que se está probando. Esto se realiza usando sentencias `assert`. Por ejemplo, `self.assertEqual` toma dos argumentos. Si estos son objetos para los que `==` devuelve `True`, la prueba pasa. De lo contrario, la prueba falla.

# Primero creamos una Clase TestGlaucomaDeteccion que hereda de unittest.TestCase. 
# Hemos definido tres métodos de prueba
# 
# 1.- test_existencia_directorio
# 
# 2.- test_carga_imagen 
# 
# 3.- test_conteo_imagenes

# In[5]:


import unittest
import os
from skimage.io import imread
from skimage.transform import resize


# In[6]:


class TestGlaucomaDeteccion(unittest.TestCase):

    def setUp(self):
        self.image_dir = 'GlaucomaTest/Fundus_Train_Val_Data/Fundus_Scanes_Sorted'
        self.train_dir = os.path.join(self.image_dir, 'Train')
        self.validation_dir = os.path.join(self.image_dir, 'Validation')

        #Esta prueba verifica la existencia de los directorios. 
        #Comprueba si los directorios image_dir, train_dir y validation_dir existen utilizando la función os.path.exists(). Si alguno de los directorios no existe, la prueba fallará.
    def test_existencia_directorio(self):
        try:
            self.assertTrue(os.path.exists(self.image_dir))
            self.assertTrue(os.path.exists(self.train_dir))
            self.assertTrue(os.path.exists(self.validation_dir))
        except AssertionError:
            self.fail("La ruta del directorio no existe.")

        #Esta prueba verifica la carga de imágenes.
        #Si la imagen no se puede cargar correctamente o genera una excepción o fallara
    def test_carga_imagen(self):
        train_image_negative = os.listdir(os.path.join(self.train_dir, 'Glaucoma_Negative'))
        train_image_positive = os.listdir(os.path.join(self.train_dir, 'Glaucoma_Positive'))

        for image in train_image_negative:
            try:
                image_path = os.path.join(self.train_dir, 'Glaucoma_Negative', image)
                loaded_image = imread(image_path)
                self.assertIsNotNone(loaded_image)
            except Exception as e:
                self.fail(f"Error al cargar la imagen: {image_path}. {e}")

        for image in train_image_positive:
            try:
                image_path = os.path.join(self.train_dir, 'Glaucoma_Positive', image)
                loaded_image = imread(image_path)
                self.assertIsNotNone(loaded_image)
            except Exception as e:
                self.fail(f"Error al cargar la imagen: {image_path}. {e}")

                #Esta prueba verifica el conteo total de las imágenes en los directorios Glaucoma_Negative y Glaucoma_Positive 
                #dentro de train_dir.
    def test_conteo_imagenes(self):
        train_image_negative = os.listdir(os.path.join(self.train_dir, 'Glaucoma_Negative'))
        train_image_positive = os.listdir(os.path.join(self.train_dir, 'Glaucoma_Positive'))
        total_imagenes = len(train_image_negative) + len(train_image_positive)

        try:
            self.assertEqual(total_imagenes, 48)  # Utilizamos 48 imágenes para las pruebas unitarias
        except AssertionError:
            self.fail("El recuento total de imágenes es incorrecto.")



# In[ ]:


if __name__ == '__main__':
    unittest.main()

