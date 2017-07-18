from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from myapp.forms import CustomerForm
from myapp.models import Customer
# Create your views here.

def home(request):
	return render(request, 'home.html', {'key': "value" })
	
class CreateCustomerView(CreateView):
	queryset = Customer()
	template_name='customer.html'
	form_class = CustomerForm
	success_url = '/'