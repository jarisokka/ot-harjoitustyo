import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_onko_alkusaldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 1.1")
    
    def test_saldo_vahenee_oikein_kun_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")
    
    def test_saldo_ei_muutu_jos_rahaa_ei_riittavasti(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_ota_rahaa_palauttaa_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)
    
    def test_ota_rahaa_palauttaa_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(15), False)