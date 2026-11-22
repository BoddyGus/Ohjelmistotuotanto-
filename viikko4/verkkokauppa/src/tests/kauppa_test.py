import unittest
from unittest.mock import Mock, call
from kauppa import Kauppa
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        self.viitegeneraattori_mock.uusi.return_value = 42

        self.tuotteet = {
            1: Tuote(1, "maito", 5),
            2: Tuote(2, "piimä", 7),
        }

        def varasto_saldo(tuote_id):
            if tuote_id in self.tuotteet:
                return 10
            return 0

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = (
            lambda tuote_id: self.tuotteet.get(tuote_id)
        )

        self.kauppa = Kauppa(
            self.varasto_mock,
            self.pankki_mock,
            self.viitegeneraattori_mock,
        )

    def osta_tuotteita(self, *tuote_idt):
        self.kauppa.aloita_asiointi()

        for tuote_id in tuote_idt:
            self.kauppa.lisaa_koriin(tuote_id)

        self.kauppa.tilimaksu("pekka", "12345")

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        self.osta_tuotteita(1)

        self.pankki_mock.tilisiirto.assert_called()

    def test_tilisiirto_kutsutaan_oikeilla_arvoilla_yhden_tuotteen_ostos(self):
        self.osta_tuotteita(1)

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            5,
        )

    def test_tilisiirto_kaksi_erilaista_tuotetta(self):
        self.osta_tuotteita(1, 2)

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            12,
        )

    def test_tilisiirto_kaksi_samaa_tuotetta(self):
        self.osta_tuotteita(1, 1)

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            10,
        )

    def test_tilisiirto_kun_toinen_tuote_on_loppu(self):
        self.varasto_mock.saldo.side_effect = (
            lambda tuote_id: 10 if tuote_id == 1 else 0
        )

        self.osta_tuotteita(1, 2)

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            5,
        )
    def test_aloita_asiointi_nollaa_edellisen_ostoksen(self):
        self.osta_tuotteita(1)
        self.osta_tuotteita(2)

        self.assertEqual(
            self.pankki_mock.tilisiirto.call_args_list[-1],
            call("pekka", 42, "12345", "33333-44455", 7),
        )

    def test_jokainen_tilimaksu_pyytää_uuden_viitenumeron(self):
        self.viitegeneraattori_mock.uusi.side_effect = [42, 43]

        self.osta_tuotteita(1)
        self.osta_tuotteita(2)

        self.assertEqual(
            self.pankki_mock.tilisiirto.call_args_list,
            [
                call("pekka", 42, "12345", "33333-44455", 5),
                call("pekka", 43, "12345", "33333-44455", 7),
            ],
        )

    def test_tuotteen_poisto_korista_palauttaa_sen_varastoon(self):
        tuote = self.tuotteet[1]

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)

        self.varasto_mock.palauta_varastoon.assert_called_once_with(tuote)
    def test_tuntematon_tuote_ei_lisaa_tuotetta_koriin(self):
        self.osta_tuotteita(999)

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            0,
        )

    def test_tuotteen_tulostus_hash_ja_vertailu(self):
        tuote = self.tuotteet[1]
        sama_tuote = Tuote(1, "eri nimi", 100)
        eri_tuote = self.tuotteet[2]

        self.assertEqual(str(tuote), "maito")
        self.assertEqual(hash(tuote), hash(sama_tuote))
        self.assertEqual(tuote, sama_tuote)
        self.assertNotEqual(tuote, eri_tuote)