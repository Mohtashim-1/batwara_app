# Copyright (c) 2024, mohtashim and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestExpense(FrappeTestCase):
	def test_equal_split_calculation(self):
		# ToDo : to create test user before
		test_expense = frappe.get_doc({
			"doctype": "Expense",
			"paid_by": "shoaibmohtashim973@gmail.com",
			"description":"Test",
			"amount": 200,
			"splits":[
				{
					"user":"friend2@gmail.com"
				},
				{
					"user":"shoaibmohtashim973@gmail.com"
				}
			]
		}).insert()
  
		self.assertEqual(test_expense.splits[0].amount, 100)
		self.assertEqual(test_expense.splits[1].amount, 100)
