# risk_scores_calculation/models.py

from django.db import models
from pathlib import Path
import os
import time
import gzip
from LSMviewer.settings import MEDIA_ROOT

# Create your models here.
def rename(instance, filename):
    '''Rename filename by adding a timestamp'''

    if filename.endswith('.nii.gz'):
        file_nii = Path(filename).stem
        file = Path(file_nii).stem
        '''decompress the file'''
        instance = gzip.decompress(instance.image.read())
    elif filename.endswith('.nii'):
        file = Path(filename).stem
    else:
        filename = "Error"
        return os.path.join(filename)

    '''rename by timestamp'''
    timestamp = str(time.time())
    timestamp = timestamp.replace('.', '_')
    ext = '.nii'
    filename = file + '_' + timestamp + ext

    return os.path.join(filename)


class InfarctImage(models.Model):
    image = models.FileField(upload_to = rename)

    def __str__(self):
        return self.image


class CoefficientImage(models.Model):
    image = models.FileField()

    def __str__(self):
       return self.image


class RequestResult(models.Model):
    infarct_image = InfarctImage()
    coefficient_image = CoefficientImage()