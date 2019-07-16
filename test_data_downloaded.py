import unittest
import os


class test_data_downloaded(unittest.TestCase):
    """
    Checks that there was actually something downloaded before running other tests!
    """

    def check_for_download(self):
        self.assertTrue(os.stat("old.txt").st_size != 0, "Nothing was downloaded from the artifactory server!")
