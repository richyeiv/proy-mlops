#!/usr/bin/env python
# coding: utf-8

# In[7]:


import unittest
import math


# In[8]:


class TestPruebaGolpeDeteccionGlaucoma(unittest.TestCase):

    def test_prueba_un_golpe(self):
        # Definir los elementos y sus probabilidades
        elementos = {
            'Glaucoma_Negativo': 0.5,
            'Glaucoma_Positivo': 0.5
        }

        # Calcular la cantidad de bits necesarios
        cantidad_bits = -sum(p * math.log2(p) for p in elementos.values())

        # Verificar que la cantidad de bits sea igual a 1
        self.assertEqual(cantidad_bits, 1)


# In[9]:


if __name__ == '__main__':
    unittest.main()


# In[ ]:




