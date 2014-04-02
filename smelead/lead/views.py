from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from lead.forms import smeleadForm
from lead.models import leadform


def index(request):
    form = smeleadForm();
    if request.method =='POST':
	form =smeleadForm(request.POST)
	if form.is_valid():
		name = form.cleaned_data['name']
		organisation=form.cleaned_data['organisation']
		city =form.cleaned_data['city']
		emailId=form.cleaned_data['emailId']
		contactno =form.cleaned_data['contactno']
		leadform(name=name,organisation=organisation,city=city,emailId=emailId,contactno=contactno).save()
		return render_to_response('thanks.html',context_instance=RequestContext(request))
                	
    return render_to_response('index.html', {'form':form},context_instance=RequestContext(request))
