from django.db import models

# Create your models here.
class IncomeTaxDetails(models.Model):
    income = models.IntegerField()
    timeperiod = models.CharField(blank=False,max_length=10)
    monthly = models.ForeignKey("CalculatedIncomeTax", on_delete=models.CASCADE, related_name="monthly_incometax")
    yearly = models.ForeignKey("CalculatedIncomeTax", on_delete=models.CASCADE, related_name="yearly_incometax")
    
    def __str__(self):
        return f"Calculated Tax for Income: {self.income} on {self.timeperiod} basis."

class CalculatedIncomeTax(models.Model):
    salary_before_tax = models.IntegerField()
    tax_deduction = models.IntegerField()
    salary_after_tax = models.IntegerField()

    def __str__(self):
        return f"Income: {self.salary_before_tax}, Tax: {self.tax_deduction} Salary: {self.salary_after_tax}"
    