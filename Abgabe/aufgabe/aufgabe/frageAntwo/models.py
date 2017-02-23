from django.db import models

# Create your models here.

class Frage(models.Model):
    text = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.text[:1000] 
    

	
	
class Antwort(models.Model):
    text = models.TextField(max_length=1000)
    isAkzeptiert = models.BooleanField(default=False)
    frage = models.ForeignKey(Frage)
	
    def __str__(self):
        return self.text[:1000] 
		
		
