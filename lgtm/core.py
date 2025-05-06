import click
from lgtm.image_source import get_image
from lgtm.drawer import save_with_message

@click.command()
@click.option('--message', '-m', default='LGTM', show_default=True, help='画像に載せる文字列')
@click.argument('keyword')
def cli(keyword, message):
    """LGTM画像生成ツール"""
    lgtm(keyword, message)

def lgtm(keyword, message):
    with get_image(keyword) as fp:
        save_with_message(fp, message)
