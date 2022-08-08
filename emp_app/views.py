from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department 
from datetime import datetime
from django.db.models import Q
def index(request):
	return render(request,'index.html')

def search(request):
	d1=Department(name='HR',location='Mumbai')
	d2=Department(name='Finance',location='Delhi')
	d3=Department(name='IT',location='Hyderabad')
	d4=Department(name=,'Marketing'location='Pune')
	d5=Department(name=,'Admin'location='Agra')
	d6=Department(name=,'Development'location='Bhubaneswar')
	d1.save()
	d2.save()
	d3.save()
	d4.save()
	d5.save()
	d6.save()
	r1=Role(name='System Administrator')
	r2=Role(name='IT Manager')
	r3=Role(name='Web development project manager')
	r4=Role(name='Front-end developer')
	r5=Role(name='Back-end developer')
	r6=Role(name='Information security engineer')
	r7=Role(name='Data scientist')
	r8=Role(name='Network architect')
	r9=Role(name='Software engineer')
	r10=Role(name='Cloud services provider')
	r11=Role(name='Technical lead')
	r12=Role(name='Admin team member')
	r1.save()
	r2.save()
	r3.save()
	r4.save()
	r5.save()
	r6.save()
	r7.save()
	r8.save()
	r9.save()
	r10.save()
	r11.save()
	r12.save()

	return render(request,'status.html')	

def view_emp(request):
	emps=Employee.objects.all()
	context={
	'emps':emps
	}
	
	return render(request,'view.html',context)

def add_emp(request):
	if request.method == 'POST':
		fn= request.POST["fn"]
		ln= request.POST["ln"]
		dept= request.POST["dept"]
		sal= int(request.POST["sal"])
		b= int(request.POST["b"])
		role= request.POST["role"]
		phone= int(request.POST["phone"])
			
		emp=Employee(first_name=fn,last_name=ln,dept_id=dept,role_id=role,salary=sal,bonus=b,phone=phone,hire_date=datetime.now())
		emp.save()
		message="Added user"
		context={
		'message':message
		}
		return render(request, 'status.html',context)   
	else:
		roles=Role.objects.all()
		depts=Department.objects.all()
		context={
		'roles':roles,
		'depts':depts
		}
		
		return render(request,'add.html',context)
	
		


def del_emp(request,emp_id=0):
	if emp_id:
		try:
			emp_to_be_removed=Employee.objects.get(id=emp_id)
			emp_to_be_removed.delete()
			message="Deleted Successfully !!"
			context={
			'message':message
			}
			return render(request, 'status.html',context)   
		except:
			message="Invalid Emp Id"
			context={
			'message':message
			}
			return render(request, 'status.html',context) 
	emps=Employee.objects.all()
	context={
	'emps':emps
	}
	return render(request,'del.html',context)


def search_emp(request):
	if request.method == 'POST':
		name = request.POST['name']
		#dept = request.POST['dept']
		role = request.POST['role']
		emps = Employee.objects.all()
		if name:
			emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
		#if dept:
		#    emps = emps.filter(dept__name__icontains = dept)
		if role:
			emps = emps.filter(role__name__icontains = role)
		search_page=True
		context = {
			'emps': emps,
			"search_page":search_page
		}
		return render(request, 'search.html', context)

	else:
		
	   search_page=False
	   context={
		"search_page":search_page
		}
	
	   return render(request,'search.html',context)	
def edit_emp(request,emp_id=0):
	if emp_id:
		try:
			emp_to_be_edit=Employee.objects.get(id=emp_id)
			flag=True	
			roles=Role.objects.all()
			depts=Department.objects.all()
			context={
			'roles':roles,
			'depts':depts,
			'emp_to_be_edit':emp_to_be_edit,
			'flag':flag
			}
			return render(request, 'edit.html',context)   
		except:
			message="Invalid Emp Id"
			context={
			'message':message
			}
			return render(request, 'status.html',context)
	else:		 
		emps=Employee.objects.all()
		edit_page=True
		context={
		'emps':emps,
		"edit_page":edit_page
		}
	
		return render(request,'edit.html',context)				

def edit_emp_details(request,emp_id):
	if request.method == 'POST':
		emp=Employee.objects.get(id=emp_id)
		emp.first_name=request.POST["fn"]
		emp.last_name=request.POST["ln"]
		emp.dept_id=request.POST["dept"]
		emp.role_id=request.POST["role"]
		emp.salary=int(request.POST["sal"])
		emp.bonus=int(request.POST["b"])
		emp.phone=int(request.POST["phone"])
		emp.save()
		message="Updated User"
		context={
		'message':message
		}
		return render(request, 'status.html',context)   
	else:
		emps=Employee.objects.all()
		edit_page=True
		context={
		'emps':emps,
		"edit_page":edit_page
		}
		return render(request,'edit.html',context)	


