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


class TestSyllableTK(unittest.TestCase):
    def setUp(self):
        self.sa = _syllabletk.SyllableAnalyzer()

    def test_the_onsets(self):
        ws = [u'trup', u'pum', u'ap']
        results = [u'tr', u'p', u'']
        self.assertEqual(self.sa.the_onsets(ws), results)

    def test_the_complex_onsets(self):
        ws = [u'strup', u'pum', u'ap']
        results = [1.0, 0.0, 0.0]
        self.assertEqual(self.sa.the_complex_onsets(ws), results)

    def test_the_obstruent_approximant_onsets(self):
        ws = [u'strup', u'pjum', u'kap']
        results = [0.0, 1.0, 0.0]
        self.assertEqual(self.sa.the_obstruent_approximant_onsets(ws),
                         results)

    def test_the_codas(self):
        ws = [u'hwelp', u'pewl', 'paw', 'plawd']
        results = [u'lp', u'wl', u'w', u'wd']
        self.assertEqual(self.sa.the_codas(ws), results)

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
        results = [1.0, 1.0, 0.0, 1.0]
        self.assertEqual(self.sa.the_approximant_obstruent_codas(ws),
                         results)

if __name__ == '__main__':
    unittest.main()
