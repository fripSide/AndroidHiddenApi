# coding: utf-8
# created at 2019/7/16
__author__ = "yuanzd123"

import os
import subprocess
from pathlib import Path

api = '26'
api_directory = Path('D:', '/', 'AndroidApiExtract', 'api-versions', api)
smali_directory = Path('D:', '/', 'AndroidApiExtract')
dex_directory = Path('D:', '/', 'AndroidApiExtract', 'dex-tools-2.1', api)

def OdexAndOat2Smali():
    for dirpath, dirnames, filenames in os.walk(api_directory):
        for file in filenames:
            # print (os.path.join(dirpath, file))
            filepath = dirpath + os.sep + file
            if filepath.endswith(".odex") or filepath.endswith(".oat"):
                basename = os.path.basename(filepath)
                subprocess.check_call(["java", "-jar", "D:\\AndroidApiExtract\\baksmali-2.2.7.jar", "x", "-a", api, "-c", "D:\\AndroidApiExtract\\api-versions\\"+api+"\\x86_64\\boot.oat", "-d", "D:\\AndroidApiExtract\\api-versions\\"+api+"\\x86_64\\", filepath, "-o", api+"_"+basename], shell=True)
                print (filepath)

def Smali2Dex():
    for dirpath, dirnames, filenames in os.walk(smali_directory):
        for dir in dirnames:
            if dir.startswith('25_'):
                filepath = dirpath + os.sep + dir + "\\"
                subprocess.check_call(["java", "-jar", "D:\\AndroidApiExtract\\smali-2.2.7.jar", "ass", "-a", api, filepath, "-o", dir+".dex"], shell=True)
                print(filepath)

def Dex2Jar():
    for dirpath, dirnames, filenames in os.walk(dex_directory):
        for file in filenames:
            # print (os.path.join(dirpath, file))
            filepath = dirpath + os.sep + file
            basename = os.path.basename(filepath)
            subprocess.check_call(["D:\\AndroidApiExtract\\dex-tools-2.1\\d2j-dex2jar.bat", "D:\\AndroidApiExtract\\dex-tools-2.1\\"+api+"\\"+basename], shell=True)

def Dex2JarMod():
    for dirpath, dirnames, filenames in os.walk(dex_directory):
        for file in filenames:
            # print (os.path.join(dirpath, file))
            filepath = dirpath + os.sep + file
            subprocess.check_call(["D:\\AndroidApiExtract\\dex-tools-2.1\\d2j-dex2jar.bat", filepath], shell=True)

def main():
    # OdexAndOat2Smali()
    # Smali2Dex()
    # Dex2Jar()
    Dex2JarMod()

if __name__ == "__main__":
	main()