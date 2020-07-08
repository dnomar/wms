import sys
sys.path.append(r"C:\Users\van-gerald.olivares\Documents\08 Code\wms")
from src.app.service.unit_of_work import TxtExportUnitOfWork
import os


def test_text2file():
    # given
    local_folder = r"C:\Users\van-gerald.olivares\Documents\symplex_reports"
    txt = "aaaaa"

    uow = TxtExportUnitOfWork(local_folder + r"\log_file.txt", "w")
    with uow:
        uow.write(txt)

    file2 = open(local_folder + r"\log_file.txt", "r")
    read_text = file2.read()
    assert read_text == txt
    file2.close()
    os.remove(local_folder + r"\log_file.txt")
