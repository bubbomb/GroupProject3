from django.db import models

class employees(models.Model):
    fname = models.CharField(max_length = 150)
    lname = models.CharField(max_length = 150)
    current_office = models.CharField(max_length = 150)
    phone  = models.CharField(max_length = 15)

class manufacturers(models.Model):
    name = models.CharField(max_length = 150)

class notes(models.Model):
    note = models.TextField()
    asset = models.ForeignKey(
        'assets',
        on_delete=models.CASCADE,
    )

class assets(models.Model):
    current_location = models.CharField(max_length = 150, null=True)
    org_tag = models.CharField(max_length=10, null=True)
    manufacturer = models.ForeignKey(
        'manufacturers',
        null=True,
        on_delete=models.CASCADE,
    )
    employee = models.ForeignKey(
        'employees',
        null=True,
        #on_delete=models.CASCADE,
    )
    part_number = models.CharField(max_length=254, null=True)
    description = models.TextField(null=True)
    date_implemented = models.DateField(null=True)

    def get_notes(self):
        return notes.objects.all().filter(asset =self)

    MANUFACTURER_CHOICES = (
        # Acer, 'Acer',
        # Alien, 'Alien',
        # Apple, 'Apple',
        # Asus, 'Asus',
        # Dell, 'Dell',
        # Google, 'Google',
        # HP, 'HP',
        # Lenovo, 'Lenovo',
        # LG, 'LG',
        # Microsoft, 'Microsoft',
        # Motorola, 'Motorola',
        # Nexus, 'Nexus',
        # Nokia, 'Nokia',
        # Razer, 'Razer',
        # Samsung, 'Samsung',
        # Sony, 'Sony',
        # Toshiba, 'Toshiba',
        # Other, 'Other'

    )
