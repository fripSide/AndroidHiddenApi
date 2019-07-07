# coding: utf-8
# created at 2019/3/13
__author__ = "fripSide"

import os
import shutil
import zipfile
import time
import subprocess
from threading import Thread
from datetime import datetime

ADB = r"D:\dev\AndroidSDK\platform-tools\adb.exe"
# UNZIP = r"D:\dev\Git\usr\bin\unzip.exe"
DEX2JAR = r"D:\tools\Android\dex-tools-2.1-SNAPSHOT\d2j-dex2jar.bat"
OAT2DEX = r"D:\tools\Android\oat2dex.jar"


def run_cmd(cmd, cwd=None, timeout=60):
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd, shell=True)
	try:
		outs, errs = proc.communicate(timeout=timeout)
	except subprocess.TimeoutExpired:
		import os
		import signal
		proc.kill()
		outs = ""
	return str(outs)

def get_file_path(walk_dir, name=None, ext=None):
	ret = []
	all_file = []
	for root, subdirs, files in os.walk(walk_dir):
		all_file += files
	print(all_file)
	if name:
		pass

def pull_framework():
	print(run_cmd("{} pull system/framework".format(ADB)))
	if not os.path.exists("framework"):
		print("Extract Framework Failed\n")
		exit(-1)

def extract_boot():
	pass
	
def extract_others():
	pass

def jar_combine():
	cmd = "{} ".format(UNZIP)

def unzip_file(file, out_path):
	zip_file = zipfile.ZipFile(file, "r")
	zip_file.extractall(out_path)
	zip_file.close()

def main():
	print("Usage: extrat_jar.py path/to/framework")
	#pull_framework()
	unzip_file("wifi-service-dex2jar.jar", "wifi")
	get_file_path("framework1")
	extract_boot()
	extract_others()
	jar_combine()

if __name__ == "__main__":
	main()