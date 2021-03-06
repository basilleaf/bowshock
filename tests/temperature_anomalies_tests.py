import unittest
import sys
from time import sleep

from bowshock import temperature_anomalies


class temperatureAnomalies_UnitTests(unittest.TestCase):

    # ENDPOINTS NOT WORKING
    #def test_ta_adress_endpoint_noend(self):
    #    
    #    r = adress(adress='1800 F Street, NW, Washington DC', begin="1990")
    #    self.assertEqual(r.status_code, 200)
    #    sleep(2)

    #def test_ta_adress_endpoint_full(self):
    #    
    #    r = adress(adress='1800 F Street, NW, Washington DC', begin="1990", end="2000")
    #    self.assertEqual(r.status_code, 200)
    #    sleep(2)

    def test_ta_coordinate_endpoint_noend(self):

        r = temperature_anomalies.coordinate(lon=100.3, lat=1.6, begin="1990")
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_ta_coordinate_endpoint_full(self):

        r = temperature_anomalies.coordinate(lon=100.3, lat=1.6, begin="1990", end="2005")
        self.assertEqual(r.status_code, 200)
        sleep(2)


if __name__ == "__main__":
    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(temperatureAnomalies_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
