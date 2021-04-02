from django.forms import ModelForm
from django import forms
from .models import  OrderDetails


class OrderForm(ModelForm):
	class Meta:
		model = OrderDetails
		fields = '__all__'

		widgets = {
			'company': forms.Select(attrs={'class':'form-control','style': 'height: 2.5em;'}),
			'vessel': forms.TextInput(attrs={'class':'form-control','style': 'height: 2.5em;'}),
			'odr': forms.Textarea(attrs={'class':'form-control','style': 'height: 2.5em;'}),
			'docs': forms.Textarea(attrs={'class':'form-control','style': 'height: 2.5em;'}),

			'supplier':forms.Textarea(attrs={'class':'form-control','style': 'height: 2.5em;'}),
			'qty': forms.TextInput(attrs={'class':'form-control','style': 'height: 2.5em;'}),
			'unit': forms.TextInput(attrs={'class':'form-control','style': 'height: 2.5em;'}),
			'size': forms.Textarea(attrs={'class':'form-control','style': 'height: 2.5em;'}),

			'weight': forms.TextInput(attrs={'class':'form-control','style': 'height: 2.5em;'}),
			'in1': forms.TextInput(attrs={'class':'form-control','style': 'height: 2.5em;'}),
			'whouse': forms.Select(attrs={'class':'form-control','style': 'height: 2.5em;'}),
			'by1': forms.Select(attrs={'class':'form-control','style': 'height: 2.5em;'}),

			'BLNO': forms.TextInput(attrs={'class':'form-control','style': 'height: 2.5em;'}),
			'port': forms.TextInput(attrs={'class':'form-control','style': 'height: 2.5em;'}),
			'outdate': forms.TextInput(attrs={'class':'form-control','style': 'height: 2.5em;'}),
			'REMARK': forms.Textarea(attrs={'class':'form-control','style': 'height: 2.5em;'}),

			'division': forms.Select(attrs={'class':'form-control','style': 'height: 2.5em;'}),
			'jobnumber': forms.TextInput(attrs={'class':'form-control','style': 'height: 2.5em;'}),
			

			
			}