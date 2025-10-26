import unittest
# src/test/testBiblio.py
from service.test_auth_service import login_socio
# ... (rest of the test remains the same)
class testSocio(unittest.TestCase):

    def test_login_socio(self):
        # Datos de prueba
        #Prueba para un login exitoso
        self.assertTrue(login_socio("gustavo@example.com", "correctpassword"))
        
        # Prueba para un login fallido
        #self.assertTrue(login_socio("gustavo@example.com", "password"))

if __name__ == '__main__':
    unittest.main()