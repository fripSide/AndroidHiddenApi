import os
from pathlib import Path
import subprocess
import shutil

OUT_PATH = "classes"

"""
copy all class files from services directory
"""

def forceMergeFlatDir(srcDir, dstDir):
	if not os.path.exists(dstDir):
		os.makedirs(dstDir)
	for item in os.listdir(srcDir):
		srcFile = os.path.join(srcDir, item)
		dstFile = os.path.join(dstDir, item)
		forceCopyFile(srcFile, dstFile)

def forceCopyFile (sfile, dfile):
	if os.path.isfile(sfile):
		shutil.copy2(sfile, dfile)

def isAFlatDir(sDir):
	for item in os.listdir(sDir):
		sItem = os.path.join(sDir, item)
		if os.path.isdir(sItem):
			return False
	return True


def copyTree(src, dst):
	for item in os.listdir(src):
		s = os.path.join(src, item)
		d = os.path.join(dst, item)
		if os.path.isfile(s):
			if not os.path.exists(dst):
				os.makedirs(dst)
			forceCopyFile(s,d)
		if os.path.isdir(s):
			isRecursive = not isAFlatDir(s)
			if isRecursive:
				copyTree(s, d)
			else:
				forceMergeFlatDir(s, d)

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

def create_out_dir(d):
	if not os.path.exists(d):
		os.mkdir(d)

def main():
	p = Path("services")
	create_out_dir(OUT_PATH)
	for fi, di, fs in os.walk("services"):
		if fi.endswith("classes"):
			print(fi)
			for d in di:
				src = os.path.join(fi, d)
				dst = os.path.join(OUT_PATH, d)
				copyTree(src, dst)
				#run_cmd(f"cp {src} {dst}")

if __name__ == "__main__":
	main()
