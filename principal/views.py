from django.shortcuts import render
from billing import get_integration

def index(request):
	pay_pal = get_integration("pay_pal")
	pay_pal.add_fields({
		"business": "MJeanC.104-facilitator@gmail.com",
		"item_name": "Curso Django",
		"invoice": "UID",
		"notify_url": "http://localhost:8000/paypal-ipn-handler/",
		"return_url": "http://localhost:8000/paypal/",
		"cancel_return": "http://localhost:8000/paypal/unsuccessful/",
		"amount": 0.01})
	return render(request, 'index.html', {'obj':pay_pal})