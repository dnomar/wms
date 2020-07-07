import os
import json
import abc


class FileExporter():

    def __init__(self):
        self.file

    def write(self, text2write: str):
        self.file.write(text2write)

    def close(self, text2write: str):
        self.file.close()
