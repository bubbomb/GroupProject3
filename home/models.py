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
    org_tag = models.CharField(max_length=10)
    manufacturer = models.ForeignKey(
        'manufacturers',
        on_delete=models.CASCADE,
    )
    employee = models.ForeignKey(
        'employees',
        on_delete=models.CASCADE,
    )
    part_number = models.CharField(max_length=254)
    description = models.TextField()
    date_implemented = models.DateField()

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
