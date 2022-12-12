from exceptions.dictionary_file_with_exception_task import ConfigDict, ConfigKeyError
import os
import shutil
import pytest
from pathlib import Path

class TestConfigDict:
    existing_fn = r"C:\\Users\yahiram\\OneDrive - Intel Corporation\\Desktop\\try_python\\pyTest_\\config_file.txt"
    existing_fn_template =  Path(r"C:\Users\yahiramorporation\Desktop\try_python\pyTest_", "config_file_template.txt") #r"C:\Users\yahiramorporation\Desktop\try_python\pyTest_\config_file_template.txt"
    new_fn = r"C:\Users\yahiramorporation\Desktop\try_python\pyTest_\config_file_new.txt"
    bad_path = r"\some\awful\path\that\doesnt\exist\file.txt"

    def setup_class(self):
        shutil.copy(TestConfigDict.existing_fn_template, TestConfigDict.existing_fn)

    def teardown_class(self):
        os.remove(TestConfigDict.new_fn)

    def test_obj(self):
        cd = ConfigDict(TestConfigDict.existing_fn)
        assert isinstance(cd, ConfigDict)
        assert isinstance(cd, dict)

    def test_existing_filename(self):
        cd = ConfigDict(TestConfigDict.existing_fn)
        assert cd._filename == TestConfigDict.existing_fn

    def test_new_filename(self):
        assert not os.path.isfile(TestConfigDict.new_fn)
        cd = ConfigDict(TestConfigDict.new_fn)
        assert cd._filename == TestConfigDict.new_fn
        assert os.path.isfile(cd._filename)

    def test_bad_filepath(self):
        with pytest.raises(IOError):
            ConfigDict(TestConfigDict.bad_path)

    def test_read_dict(self):
        cd = cd = ConfigDict(TestConfigDict.existing_fn)
        assert cd['a'] == '5'
        assert cd['b'] == '10'
        assert cd['c'] == 'this=that'

        with pytest.raises(ConfigKeyError):
            print(cd['x'])

    def test_write_dict(self):
        cd = ConfigDict(TestConfigDict.existing_fn)
        cd['zz'] = 'top'
        cd2 = cd = ConfigDict(TestConfigDict.existing_fn)
        assert cd2['zz'] == 'top'


