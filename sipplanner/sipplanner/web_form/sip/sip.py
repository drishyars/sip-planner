import frappe

def get_context(context):
	# do your magic here
	print(context.template)
	if context.template == 'website/doctype/web_form/templates/web_list.html':
		context.template = 'sipplanner/sipplanner/web_form/sip/templates/web_list.html'
	# pass
