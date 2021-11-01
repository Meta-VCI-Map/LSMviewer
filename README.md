# LSMviewer

## About

LSMviewer is a user-interface for calculating the **Location Impact Score** and **Network Impact Score** of post-stroke cognitive impairment and dementia, based on lesion-symptom mapping. It offers an online and a standalone version of the tool.

Detailed descriptions of the risk scores used:
- **Location Impact Score**: https://doi.org/10.1016/S1474-4422(21)00060-0 
- **Network Impact Score**: https://doi.org/10.1161/STROKEAHA.119.025637

Information can also be found on the ***Meta VCI Map*** website: https://metavcimap.org/

## Usage

### Standalone tool version

Download the desktop application from the ***Meta VCI Map*** website, following this URL: https://metavcimap.org/lsmviewer


#### Prerequisites
Move the `LSMviewer.exe`  file into the `Source code` folder.

Make sure to add the path of the executable file LSMviewer.exe to the exclusions of your antivirus. See more details below:

	* for Avast https://support.avast.com/en-ww/article/Antivirus-scan-exclusions

	* for Marlwarebytes https://support.malwarebytes.com/hc/en-us/articles/360039024133-Exclude-detections-in-Malwarebytes-for-Windows-v3

	* for Norton https://support.norton.com/sp/en/us/home/current/solutions/v3672136
  
  
#### Getting started

To launch the application, run the executable file `LSMviewer.exe`.

One or multiple multiple binary masks of brain infarcts can be selected. However, note that the files should be of size `(182, 218, 182)` 
and that the user should not upload more than ~300 files at once, otherwise the application will crash.

The user will be asked to select a directory where the results will be saved in the format of an Excel file. 
Apart from this file, they will also be displayed inside a frame on the application window.

Some details on the results will appear in a frame at the bottom of the application window.
Note that the **Network Impact Score** may be undefined in cases where the uploaded file contains an isolated white matter infarct or an infratentorial incident.



### Online tool version

Find the online version of the application on the ***Meta VCI Map*** website following this URL: https://metavcimap.org/lsmviewer

#### Getting started

The user can upload a binary mask of a brain infarct of size `(182, 218, 182)`, visualize it on a 3D online viewer and select a risk score for calculation. 

The results will be displayed on the screen. An excel file with the detailed results on the **Network Impact Score** can be downloaded on the user's 
device if desired.



## Credits

LSMviewer is developed by Maria Leousi, on behaf of the *Meta VCI Map* consortium,
University Medical Center Utrecht, The Netherlands.
