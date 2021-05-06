import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5 import Qt
from PyQt5.QtCore import QSize
from unittest import TestCase
import main

app = QApplication(sys.argv)


class SoundTest(unittest.TestCase):
    """Tests the sound scanner"""
    def setUp(self):
        """Create The Gui"""
        self.form = main.MainWindow()
        self.form.log.setLevel("NOTSET")
        self.results = self.form.specs.sound.test()

    def test_sound_cards(self):
        """Tests that sound_cards is not None"""
        self.assertNotEqual(self.results.sound_cards, None, "sound_cards should not be None")

    def test_sound_card_present(self):
        """Tests that sound_card_present is not None"""
        self.assertNotEqual(self.results.sound_card_present, None, "sound_card_present should not be None")

    def test_default_sound_card(self):
        """Tests that default_sound_card is not None"""
        self.assertNotEqual(self.results.default_sound_card, None, "default_sound_card should not be None")

    def test_mics(self):
        """Tests that mics is not None"""
        self.assertNotEqual(self.results.mics, None, "mics should not be None")

    def test_mic_present(self):
        """Tests that mic_present is not None"""
        self.assertNotEqual(self.results.mic_present, None, "mic_present should not be None")

    def test_default_mic(self):
        """Tests that default_mic is not None"""
        self.assertNotEqual(self.results.default_mic, None, "default_mic should not be None")


if __name__ == "__main__":
    unittest.main()
