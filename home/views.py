from django.shortcuts import render
from django.http import HttpResponse
from home import models as hmod
from django import forms

# Create your views here.

def index(request):

	if request.method =="POST":

		#print(request.POST)
		form = request.POST
		#print(form.get('current_office'))

		current_office =form.get('current_office')
		manufacturer = form.get('manufacturer')
		other_manufacturer = form.get('other_manufacturer')
		date_implemented = form.get('date_implemented')
		org_tag = form.get('org_tag')
		part_number = form.get('manufacturer_part_number')
		maintenance_notes = form.get('maintenance_notes')
		description = form.get('description')


		#print(date_implemented)

		a = hmod.assets()
		a.current_location =current_office
		a.part_number = part_number
		a.org_tag = org_tag
		a.description = description
		a.date_implemented = date_implemented
		a.manufacturer = hmod.manufacturers.objects.get(name=manufacturer)
		print(a)
		a.save()


	#form = AssetForm()


	manufacturers = hmod.manufacturers.objects.all()
	print(manufacturers)
	#print('index page')
	return render(request, 'index.html',{'manufacturers':manufacturers})

def data(request):


	assets = hmod.assets.objects.all()
	print(assets)
	#print('data page!')

	
	return render(request, 'data.html', {'assets':assets})


def manufacturer(request):

	if request.method =="POST":

		print(request.POST)
		print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
		form = request.POST
		name = form.get('name')
		print(name)

		m = hmod.manufacturers()
		m.name = name
		m.save()

	return render(request,'manufacturer.html')



# class AssetForm(forms.Form):
# 	"""docstring for AssetForm"""
# 	current_location = forms.CharField(label='Current Location', max_length = 150)
# 	org_tag = forms.CharField(label ='Organizational Tag', max_length=10)
# 	part_number = forms.CharField(label='Part Number', max_length=50)
# 	description = forms.CharField(label='Description', max_length = 50000)

# 	#manufacturer = forms.ModelChoiceField(label = 'Manufacturer')
#   	#manufacturer = forms.ModelChoiceField(label = 'Manufacturer')
#     #date_implemented = forms.DateField(label = 'Date Implemented')
		
