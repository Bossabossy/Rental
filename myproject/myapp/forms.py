from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm
from myapp.models import Customer
from myapp.models import Rent
class CustomerForm(ModelForm):
	class Meta:
		model =  Customer
		exclude=[]
		
	def __init__(self, *args, **kwargs):
		super(CustomerForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))

class RentForm(ModelForm):
	class Meta:
		model =  Rent
		exclude=[]
		
	def __init__(self, *args, **kwargs):
		super(RentForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))