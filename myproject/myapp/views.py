from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from myapp.forms import CustomerForm
from myapp.models import Customer
from myapp.forms import RentForm
from myapp.models import Rent
# Create your views here.

def home(request):
	return render(request, 'home.html', {'key': "value" })
	
class CreateCustomerView(CreateView):
	queryset = Customer()
	template_name='customer.html'
	form_class = CustomerForm
	success_url = '/'
class CreateRentView(CreateView):
	queryset = Rent()
	template_name ='rent.html'
	form_class = RentForm
	success_url = '/'