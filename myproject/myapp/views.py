from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from myapp.forms import CustomerForm, RentForm
from myapp.models import Customer, Rent, Car

# Create your views here.

def home(request):
	return render(request, 'home.html', {'key': "value" })
	
class CreateCustomerView(CreateView):
	queryset = Customer()
	template_name='customer.html'
	form_class = CustomerForm
	success_url = '/rent/'

class CreateRentView(CreateView):
	queryset = Rent()
	template_name ='rent.html'
	form_class = RentForm
	success_url = '/'

class ListCarView(ListView):
    queryset = Car.objects.all().order_by('-brand')
    template_name='car_list.html'
    context_object_name = "car_list"
    paginate_by = 5