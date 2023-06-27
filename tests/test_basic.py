from encrypt_desktop_files import copy_sampledata_to_dest,delete_sampledata_from_dest,SAMPLE_DATA_DEST_PATH, encrypt_folder_recursively

import os
import unittest

class TestBasic(unittest.TestCase):

    def test_can_create_files(self):

        if os.path.exists(SAMPLE_DATA_DEST_PATH):
            delete_sampledata_from_dest()

        copy_sampledata_to_dest()

        assert(os.path.exists(SAMPLE_DATA_DEST_PATH))
        assert(os.path.exists(SAMPLE_DATA_DEST_PATH+"/test.txt"))

        encrypt_folder_recursively(SAMPLE_DATA_DEST_PATH)
        assert(os.path.exists(SAMPLE_DATA_DEST_PATH+"/test.txt.enc"))