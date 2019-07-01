import click
from python_terraform import *

t = Terraform()

class Config(object):

    def __init__(self):
        self.region = 'empty'


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--region', type=str, envvar='AWS_DEFAULT_REGION',
                required=True,
                help='Set the region that terraform will create your infrastructure.'
                )
@pass_config
def cli(config, region):
    """ PyForm

    This script creates infrastructure with terraform
    """
    config.region = region


"""
  plan
"""


@cli.command ()
@click.option ( '--service', type=str, required=True,
                help="Service that you want to create the resource."
                )
@click.argument ('resource', nargs=-1, type=str,required=False)
@pass_config
def plan (config, service, resource):
    """ Shows a preview of terraform commands.
    List of resources that you want to create.
    """
    for x in resource:
        terraform_plan(x,'%s' %service,'%s' % config.region)


def terraform_plan(resource, service, region):
    print(resource, service, region, string.encode("ascii", "replace"))

if __name__ == '__main__':
    cli ()
