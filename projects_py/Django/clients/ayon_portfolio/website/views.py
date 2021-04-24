from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
# from django.http import HttpResponse
# from datetime import datetime
from django.contrib import messages
from .models import Contact
from .forms import *


@csrf_protect
def home(request):
	form = ContactForm()
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your Message Has Been Sent!')
			return redirect('home')
	context = {'form': form}
	# return HttpResponse("Hello World!!!")
	return render(request, "website/index.html", context)
