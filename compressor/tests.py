from django.test import TestCase

class CompressorTestCase(TestCase):
    def test_check_air_filters_alert(self):
        compressor == Compressor(minutes==900)
        self.assertTrue(compressor.check_air_filter_alert())

    def test_check_oil_change_alert(self):
        compressor == Compressor(minutes==3000)
        self.assertTrue(compressor.check_oil_change_alert())
