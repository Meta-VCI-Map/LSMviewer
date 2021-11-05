# LSMviewer

## About

LSMviewer is a user-interface for calculating the **Location Impact Score** and **Network Impact Score** of post-stroke cognitive impairment and dementia, based on lesion-symptom mapping. It offers an online and a standalone version of the tool.

Detailed descriptions of the risk scores used:
- **Location Impact Score**: https://doi.org/10.1016/S1474-4422(21)00060-0 
- **Network Impact Score**: https://doi.org/10.1161/STROKEAHA.119.025637

Information can also be found on the ***Meta VCI Map*** website: https://metavcimap.org/

## Usage

### Create your own executable

The original code of the executable file can be found in `LSMviewer.py` while the executable file itself can be downloaded from the Releases (https://github.com/Meta-VCI-Map/LSMviewer/releases).
If a custom version of the executable is derired, teh user will need to convert the `LSMviewer.py` script to an executable by using a simple graphical interface.
To do this, please follow the instructions below:

1. Download or clone the releases branch on your device, create and activate the virtual environment using conda on command prompt:
```
git clone -b releases https://github.com/Meta-VCI-Map/LSMviewer
conda env create -f environment.yml
conda activate env
``` 

2. Moving on to the creation of the executable, you will have to open the graphical interface 
``` 
auto-py-to-exe.exe
```
browse to the `LSMviewer.py` file, select the 'One File' and 'Windows Based' choices and proceed to the conversion as shown below:

![printscreen1](https://user-images.githubusercontent.com/23291570/139864771-07d7ed53-8c78-4b7c-850f-fe4125a5b4b8.png)


3. Once completed, the executable file `LSMviewer.exe` can be found in the newly created `output` folder:

![printscreen2](https://user-images.githubusercontent.com/23291570/139866215-e27e9fa5-8115-462b-9658-50967e860f8b.png)



### Use the latest available release

You can also use the latest available release containing the executable by following the steps below:

1. Download the `LSMviewer.exe` and source code from the Releases: https://github.com/Meta-VCI-Map/LSMviewer/releases

2. Move the `LSMviewer.exe` file into the `Source code` folder.

3. Make sure to add the path of the executable file LSMviewer.exe to the exclusions of your antivirus. See more details below:

	* for Avast https://support.avast.com/en-ww/article/Antivirus-scan-exclusions

	* for Marlwarebytes https://support.malwarebytes.com/hc/en-us/articles/360039024133-Exclude-detections-in-Malwarebytes-for-Windows-v3

	* for Norton https://support.norton.com/sp/en/us/home/current/solutions/v3672136
  
  
## Getting started

To launch the application, run the executable file `LSMviewer.exe`.

One or multiple multiple binary masks of brain infarcts can be selected. However, note that the files should be of size `(182, 218, 182)` 
and that the user should not upload more than ~300 files at once, otherwise the application will crash.

The user will be asked to select a directory where the results will be saved in the format of an Excel file. 
Apart from this file, they will also be displayed inside a frame on the application window.

Some details on the results will appear in a frame at the bottom of the application window.
Note that the **Network Impact Score** may be undefined in cases where the uploaded file contains an isolated white matter infarct or an infratentorial incident.


## Credits

LSMviewer is developed by Maria Leousi, on behaf of the ***Meta VCI Map*** consortium,
University Medical Center Utrecht, The Netherlands.
