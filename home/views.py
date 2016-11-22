from django.shortcuts import render
from django.http import HttpResponse
from home import models as hmod
from django import forms

# Create your views here.

def index(request):

	if request.method =="POST":

		print(request.POST)
		form = request.POST
		#print(form.get('current_office'))

		current_office =form.get('current_office')
		manufacturer = form.get('manufacturer')
		other_manufacturer = form.get('other_manufacturer')
		date_implemented = form.get('date_implemented')
		org_tag = form.get('org_tag')
		part_number = form.get('manufacturer_part_number')
		maintenance_notes = form.get('maintenance_notes')

		a = hmod.assets()
		a.current_office =current_office
		a.part_number = part_number
		a.org_tag = org_tag
		a.save()



	#print('index page')
	return render(request, 'index.html')

def data(request):


	assets = hmod.assets.objects.all()
	print(assets)
	print('data page!')

	

	return render(request, 'data.html', {'assets':assets})

# class AssetForm(forms.Form):
# 	"""docstring for AssetForm"""
# 	current_location = forms.CharField(label='Current Location', max_length = 150)
#     org_tag = forms.CharField(label ='Organizational Tag', max_length=10)
#     # manufacturer = forms.ModelChoiceField(label = 'Manufacturer',)

#     # employee = models.ForeignKey
#     # part_number = models.CharField(max_length=254)
#     # description = models.TextField()
#     # date_implemented = models.DateField()
