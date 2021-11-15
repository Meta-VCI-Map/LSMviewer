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

2. `LSMviewer/common.py` contains the general Django settings. The local server specific settings can be found in `LSMviewer/development.py`. Make sure that DJANGO_SETTINGS_MODULE looks for this file in order to run the application locally. Check this in `manage.py`:
```
DJANGO_SETTINGS_MODULE = 'LSMviewer.development' 
```

3. Move into the directory of `manage.py` and create an `.env` file containing the _SECRET_KEY_ in the following form 
> SECRET_KEY = ' ... '

Then double-check that the name of this file is referred to in the `.gitignore`.

3. To launch the server, you can run 
```
python manage.py runserver
```

The local server is working at http://127.0.0.1:8000, as indicated by the `LSMviewer/urls.py`

If you want to change this URL, edit the urlpatterns in the above file.


### Adding a new score
Adding new scores on the tool, requires some modifications in javascript/html and in python.

#### risk_scores_calculation/views.py
Handles the calculations in python. For the new score, create a function inside the `RequestResultViewSet class` that will handle the request for computing the score and will return the result in a json format.

#### risk_scores_calculation/urls.py
Creates request URLs for the API endpoints. Add the path to which the request for the score calculation mentioned above will be found.

#### templates/risk_score_calculation.html
Handles what is shown on the screeen. For the new score, you can add an option to the form with id="selection_form".
  
#### static/riskScoreCalculation.js
Handles the flow of the operations in html. Add a funtion for the new score that will take as input the file which is uploaded by the user and that creates a POST ajax request looking at the API endpoint's URL previously inserted in the `urls.py`. This way, the new score will be linked to the correct function for calculation in the `views.py`

## Build on remote server (using Antagonist.nl hosting)

To deploy the application on the remote server, please follow the instructions below:

1. Log in at https://metavcimap.org:2223/
2. Establish a connection with SSH. See more details at https://www.antagonist.nl/help/nl/webhosting/ssh
3. From the Extra Features section, choose Python Selector to manage the Python application 
![printscreen3](https://user-images.githubusercontent.com/23291570/139890544-f4c5b11b-27cb-49cb-8d15-22806ca6d849.png)

More details on how Python applications are created are available at https://www.antagonist.nl/blog/beginnen-met-python/

4. Activate the virtual environment by 
```
source /home/[user]/virtualenv/lsmviewer/3.7/bin/activate && cd /home/[user]/lsmviewer
```
The required packages for the environment are installed by `pip install [package-name]`.

5. The web application for the **LSMviewer** (_metavcimap.org/lsmviewer_) is already created on the server. The deployment branch is also cloned in this directory
```
git clone -b deployment https://github.com/Meta-VCI-Map/LSMviewer
```
6. The code from the GitHub repository can be found in _/home/[user]/lsmviewer/LSMviewer/_ and the logs file in _/home/[user]/logs/lsmviewer.log_
7. `LSMviewer/common.py` contains the general Django settings. The remote server specific settings can be found in `LSMviewer/production.py`. Make sure that DJANGO_SETTINGS_MODULE looks for this file in order to run the application locally. Check this in `wsgi.py`:
```
DJANGO_SETTINGS_MODULE = 'LSMviewer.LSMviewer.production' 
```
8. Move into the directory of `manage.py` and create an `.env` file containing the _SECRET_KEY_ in the following form 
> SECRET_KEY = ' ... '

Then double-check that the name of this file is referred to in the `.gitignore`.

9. Note that on the remote server, you are one directory deeper than on local server. The application should run from /home/[user]/lsmviewer/ but using the Git repository this path is extended by a directory: /home/[user]/lsmviewer/LSMviewer/. So, you will have to change some imports:
#### lsmviewer/LSMviewer/LSMviewer/production.py
```
...
from LSMviewer.LSMviewer.common import *
...

```
#### lsmviewer/LSMviewer/LSMviewer/urls.py
```
...
from LSMviewer.risk_scores_calculation.views
...
path('', include('LSMviewer.risk_scores_calculation.urls')),
...
```
#### lsmviewer/LSMviewer/risk_score_calculation/apps.py
```...
from LSMviewer.LSMviewer.common
...
name = 'LSMviewer.risk_scores_calculation'
...
```
#### lsmviewer/LSMviewer/risk_score_calculation/serializers.py
```
...
from LSMviewer.risk_scores_calculation.models 
...
```
#### lsmviewer/LSMviewer/risk_score_calculation/urls.py
```
...
from LSMviewer.risk_scores_calculation.views
...
```
#### lsmviewer/LSMviewer/risk_score_calculation/views.py
```
...
from LSMviewer.LSMviewer.common 
from LSMviewer.risk_scores_calculation.serializers
from LSMviewer.LSMviewer.production import STATIC_ROOT
...
```
For both the `calculate_location_score` and the `calculate_network_score functions` you should change the value of the variable `atlas_dir` from the static folder to STATIC_ROOT. In addition to that, you should make a copy of the images uploaded by the user into the pubic_html directory.
#### lsmviewer/LSMviewer/templates/risk_score_calculation.html
```
...
papayaparams_userUpload["images"] = [
 "\\static/MNI152_T1_1mm_brain_uint8.nii",
 "\\static/{{ filename }}"
];
...
```
10. The remote server is working at the Application URL defined in Python Selector, here at https://metavcimap.org/lsmviewer
11. The _public_html_ folder contains a folder with the same name as the application (here _lsmviewer_), where a `.htaccess` file is placed. This ensures that the server can find the application. In the same directory, folders with the names of the requests used from the application are placed containing `.htaccess` files as well.
12. Make sure to restart the application from https://metavcimap.org:2223/user/plugins/python_selector#/applications/lsmviewer if changes are applied on the files.


### Adding a new score
Adding new scores on the tool, requires some modifications in javascript/html and in python.

#### lsmviewer/LSMviewer/risk_scores_calculation/views.py
Handles the calculations in python. For the new score, create a function inside the `RequestResultViewSet class` that will handle the request for computing the score and will return the result in a json format.

#### lsmviewer/LSMviewer/risk_scores_calculation/urls.py
Creates request URLs for the API endpoints. Add the path to which the request for the score calculation mentioned above will be found.

#### lsmviewer/LSMviewer/templates/risk_score_calculation.html
Handles what is shown on the screeen. For the new score, you can add an option to the form with id="selection_form".
  
#### public_html/static/riskScoreCalculation.js
Handles the flow of the operations in html. Add a funtion for the new score that will take as input the file which is uploaded by the user and that creates a POST ajax request looking at the API endpoint's URL previously inserted in the `urls.py`. This way, the new score will be linked to the correct function for calculation in the `views.py`

#### public_html/lsmviewer
As mentioned before, this folder ensures that the server can find the application. When adding new scores to the tool, new request URLs for the API endpoints need to be added as well, as described above. These URLs will be visible by the application only if you create subfolders in _lsmviewer_ with the names of the requests and if you place a `.htaccess` file within.

Important notes: 
1. If you want to modify javascript or css files make sure to do that in the `public_html/static/` folder. The changes will not be visible if applied in `LSMviewer/static/`
2. Don't forget to restart the application if changes are applied.



## Usage

As mentioned above, the local web application can be found at http://127.0.0.1:8000 and remote web application at the Application URL; on the ***Meta VCI Map*** website following this link: https://metavcimap.org/lsmviewer


#### Getting started

The user can upload a binary mask of a brain infarct of size `(182, 218, 182)`, visualize it on a 3D online viewer and select a risk score for calculation. 

The results will be displayed on the screen. An excel file with the detailed results on the **Network Impact Score** can be downloaded on the user's 
device if desired.



## Credits

LSMviewer is developed by Maria Leousi, on behaf of the ***Meta VCI Map*** consortium,
University Medical Center Utrecht, The Netherlands.
