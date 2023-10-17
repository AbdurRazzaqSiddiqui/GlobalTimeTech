from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import IncomeTaxDetails, CalculatedIncomeTax


# Create your views here.
def index(request):
    if request.method == 'POST':
        request.session['income'] = int(request.POST["income"])
        request.session['timeperiod'] = request.POST["timeperiod"]
        if request.session['timeperiod'] == "Monthly":
            request.session['salary_before_tax'] = request.session['income']*12
        elif request.session['timeperiod'] == "Yearly":
            request.session['salary_before_tax'] = request.session['income']
            
        request.session['tax']=0
        if (request.session['salary_before_tax']) > 600000 and request.session['salary_before_tax'] <= 1200000:
            request.session['tax'] = request.session['salary_before_tax'] * 0.025
        elif request.session['salary_before_tax'] > 1200000 and request.session['salary_before_tax'] <= 2400000:
            request.session['tax'] = request.session['salary_before_tax'] * 0.125
        elif request.session['salary_before_tax'] > 2400000 and request.session['salary_before_tax'] <= 3600000:
            request.session['tax'] = request.session['salary_before_tax'] * 0.225
        elif request.session['salary_before_tax'] > 3600000 and request.session['salary_before_tax'] <= 5000000:
            request.session['tax'] = request.session['salary_before_tax'] * 0.325
        elif request.session['salary_before_tax'] > 5000000:
            request.session['tax'] = request.session['salary_before_tax'] * 0.35

        request.session['salary_after_tax'] = int(request.session['salary_before_tax']) - int(request.session['tax'])
        yearly_salary = CalculatedIncomeTax.objects.create(salary_before_tax=int(request.session['salary_before_tax']),tax_deduction=int(request.session['tax']),salary_after_tax=int(request.session['salary_after_tax']))
        yearly_salary.save()

        monthly_salary = CalculatedIncomeTax.objects.create(salary_before_tax=int(request.session['salary_before_tax']/12),tax_deduction=int(request.session['tax']/12),salary_after_tax=int(request.session['salary_after_tax']/12))
        monthly_salary.save()

        details = IncomeTaxDetails.objects.create(income=request.session['income'],timeperiod=request.session['timeperiod'],monthly=monthly_salary,yearly=yearly_salary)
        details.save()
        return render(request, "IncomeTaxCalculator/index.html",{
            "monthly_salary":monthly_salary,
            "yearly_salary":yearly_salary,
            "results":True
        })
    else:
        return render(request, "IncomeTaxCalculator/index.html",{
            "results":False
        })