import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5 import Qt
from PyQt5.QtCore import QSize
from unittest import TestCase
import main

app = QApplication(sys.argv)


class SpecCheckTest(unittest.TestCase):
    """Test The SpecChecker GUI"""
    def setUp(self):
        """Create The Gui"""
        self.form = main.MainWindow()
        self.form.log.setLevel("NOTSET")

    def test_lblName_text(self):
        """Tests that lblName text is correct"""
        self.assertEqual(self.form.lblName.text(), "Name", 'lblName text incorrect')

    def test_txtName_text(self):
        """Tests that txtName text is correct"""
        self.assertEqual(self.form.txtName.text(), "", 'txtName text incorrect')

    def test_txtName_placeholder_text(self):
        """Tests that txtName placeholder text is correct"""
        self.assertEqual(self.form.txtName.placeholderText(), "Enter Your Full Name", 'txtName placeholder text incorrect')

    def test_lblEmail_text(self):
        """Tests that lblEmail text is correct"""
        self.assertEqual(self.form.lblEmail.text(), "Email", 'lblEmail text incorrect')

    def test_txtEmail_text(self):
        """Tests that txtEmail text is correct"""
        self.assertEqual(self.form.txtEmail.text(), "", 'txtEmail text incorrect')

    def test_txtEmail_placeholder_text(self):
        """Tests that txtEmail placeholder text is correct"""
        self.assertEqual(self.form.txtEmail.placeholderText(), "Double Check For Accuracy", 'txtEmail placeholder text incorrect')

    def test_txtStatus_text_defaults(self):
        """Test the txtStatus initial text is blank"""
        self.assertEqual(self.form.txtStatus.toPlainText(), "", "txtStatus default text not empty")

    def test_txtStatus_placeholder_text_defaults(self):
        """Test the txtStatus initial placeholder text is blank"""
        self.assertEqual(self.form.txtStatus.placeholderText(), "Press start to begin...", "txtStatus placeholder text incorrect")

    def test_start_button_defaults(self):
        """Test the GUI Start Button Default Values"""
        self.assertEqual(self.form.btnStart.text(), "Start", "btnStart text incorrect")

    def test_exit_button_defaults(self):
        """Test the GUI Exit Button Default Values"""
        self.assertEqual(self.form.btnExit.text(), "Exit", "btnExit text incorrect")

    def test_progress_bar_defaults(self):
        """Test the GUI Progress Bar Default Values"""
        self.assertEqual(self.form.progressBar.value(), 0, "progressbar value not defaulting to zero")

    def test_title_bar(self):
        """Tests Main Title Bar Default Value"""
        self.assertEqual(self.form.windowTitle(), "PC Specification Checker", "Window title is incorrect")

    def test_file_menu_text(self):
        """Tests the text of the File menu"""
        self.assertEqual(self.form.menu_File.title(), "&File", "Menu item File text incorrect")

    def test_about_menu_text(self):
        """Tests the text of the About menu"""
        self.assertEqual(self.form.actionAbout.text(), "A&bout", "Menu item About text incorrect")

    def test_exit_menu_text(self):
        """Tests the text of the Exit menu"""
        self.assertEqual(self.form.actionExit.text(), "E&xit", "Menu item Exit text incorrect")

    def test_window_size(self):
        """Tests That Main Window Size Is 453x492"""
        self.assertEqual(self.form.size(), QSize(453, 492), "Main window sized incorrectly")

    def test_update_status(self):
        """Tests That updateStatus successfully updates status"""
        self.form.updateStatus("Testing 1, 2, 3!")
        self.assertEqual(self.form.txtStatus.toPlainText(), "Testing 1, 2, 3!", "txtStatus is not updating properly")

    def test_clear_status(self):
        """Tests That updateStatus successfully clears status"""
        self.form.clearStatus()
        self.assertEqual(self.form.txtStatus.toPlainText(), "", "txtStatus is not clearing properly")

    def test_general_save_to_file_default_configuration(self):
        """Tests that default configuration loads properly"""
        self.form.load_default_configuration()
        self.assertEqual(self.form.config.get('general', 'save to file'), "False", "Default config item 'general save to file' incorrect")

    def test_general_debug_default_configuration(self):
        """Tests that default configuration loads properly"""
        self.form.load_default_configuration()
        self.assertEqual(self.form.config.get('general', 'debug'), "True", "Default config item 'general debug' incorrect")

    def test_general_debug_level_default_configuration(self):
        """Tests that default configuration loads properly"""
        self.form.load_default_configuration()        
        self.assertEqual(self.form.config.get('general', 'debug level'), "INFO", "Default config item 'general debug level' incorrect")

    def test_email_submission_enabled_default_configuration(self):
        """Tests that default configuration loads properly"""
        self.form.load_default_configuration()
        self.assertEqual(self.form.config.get('email_submission', 'enabled'), "False", "Default config item 'email_submission enabled' incorrect")

    def test_email_submission_fields_json_default_configuration(self):
        """Tests that default configuration loads properly"""
        self.form.load_default_configuration()
        self.assertEqual(self.form.config.get('email_submission', 'fields json'), "fields.json", "Default config item 'email_submission fields json' incorrect")

    def test_google_submission_default_configuration(self):
        """Tests that default configuration loads properly"""
        self.form.load_default_configuration()
        self.assertEqual(self.form.config.get('google_submission', 'enabled'), "False", "Default config item 'google_submission enabled' incorrect")

    def test_google_submission_pre_url_default_configuration(self):
        """Tests that default configuration loads properly"""
        self.form.load_default_configuration()
        self.assertEqual(self.form.config.get('google_submission', 'pre url'), "https://docs.google.com/forms/d/e/", "Default config item 'google_submission pre url' incorrect")

    def test_google_submission_post_url_default_configuration(self):
        """Tests that default configuration loads properly"""
        self.form.load_default_configuration()
        self.assertEqual(self.form.config.get('google_submission', 'post url'), "/formResponse", "Default config item 'google_submission post url' incorrect")

    def test_google_submission_fields_json_default_configuration(self):
        """Tests that default configuration loads properly"""
        self.form.load_default_configuration()
        self.assertEqual(self.form.config.get('google_submission', 'fields json'), "fields.json", "Default config item 'google_submission fields json' incorrect")

    def test_cpu_enabled_default_configuration(self):
        """Tests that default cpu enabled configuration loads properly"""
        self.form.load_default_configuration()
        self.assertEqual(self.form.config.get('cpu', 'enabled'), "True", "Default config item 'cpu enabled' incorrect")

    def test_gpu_enabled_default_configuration(self):
        """Tests that default gpu enabled configuration loads properly"""
        self.form.load_default_configuration()
        self.assertEqual(self.form.config.get('gpu', 'enabled'), "True", "Default config item 'gpu enabled' incorrect")

    def test_harddrive_enabled_default_configuration(self):
        """Tests that default harddrive enabled configuration loads properly"""
        self.form.load_default_configuration()
        self.assertEqual(self.form.config.get('harddrive', 'enabled'), "True", "Default config item 'harddrive enabled' incorrect")

    def test_location_enabled_default_configuration(self):
        """Tests that default location enabled configuration loads properly"""
        self.form.load_default_configuration()
        self.assertEqual(self.form.config.get('location', 'enabled'), "True", "Default config item 'location enabled' incorrect")

    def test_location_provider_default_configuration(self):
        """Tests that default location provider configuration loads properly"""
        self.form.load_default_configuration()
        self.assertEqual(self.form.config.get('location', 'provider'), "ipinfo", "Default config item 'location provider' incorrect")

    def test_memory_enabled_default_configuration(self):
        """Tests that default memory enabled configuration loads properly"""
        self.form.load_default_configuration()
        self.assertEqual(self.form.config.get('memory', 'enabled'), "True", "Default config item 'memory enabled' incorrect")

    def test_network_enabled_default_configuration(self):
        """Tests that default network enabled configuration loads properly"""
        self.form.load_default_configuration()
        self.assertEqual(self.form.config.get('network', 'enabled'), "True", "Default config item 'network enabled' incorrect")

    def test_sound_enabled_default_configuration(self):
        """Tests that default sound enabled configuration loads properly"""
        self.form.load_default_configuration()
        self.assertEqual(self.form.config.get('sound', 'enabled'), "True", "Default config item 'sound enabled' incorrect")

    def test_system_enabled_default_configuration(self):
        """Tests that default system enabled configuration loads properly"""
        self.form.load_default_configuration()
        self.assertEqual(self.form.config.get('system', 'enabled'), "True", "Default config item 'system enabled' incorrect")

    def test_speedtest_enabled_default_configuration(self):
        """Tests that default speedtest enabled configuration loads properly"""
        self.form.load_default_configuration()
        self.assertEqual(self.form.config.get('speedtest', 'enabled'), "True", "Default config item 'speedtest enabled' incorrect")

    def test_speedtest_provider_default_configuration(self):
        """Tests that default speedtest provider configuration loads properly"""
        self.form.load_default_configuration()
        self.assertEqual(self.form.config.get('speedtest', 'provider'), "fast", "Default config item 'speedtest provider' incorrect")


if __name__ == "__main__":
    unittest.main()
