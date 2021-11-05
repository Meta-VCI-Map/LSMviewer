# LSMviewer

## About

LSMviewer is a user-interface for calculating the **Location Impact Score** and **Network Impact Score** of post-stroke cognitive impairment and dementia, based on lesion-symptom mapping. It offers an online and a standalone version of the tool.

Detailed descriptions of the risk scores used:
- **Location Impact Score**: https://doi.org/10.1016/S1474-4422(21)00060-0 
- **Network Impact Score**: https://doi.org/10.1161/STROKEAHA.119.025637

Information can also be found on the ***Meta VCI Map*** website: https://metavcimap.org/

## Build on your local server

Developing the application locally means hosting it on the user's device. The local server should work at this URL: http://127.0.0.1:8000. 
To do this, please follow the instructions below:

1. Download or clone the main branch on your device, create and activate the virtual environment using conda on command prompt:
 ```
git clone -b main https://github.com/Meta-VCI-Map/LSMviewer
conda env create -f environment.yml
conda activate env
```

2. Move into the directory of `manage.py` and create an `.env` file containing the _SECRET_KEY_ in the following form 
> SECRET_KEY = ' ... '

Then double-check that the name of this file is referred to in the `.gitignore`.

3. To launch the server, you can run 
```
python manage.py runserver
```

The local server is working at http://127.0.0.1:8000, as indicated by the
> LSMviewer/urls.py

If you want to change this URL, edit the urlpatterns in the above file.



## Usage

As mentioned above, the web application can be found at http://127.0.0.1:8000


#### Getting started

The user can upload a binary mask of a brain infarct of size `(182, 218, 182)`, visualize it on a 3D online viewer and select a risk score for calculation. 

The results will be displayed on the screen. An excel file with the detailed results on the **Network Impact Score** can be downloaded on the user's 
device if desired.



## Credits

LSMviewer is developed by Maria Leousi, on behaf of the ***Meta VCI Map*** consortium,
University Medical Center Utrecht, The Netherlands.
