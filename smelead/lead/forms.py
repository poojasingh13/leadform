from django import forms

class smeleadForm(forms.Form):
    	name = forms.CharField(max_length=200)
	organisation= forms.CharField(max_length=200)
	city= forms.CharField(max_length=200)
	emailId= forms.EmailField()
	contactno= forms.CharField(max_length=200)
    
