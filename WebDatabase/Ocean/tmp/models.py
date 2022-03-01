from django.db import models
from django.forms import ModelForm
from django.core.files import File
# Create your models here.

class Dlsnp(models.Model):
    
    data_file = models.FileField()
    unique_code = models.CharField(max_length=200)
    predict_result = models.FileField()
    
    def add_predict_result(self, result_path, result_name):

        with open (result_path, "rb")as f:
             wrapped_file = File(f)
             self.predict_result.save(result_name, wrapped_file, save=True)
       
    def __str__(self):
        return self.unique_code
