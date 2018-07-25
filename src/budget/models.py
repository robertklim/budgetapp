from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True, blank=True)
    budget = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def budget_balance(self):
        expense_list = Expense.objects.filter(project=self)
        total_expense_amount = 0
        for expense in expense_list:
            total_expense_amount += expense.amount

        return self.budget - total_expense_amount

    def total_expenses(self):
        expense_list = Expense.objects.filter(project=self)
        return len(expense_list)

class Category(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='expenses')
    name = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-amount',)

