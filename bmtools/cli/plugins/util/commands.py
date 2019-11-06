import click
import logging
import os

from clint.textui import puts, colored, indent

@click.group('util')
@click.option('-c', '--config', type=click.Path(), default='./simulation_config.json', help='Configuration file to use, default: "simulation_config.json"')
@click.pass_context
def cli(ctx, config):
    config_path = os.path.abspath(os.path.expanduser(config)).replace("\\","/")

    ctx.obj["config"] = config_path

    if not os.path.exists(config_path):
        click.echo(colored.red("Config file not found: " + config))



if __name__ == "__main__":
    cli()