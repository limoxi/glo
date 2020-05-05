# coding: utf8

import os
import sys

import click

from glo.core.resource_params import ResourceParams
from cli_func import init_project, add_resource

reload(sys)
sys.setdefaultencoding('utf-8')

@click.group()
def cli():
    pass

@click.command()
@click.option('--args', prompt='framework.project.resource:', help='ghost.test.fish')
@click.option('--plural', prompt='resource plural:', help='资源的复数形式')
def add(args, plural):
    sps = args.split('.')
    framework = sps[0]
    project_name = sps[1]
    resource_name = sps[2]
    resource_params = ResourceParams(
        framework,
        project_name,
        resource_name,
        plural
    )
    add_resource(resource_params)
    click.echo('resource added ' + resource_name)

@click.command()
@click.option('--args', prompt='framework.project_name:', help='ghost.test')
def init(args):
    sps = args.split('.')
    framework = sps[0]
    project_name = sps[1]
    if framework not in ('rust', 'ghost') or framework == 'rust':
        click.echo("not support right now")
        return
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