import unittest
import models

class TestModels(unittest.TestCase):
     def test_models(self):
          self.assertEqual(models.svc(1,1,1.01,3,0,-1,0,0,0,133,47.1,135.5,2.65,6.31,14.55,43.25,4.755,8550,0,0,0,0,0,0,139.8635,1,1,11
), 1)     
          self.assertEqual(models.rf(1,1,1.01,3,0,-1,0,0,0,133,47.1,135.5,2.65,6.31,14.55,43.25,4.755,8550,0,0,0,0,0,0,139.8635,1,1,11
), 1)
          self.assertEqual(models.dt(1,1,1.01,3,0,-1,0,0,0,133,47.1,135.5,2.65,6.31,14.55,43.25,4.755,8550,0,0,0,0,0,0,139.8635,1,1,11
), 1)
          
if __name__ == '__main__':
    unittest.main()