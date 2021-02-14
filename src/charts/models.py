from django.db import models
from authentication.models import CustomUser

# Create your models here.
class Chart(models.Model):
    """
    Define a chart model
    """

    DEPARTMENTS = (
        ("sales", "Sales"),
        ("finance", "Finance"),
        ("engineering", "Engineering"),
    )

    name = models.CharField(max_length=256)
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="charts"
    )
    department = models.CharField(choices=DEPARTMENTS, max_length=20)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-published",)

    def __str__(self):
        return self.name
