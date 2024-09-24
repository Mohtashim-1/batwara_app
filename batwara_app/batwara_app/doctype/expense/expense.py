# Copyright (c) 2024, mohtashim and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Expense(Document):
	def before_save(self):
		self.apply_split()
  
	def apply_split(self):
		if self.split_method == "Equally":
			self.calculate_equal_splits()
		else:
			# manually
			pass

	def calculate_equal_splits(self):
		num_splits = len(self.splits)
		split_amount = self.amount / num_splits

		for s in self.splits:
			s.amount = split_amount 