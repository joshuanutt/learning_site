from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from . import forms

@login_required
def home(request):
	user = request.user
	return render(request, 'home.html',{'user':user})

def suggestion_view(request):
	form = forms.SuggestionForm()

	if request.method == 'POST':
		form = forms.SuggestionForm(request.POST)
		if form.is_valid():
			send_mail(
				'Suggestion from {}'.format(form.cleaned_data['name']),
				form.cleaned_data['suggestion'], 
				'{name} <{email}>'.format(**form.cleaned_data),
				['josh.nutt@yahoo.com']
			)
			messages.add_message(request, messages.SUCCESS,
								'Thanks for your suggestion!')

			return HttpResponseRedirect(reverse('suggestion'))

	return render(request, 'suggestion_form.html',{'form':form})
