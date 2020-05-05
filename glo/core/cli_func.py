# coding: utf8

import os
from string import Template

from glo.core.resource_params import ResourceParams


class RTemplate(Template):
	delimiter = '&_'

TPL_DATA = dict()
FRAMEWORK = ''
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def __create_file(path, inner_content):
	"""
	创建文件
	"""
	if not os.path.exists(path) or path.split(os.path.sep)[-1] == '__init__.py':
		with open(path, 'w') as f:
			f.write(inner_content)

def __create_files(src_path, target_path, file_names):
	if not os.path.exists(target_path):
		os.makedirs(target_path)

	for name in file_names:
		if name.endswith('.pyc'):
			continue

		src_file_path = src_path + os.path.sep + name
		with open(src_file_path, 'r') as f:
			content_tmp = f.read()

		print src_file_path, '----------'
		content = RTemplate(content_tmp).substitute(TPL_DATA)
		name = RTemplate(name).substitute(TPL_DATA)
		target_file_path = target_path + os.path.sep + name
		__create_file(target_file_path, content)

def __create_dirs(dir_path, dirs):
	"""
	创建目录
	"""
	for dir in dirs:
		full_path = '{}{}'.format(dir_path, dir)
		if not os.path.exists(full_path):
			os.makedirs(full_path)
			if FRAMEWORK == 'rust':
				__create_file('{}{}__init__.py'.format(full_path, os.path.sep), '# coding: utf8')

def init_project(framework, service_name):
	"""
	初始化项目
	"""
	global TPL_DATA, FRAMEWORK
	FRAMEWORK = framework
	TPL_DATA['service_name'] = service_name

	TEMPLATE_FILES_PATH = os.path.join(CURRENT_DIR, '..{sep}templates{sep}{framework}_project{sep}init'.format(
		sep = os.path.sep,
		framework = framework
	))
	target_relative_path = '.{sep}{service_name}{sep}'.format(
		sep = os.path.sep,
		service_name = service_name
	)
	for root, dirs, files in os.walk(TEMPLATE_FILES_PATH):
		sps = root.split(TEMPLATE_FILES_PATH)
		if len(sps) == 1:
			target_path = target_relative_path
			src_path = sps[0]
		else:
			target_path = '{rr}{sep}{tp}{sep}'.format(
				rr = target_relative_path,
				sep = os.path.sep,
				tp = sps[1]
			)
			src_path = root
		if dirs:
			__create_dirs(target_path, dirs)

		if files:
			print src_path, "============"
			__create_files(src_path, target_path, files)

def __register_ghost_api(project_path):
	with open(os.path.join(project_path, 'api', 'resources.go'), 'r') as f:
		lines = f.readlines()
		content = """	_ "{}/api/{}"\n""".format(TPL_DATA['project_name'], TPL_DATA['resource_name'])
		lines.insert(-1, content)

	with open(os.path.join(project_path, 'api', 'resources.go'), 'wb') as f:
		f.write(''.join(lines))

def __register_ghost_db(project_path):
	with open(os.path.join(project_path, 'db', 'init.go'), 'r') as f:
		lines = f.readlines()
		content = """	_ "{}/db/{}"\n""".format(TPL_DATA['project_name'], TPL_DATA['resource_name'])
		lines.insert(4, content)

	with open(os.path.join(project_path, 'db', 'init.go'), 'wb') as f:
		f.write(''.join(lines))

def __add_ghost_resource(resource_params, template_path, project_path):
	api_files = []
	db_files = []
	domain_files = []
	api_src_path = os.path.join(template_path, 'api')
	domain_src_path = os.path.join(template_path, 'domain')
	db_src_path = os.path.join(template_path, 'db')
	for _, __, files in os.walk(api_src_path):
		api_files = files
	for _, __, files in os.walk(domain_src_path):
		domain_files = files
	for _, __, files in os.walk(db_src_path):
		db_files = files

	resource_name = resource_params.resource_name
	__create_files(api_src_path, os.path.join(project_path, 'api', resource_name), api_files)
	__register_ghost_api(project_path)
	__create_files(domain_src_path, os.path.join(project_path, 'domain', 'model', resource_name), domain_files)
	__create_files(db_src_path, os.path.join(project_path, 'db', resource_name), db_files)
	__register_ghost_db(project_path)

def add_resource(resource_params):
	"""
	增加资源
	"""
	if not os.getcwd().endswith(resource_params.project_name):
		raise Exception('you need to enter into the project dir and run glo add !!!')
	template_path = os.path.join(CURRENT_DIR, '..{sep}templates{sep}{framework}_project{sep}resource'.format(
		sep=os.path.sep,
		framework=resource_params.framework
	))
	project_path = '.'
	resource_params.fill_dict(TPL_DATA)
	if resource_params.framework == 'ghost':
		__add_ghost_resource(resource_params, template_path, project_path)

def __addon_file_content(path, inner_content):
	"""
	追加文件内容
	"""
	with open(path, 'a') as f:
		f.write(inner_content)

if __name__ == '__main__':
	# init_project('ghost', 'test')
	add_resource(ResourceParams(
		"ghost", "test", "woman", "women"
	))