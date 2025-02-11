from django.db import models

class Professional(models.Model):
    name = models.CharField(max_length=255)
    social_name = models.CharField(max_length=255, blank=True, null=True)
    profession = models.CharField(max_length=100)
    address = models.TextField()
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Consultation(models.Model):
    date = models.DateTimeField()
    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE,
        related_name="consultations"
    )

    def __str__(self):
        return f"Consultation on {self.date} with {self.professional.name}"

