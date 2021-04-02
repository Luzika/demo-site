from django.shortcuts import render, redirect
from .models import OrderDetails
from django.contrib import messages
from .forms import OrderForm


def Showodr(request):

	resultdisplay = OrderDetails.objects.all()
	return render(request,"ordertable.html",{'OrderDetails':resultdisplay})

def hienthi(request):
	resultdisplay = OrderDetails.objects.all()
	return render(request,"hienthi.html",{'OrderDetails':resultdisplay})

def Insert(request):
	if request.method=='POST':
		if request.POST.get('company') and request.POST.get('vessel') and request.POST.get('odr') and request.POST.get('supplier') and request.POST.get('qty') and request.POST.get('size') and request.POST.get('weight') and request.POST.get('in1') and request.POST.get('whouse') and request.POST.get('port') and request.POST.get('division'):
			saverecord=OrderDetails()
			saverecord.company=request.POST.get('company')
			saverecord.vessel=request.POST.get('vessel')
			saverecord.odr=request.POST.get('odr')
			saverecord.supplier=request.POST.get('supplier')
			saverecord.qty=request.POST.get('qty')
			saverecord.size=request.POST.get('size')
			saverecord.weight=request.POST.get('weight')
			saverecord.in1=request.POST.get('in1')
			saverecord.whouse=request.POST.get('whouse')
			saverecord.port=request.POST.get('port')
			saverecord.division=request.POST.get('division')
			saverecord.save()
			messages.success(request,'Record Saved Successfully!')
			return render(request,'inputorder.html')
	else:
			return render(request,'inputorder.html')

def Input2(request):

	# form = OrderForm()
	if request.method =='POST':
		form =OrderForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Record Saved Successfully!')
			form = OrderForm()
	else:
		form = OrderForm()
		context = {'form':form}
		return render(request, 'nhap.html', context)

