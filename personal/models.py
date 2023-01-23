from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Personnel(models.Model):
    GENDER = (
        ("M", "Male"),
        ("F", "Female"),
    )
    
    department = models.ForeignKey(Department, related_name="personnel", on_delete=models.SET_NULL, null=True)
    firstname = models.CharField(max_length=50, blank=False)
    lastname = models.CharField(max_length=50, blank=False)
    is_staffed = models.BooleanField(default=False)
    title = models.CharField(max_length=50, blank=False)
    gender = models.CharField(choices=GENDER, default="M", max_length=50, blank=False)
    # updated_date = models.DateTimeField(auto_now=True)
    # created_date = models.DateTimeField(auto_now_add=True)
    salary = models.PositiveIntegerField()
    start_date = models.DateField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
