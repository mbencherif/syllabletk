# -*- coding: utf-8 -*-

import unittest
import _syllabletk


class TestSyllabifier(unittest.TestCase):
    def test_one_syllable(self):
        self.assertEqual(_syllabletk.Syllabifier(
                         u'hwelp', son_peak=True).as_tuples(),
                         [(u'hw', u'e', u'lp')])

    def test_more_complex_syllabification(self):
        self.assertEqual(_syllabletk.Syllabifier(
                         u'atrɐms', son_peak=True).as_tuples(),
                         [(u'', u'a', u''), (u'tr', u'ɐ', u'ms')])

    def test_pterodactyl_syllabification(self):
        self.assertEqual(_syllabletk.Syllabifier(
                         u'ptɛrodaktyl', son_peak=True).as_tuples(),
                         [(u'pt', u'ɛ', u''), (u'r', u'o', u''),
                          (u'd', u'a', u'k'), (u't', u'y', u'l')])

    def test_german_fricative_syllabification(self):
        self.assertEqual(_syllabletk.Syllabifier(
                         u'ʃveʁɪxkajt', son_peak=True).as_tuples(),
                         [(u'ʃv', u'e', u''), (u'ʁ', u'ɪ', u'x'),
                          (u'k', u'aj', u't')])

    def test_english_phonetic_syllabification(self):
        self.assertEqual(_syllabletk.Syllabifier(
                         u'painsalow', son_peak=True).as_tuples(),
                         [(u'p', u'ai', u'n'), (u's', u'a', u''),
                          (u'l', u'ow', u'')])

    def test_diphthong_syllabification(self):
        self.assertEqual(_syllabletk.Syllabifier(
                         u'ʃɑɪnʃajn', son_peak=True).as_tuples(),
                         [(u'ʃ', u'ɑɪ', u'n'), (u'ʃ', u'aj', u'n')])


# Deprecated due to deprecation of _syllabletk.SyllableAnalyzerDepr.

class TestSyllableTK(unittest.TestCase):
    def setUp(self):
        self.sa = _syllabletk.SyllableAnalyzerDepr()

    def test_the_onsets(self):
        ws = [u'trup', u'pɹum', u'ap', u'strupon']
        results = [u'tr', u'pɹ', u'', u'str', u'p']
        self.assertEqual(self.sa.the_onsets(ws), results)

    def test_the_codas(self):
        ws = [u'hwelp', u'pewl', u'pa', u'plawd', u'taptap']
        results = [u'lp', u'l', u'', u'd', u'p', u'p']
        self.assertEqual(self.sa.the_codas(ws), results)

    def test_the_obstruent_sonorant_onsets(self):
        ws = [u'smaks', u'tliŋ', u'stap']
        results = [1.0, 1.0, 0.0]
        self.assertEqual(self.sa.the_obstruent_sonorant_onsets(ws),
                         results)

    def test_the_plosive_sonorant_onsets(self):
        ws = [u'pwak', u'snasplam', u'kap']
        results = [1.0, 0.0, 1.0, 0.0]
        self.assertEqual(self.sa.the_plosive_sonorant_onsets(ws),
                         results)

    def test_the_obstruent_approximant_onsets(self):
        ws = [u'tsup', u'pɹum', u'klap']
        results = [0.0, 1.0, 1.0]
        self.assertEqual(self.sa.the_obstruent_approximant_onsets(ws),
                         results)

    def test_the_plosive_approximant_onsets(self):
        ws = [u'tlup', u'pɹum', u'kwap', u'mleɡ']
        results = [1.0, 1.0, 1.0, 0.0]
        self.assertEqual(self.sa.the_plosive_approximant_onsets(ws),
                         results)

    def test_the_obstruent_obstruent_onsets(self):
        ws = [u'skup', u'ptum', u'kwap', u'mleɡ']
        results = [1.0, 1.0, 0.0, 0.0]
        self.assertEqual(self.sa.the_obstruent_obstruent_onsets(ws),
                         results)

    def test_the_plosive_plosive_onsets(self):
        ws = [u'ptuk', u'pɹum', u'kwap', u'ɡbo']
        results = [1.0, 0.0, 0.0, 1.0]
        self.assertEqual(self.sa.the_plosive_plosive_onsets(ws),
                         results)

    def test_the_sonorant_sonorant_onsets(self):
        ws = [u'mloŋ', u'mnemonik']
        results = [1.0, 1.0, 0.0, 0.0]
        self.assertEqual(self.sa.the_sonorant_sonorant_onsets(ws),
                         results)

    def test_the_nasal_nasal_onsets(self):
        ws = [u'mloŋ', u'mnemonik']
        results = [0.0, 1.0, 0.0, 0.0]
        self.assertEqual(self.sa.the_nasal_nasal_onsets(ws),
                         results)

    def test_the_complex_onsets(self):
        ws = [u'trup', u'pɹum', u'ap', u'strupon']
        results = [1.0, 1.0, 0.0, 1.0, 0.0]
        self.assertEqual(self.sa.the_complex_onsets(ws), results)

    def test_the_complex_onsets_2(self):
        ws = [u'trup', u'pɹum', u'ap', u'strupon']
        results = [1.0, 1.0, 0.0, 0.0, 0.0]
        self.assertEqual(self.sa.the_complex_onsets_2(ws), results)

    def test_the_complex_onsets_3(self):
        ws = [u'trup', u'spɹum', u'ap', u'strupon']
        results = [0.0, 1.0, 0.0, 1.0, 0.0]
        self.assertEqual(self.sa.the_complex_onsets_3(ws), results)

    def test_the_complex_onsets_4_or_more(self):
        ws = [u'trup', u'pɹum', u'ntsjap', u'pzlwustplon']
        results = [0.0, 0.0, 1.0, 1.0, 0.0]
        self.assertEqual(self.sa.the_complex_onsets_4_or_more(ws), results)

    def test_the_simple_codas(self):
        ws = [u'ka', u'rysp', u'ʃpil']
        results = [0.0, 0.0, 1.0]
        self.assertEqual(self.sa.the_simple_codas(ws), results)

    def test_the_complex_codas(self):
        ws = [u'ka', u'rysp', u'ʃpil']
        results = [0.0, 1.0, 0.0]
        self.assertEqual(self.sa.the_complex_codas(ws), results)

    def test_the_approximant_obstruent_codas(self):
        ws = [u'hwelp', u'pewl', 'paw', 'plawd']
        results = [1.0, 0.0, 0.0, 0.0]
        self.assertEqual(self.sa.the_approximant_obstruent_codas(ws),
                         results)

if __name__ == '__main__':
    unittest.main()
