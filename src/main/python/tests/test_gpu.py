import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5 import Qt
from PyQt5.QtCore import QSize
from unittest import TestCase
from spec_checker.modules.gpu import GpuRecords, GpuRecord
import main

app = QApplication(sys.argv)


class GpuTest(unittest.TestCase):
    """Tests the gpu scanner"""
    def setUp(self):
        """Create The Gui"""
        self.form = main.MainWindow()
        self.form.log.setLevel("NOTSET")
        self.results = self.form.specs.gpus.test()

    def test_results_is_GpuRecords(self):
        """Tests that the results from gpu.test() is a type <GpuRecords>"""
        self.assertEqual(type(self.results), type(GpuRecords()), "result of gpu.test() should be of type <GpuRecords>")

    def test_list_items_are_type_GpuRecord(self):
        """Tests that the first item in the results from gpu.test() is a type <GpuRecord>"""
        for i in range(len(self.results.list)):
            self.assertEqual(type(self.results.list[i]), type(GpuRecord()), "result of gpu.test() should be of type <GpuRecord>")

    def test_gpu_id_is_integer(self):
        """Tests that gpu_id is of type integer"""
        self.assertEqual(type(self.results.list[0].gpu_id), type(int()), "gpu_id should be an integer")

    def test_gpu_name_is_not_None(self):
        """Tests that gpu_name is not None"""
        self.assertNotEqual(self.results.list[0].gpu_name, None, "gpu_name should not be None")

    def test_gpu_load_is_not_None(self):
        """Tests that gpu_load is not None"""
        self.assertNotEqual(self.results.list[0].gpu_load, None, "gpu_load should not be None")

    def test_gpu_free_memory_is_not_None(self):
        """Tests that gpu_free_memory is not None"""
        self.assertNotEqual(self.results.list[0].gpu_free_memory, None, "gpu_free_memory should not be None")

    def test_gpu_used_memory_is_not_None(self):
        """Tests that gpu_used_memory is not None"""
        self.assertNotEqual(self.results.list[0].gpu_used_memory, None, "gpu_used_memory should not be None")

    def test_gpu_total_memory_is_not_None(self):
        """Tests that gpu_total_memory is not None"""
        self.assertNotEqual(self.results.list[0].gpu_total_memory, None, "gpu_total_memory should not be None")

    def test_gpu_temperature_is_not_None(self):
        """Tests that gpu_temperature is not None"""
        self.assertNotEqual(self.results.list[0].gpu_temperature, None, "gpu_temperature should not be None")


if __name__ == "__main__":
    unittest.main()
