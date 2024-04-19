from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ATMSite(models.Model):
    name = models.CharField(max_length=100)
    site_id = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_details = models.JSONField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.name