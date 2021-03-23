import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)
        
    def test_onko_rahamaara_oikein_alussa(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")

    def test_onko_edullisten_maara_nolla(self):
        self.assertEqual(str(self.kassapaate.edulliset), "0")
    
    def test_onko_maukkaitten_maara_nolla(self):
        self.assertEqual(str(self.kassapaate.maukkaat), "0")
    
    def test_syo_edullinen_kateisella_annettu_raha_oikea(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100240")
    
    def test_syo_edullinen_kateisella_annettu_raha_liian_vahan(self):
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(230)), "230")
    
    def test_syo_edullinen_kateisella_vaihtoraha_oikein(self):
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(500)), "260")
    
    def test_syo_edullinen_kateisella_myydyt_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(str(self.kassapaate.edulliset), "1")
    
    def test_syo_maukkaat_kateisella_annettu_raha_oikea(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100400")
    
    def test_syo_maukkaat_kateisella_annettu_raha_liian_vahan(self):
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(300)), "300")
    
    def test_syo_maukkaat_kateisella_vaihtoraha_oikein(self):
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(500)), "100")
    
    def test_syo_maukkaat_kateisella_myydyt_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(str(self.kassapaate.maukkaat), "1")
    
    def test_syo_edullinen_kortilla_myydyt_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.edulliset), "1")

    def test_syo_maukkaat_kortilla_myydyt_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.maukkaat), "1")
    
    def test_syo_edullinen_kortilla_rahaa_ei_kassaan(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
    
    def test_syo_maukkaat_kortilla_rahaa_ei_kassaan(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
    
    def test_syo_edullinen_kortilla_rahaa_palauta_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_syo_maukkaat_kortilla_ei_rahaa_palauta_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_syo_edullinen_kortilla_ei_rahaa_palauta_false(self):
        maksukortti2 = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti2), False)
    
    def test_syo_maukkaat_kortilla_ei_rahaa_palauta_false(self):
        maksukortti2 = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti2), False)
    
    def test_lataa_kortille_rahaa_kassan_rahat_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100200")
    
    def test_lataa_kortille_negatiivinen_summa(self):
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200), None)
    
