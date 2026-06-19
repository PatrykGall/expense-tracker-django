from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ExpenseForm
from .models import Category, Expense


def expense_list(request):
    expenses = Expense.objects.select_related("category").all()
    categories = Category.objects.all()

    category_id = request.GET.get("category")
    date_from = request.GET.get("date_from")
    date_to = request.GET.get("date_to")

    if category_id:
        expenses = expenses.filter(category_id=category_id)

    if date_from:
        expenses = expenses.filter(date__gte=date_from)

    if date_to:
        expenses = expenses.filter(date__lte=date_to)

    total = expenses.aggregate(total=Sum("amount"))["total"] or 0

    category_summary = (
        expenses
        .values("category__name")
        .annotate(total=Sum("amount"))
        .order_by("category__name")
    )

    chart_labels = [item["category__name"] for item in category_summary]
    chart_data = [float(item["total"]) for item in category_summary]

    context = {
        "expenses": expenses,
        "categories": categories,
        "total": total,
        "selected_category": category_id,
        "date_from": date_from,
        "date_to": date_to,
        "chart_labels": chart_labels,
        "chart_data": chart_data,
    }

    return render(request, "expenses/expense_list.html", context)


def expense_create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("expense_list")
    else:
        form = ExpenseForm()

    return render(
        request,
        "expenses/expense_form.html",
        {"form": form, "title": "Dodaj wydatek"}
    )


def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk)

    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("expense_list")
    else:
        form = ExpenseForm(instance=expense)

    return render(
        request,
        "expenses/expense_form.html",
        {"form": form, "title": "Edytuj wydatek"}
    )


def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)

    if request.method == "POST":
        expense.delete()
        return redirect("expense_list")

    return render(
        request,
        "expenses/expense_confirm_delete.html",
        {"expense": expense}
    )