import sys
import click

@click.command()
@click.option('--words', default='Hello')
@click.argument('name')
def greet(name, words):
    click.echo(f'{words}, {name}!')


if __name__ == '__main__':
    greet()
    # args = sys.argv
    # for arg in args:
    #     print(arg)
