# coding: utf8

class ResourceParams(object):
	__slots__ = (
		'framework',
		'project_name',
		'resource_name',
		'resource_title',
		'resource_plural',
		'resource_title_plural'
	)

	def __init__(self, framework, project_name, name, plural):
		self.framework = framework
		self.project_name = project_name
		self.resource_name = name
		self.resource_plural = plural
		self.resource_title = name.title()
		self.resource_title_plural = plural.title()

	def fill_dict(self, tpl_data):
		tpl_data['framework'] = self.framework
		tpl_data['project_name'] = self.project_name
		tpl_data['service_name'] = self.project_name
		tpl_data['resource_name'] = self.resource_name
		tpl_data['resource_plural'] = self.resource_plural
		tpl_data['resource_title'] = self.resource_title
		tpl_data['resource_title_plural'] = self.resource_title_plural