import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.ostokset(), [])

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_hinta_oikein(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_erilaisen_tuotteen_lisaamisen_jalkeen_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        juusto = Tuote("Juusto", 5)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_erilaisen_tuotteen_hinta_oikein(self):
        maito = Tuote("Maito", 3)
        juusto = Tuote("Juusto", 5)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)

        self.assertEqual(self.kori.hinta(), 8)

    def test_saman_tuotteen_lisaaminen_kahdesti_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_saman_tuotteen_lisaaminen_kahdesti_hinta_oikein(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_yksi_ostos(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_ostos_kuvaa_lisattya_tuotetta_oikein(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_erilaisen_tuotteen_lisaaminen_luo_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        juusto = Tuote("Juusto", 5)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)

        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_saman_tuotteen_lisaaminen_kahdesti_luo_yhden_ostoksen(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    def test_saman_tuotteen_ostos_tietaa_lukumaaran(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 2)

    def test_saman_tuotteen_yhden_poiston_jalkeen_lukumaara_1(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.lukumaara(), 1)

    def test_viimeisen_tuotteen_poisto_tyhjentaa_korin(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.ostokset(), [])

    def test_tyhjennys_tyhjentaa_korin(self):
        maito = Tuote("Maito", 3)
        juusto = Tuote("Juusto", 5)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)
        self.kori.tyhjenna()

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.ostokset(), [])