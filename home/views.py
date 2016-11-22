from django.shortcuts import render
from django.http import HttpResponse
from home import models as hmod
from django import forms

# Create your views here.

def index(request):

	if request.method =="POST":
		
		print(request.POST)
		form = request.POST
		print(form.get('current_office'))

	print('index page')
	return render(request, 'index.html')

def data(request):

	template_vars = []

	print('data page!')

	return render(request, 'data.html', template_vars)

# class AssetForm(forms.Form):
# 	"""docstring for AssetForm"""
# 	current_location = forms.CharField(label='Current Location', max_length = 150)
#     org_tag = forms.CharField(label ='Organizational Tag', max_length=10)
#     # manufacturer = forms.ModelChoiceField(label = 'Manufacturer',)

#     # employee = models.ForeignKey
#     # part_number = models.CharField(max_length=254)
#     # description = models.TextField()
#     # date_implemented = models.DateField()
