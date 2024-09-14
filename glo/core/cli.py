# coding: utf8

import os
import click

from glo.core.cli_func import add_resource, init_project
from glo.core.helper import get_plural_for_word
from glo.core.resource_params import ResourceParams

@click.group()
def cli():
    pass

@click.command()
@click.argument('resource_name')
def add(resource_name):
    framework = 'ghost'
    project_name = os.getcwd().split(os.sep)[-1]
    plural = get_plural_for_word(resource_name)
    resource_params = ResourceParams(
        framework,
        project_name,
        resource_name,
        plural
    )
    add_resource(resource_params)
    click.echo('resource added ' + resource_name)

@click.command()
@click.argument('project_name')
def init(project_name):
    framework = 'ghost'
    click.echo('please be sure you have the rights to create files in current dir!')
    init_project(framework, project_name)
    click.echo(framework + ' project created: ' + project_name)
    if framework == 'ghost':
        os.system('cd {} && go mod init {} && go mod tidy'.format(project_name, project_name))
        info = """
            the last 2 steps you should do: 
              1. config & manage mysql database
              2. go build and run
              then enjoy it !
        """
        click.echo(info)
    else:
        os.system('cd {} && pipreqs --force ./ && pip install'.format(project_name))

cli.add_command(add) #增加资源
cli.add_command(init) #初始化新项目