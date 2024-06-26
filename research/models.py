from django.db import models

class Chercheur(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProjetRecherche(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    project_leader = models.ForeignKey(Chercheur, on_delete=models.CASCADE, related_name='led_projects')
    researchers = models.ManyToManyField(Chercheur, related_name='projects')

    def __str__(self):
        return self.title
    
class Publication(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    project = models.ForeignKey(ProjetRecherche, on_delete=models.CASCADE, related_name='publications')
    publication_date = models.DateField()
    
    def __str__(self):
        return self.title