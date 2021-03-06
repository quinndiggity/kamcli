import click
from sqlalchemy import create_engine
from kamcli.ioutils import ioutils_dbres_print
from kamcli.cli import pass_context
from kamcli.cli import parse_user_spec
from kamcli.iorpc import command_ctl


##
#
#
@click.group('dialog', help='Manage dialog module (active calls tracking)')
@pass_context
def cli(ctx):
    pass


##
#
#
@cli.command('showdb', short_help='Show dialog records in database')
@click.option('oformat', '--output-format', '-F',
                type=click.Choice(['raw', 'json', 'table', 'dict']),
                default=None, help='Format the output')
@click.option('ostyle', '--output-style', '-S',
                default=None, help='Style of the output (tabulate table format)')
@pass_context
def dialog_showdb(ctx, oformat, ostyle):
    """Show details for records in dialog table

    \b
    """
    e = create_engine(ctx.gconfig.get('db', 'rwurl'))
    ctx.vlog('Showing all dispatcher records')
    res = e.execute('select * from dialog')
    ioutils_dbres_print(ctx, oformat, ostyle, res)


##
#
#
@cli.command('list', short_help='Show details for dialog records in memory')
@pass_context
def dialog_list(ctx):
    """Show details for dialog records in memory

    \b
    """
    command_ctl(ctx, 'dialog.list', [ ])


