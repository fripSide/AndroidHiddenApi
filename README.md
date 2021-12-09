### About
### Extract jar from AOSP source code compiling files

```
# android.jar service helper API
out/soong/.intermediates/frameworks/base/framework/android_common/turbine-combined/framework.jar

# service implement API
# classes floder in 
out/soong/.intermediates/frameworks/base/services 
# extract all classes
python3 combine.py
```



### Extract jar from Emulator

AndroidApiExtract is a tool used to extract full framework jar with hiden APIs from Android devices. 

framework-full.jar: contain all the classes.
framework-lite.jar: only contain android framework and service classes. (use for static analysis)

Extract Methods in oat2smali2dex2jar.py:

For API23-25:

	First, use OdexAndOat2Smali() scan and convert every .odex and .oat files in /system/framework directory to smali files in one out directory.
	
	Second, use Smali2Dex() convert the smali files to .dex files.
	
	Third, use Dex2Jar() convert .dex files to jar for 

For API26+:

	First, use vdexExtractor to get smali files from /system/framework directory
	 
	Second, use Dex2Jar() convert .dex files to jar for API26+

For API29+:
	https://github.com/aeab13/android-jar-with-hidden-api