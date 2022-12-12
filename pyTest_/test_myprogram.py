import os
import myprogram
import pytest
import shutil

class TetsDoubleIt:

    numbers_file_template = "testnums_template.txt"
    numbers_file_testor = "testnums.txt"

    def setup_class(self):
        shutil.copy(TetsDoubleIt.numbers_file_template, TetsDoubleIt.numbers_file_testor)

    def teardown_class(self):
        os.remove(TetsDoubleIt.numbers_file_testor)

    def test_doublelines(self):
        myprogram.doublelines(TetsDoubleIt.numbers_file_testor)
        old_vals = [int(line) for line in open(TetsDoubleIt.numbers_file_template)]
        new_vals = [int(line) for line in open(TetsDoubleIt.numbers_file_testor)]
        for old_val, new_val in zip(old_vals, new_vals):
            assert int(new_val) == int(old_val) * 2

    def test_doubleit_value(self):
        assert myprogram.doubleit(10) == 20

    def test_doubleit_type(self):
        with pytest.raises(TypeError):
            myprogram.doubleit("hello")

