from datetime import date
from decimal import Decimal

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from .models import Category, Expense


class ExpenseModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Jedzenie")

    def test_create_expense(self):
        expense = Expense.objects.create(
            category=self.category,
            amount=Decimal("35.50"),
            date=date(2026, 6, 19),
            description="Obiad",
        )

        self.assertEqual(expense.category.name, "Jedzenie")
        self.assertEqual(expense.amount, Decimal("35.50"))
        self.assertEqual(expense.date, date(2026, 6, 19))
        self.assertEqual(expense.description, "Obiad")

    def test_expense_amount_must_be_positive(self):
        expense = Expense(
            category=self.category,
            amount=Decimal("0.00"),
            date=date(2026, 6, 19),
            description="Bledny wydatek",
        )

        with self.assertRaises(ValidationError):
            expense.full_clean()

    def test_category_string_representation(self):
        self.assertEqual(str(self.category), "Jedzenie")


class ExpenseViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Transport")

        self.expense = Expense.objects.create(
            category=self.category,
            amount=Decimal("250.00"),
            date=date(2026, 6, 18),
            description="Paliwo",
        )

    def test_expense_list_view_status_code(self):
        response = self.client.get(reverse("expense_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Paliwo")
        self.assertContains(response, "250.00")

    def test_expense_create_view(self):
        response = self.client.post(
            reverse("expense_create"),
            {
                "category": self.category.id,
                "amount": "99.99",
                "date": "2026-06-20",
                "description": "Testowy wydatek",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Expense.objects.filter(description="Testowy wydatek").exists()
        )

    def test_expense_update_view(self):
        response = self.client.post(
            reverse("expense_update", args=[self.expense.id]),
            {
                "category": self.category.id,
                "amount": "300.00",
                "date": "2026-06-21",
                "description": "Zmieniony wydatek",
            },
        )

        self.expense.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.expense.amount, Decimal("300.00"))
        self.assertEqual(self.expense.description, "Zmieniony wydatek")

    def test_expense_delete_view(self):
        response = self.client.post(
            reverse("expense_delete", args=[self.expense.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Expense.objects.filter(id=self.expense.id).exists()
        )