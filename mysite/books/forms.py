from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	email = forms.EmailField(required = False,label = 'E-mail address')
	message = forms.CharField(widget = forms.Textarea)
	#message = forms.TextField()
	
	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError('Not enough words!')
		return message
	
class RedirectInfomation(object):
	def __init__(self,flag,info):
		self.redirect = flag
		self.infomation = info
