
try:
	import frappe
	import json
	from frappe import _
	import frappe.www.list
	from frappe.utils import cstr
	

except Exception as e:
	print(f"import Failed")
#finally:
#	print(f"import Failed")

#main method executed on page load
def get_context(context):
	fields=[
  "title",
  "property_type",
  "host",
  "location",
  "price_per_night",
  "beds",
  "bedrooms",
  "description",
  "image_1",
  "image_2",
  "image_3",
  "image_4",
 ]
	houses=frappe.db.get_all('Property',fields=fields,  as_list=True)
	context.houses=houses

#__________________________________________________________
