from .utils import convert_
import click


@click.group()
def cli():
    """
    Simple CLI for working with your CNN's dataset 🔥
    """
    pass


@cli.command()
@click.option('--type', '-t', 'type', help='output images extension', type=click.Choice(['jpg', 'png']), default='jpg', show_default=True)
@click.option('--target-size', '-s', 'size', help='output images size', default=128, show_default=True)
@click.argument('root_dir')
def convert(type, size, root_dir):
    """
    Converting images to specific size and format
    """
    convert_(type, size, root_dir)


@cli.command()
@click.option('--probability', '-p', 'probability', help='default probability for operations', default=0.5, show_default=True)
@click.option('--max-left-rotation', '-mlr', 'left_r', help='maximum left rotation (in degrees)', default=10, show_default=True)
@click.option('--max-right-rotation', '-mrr', 'right_r', help='maximum right rotation (in degrees)', default=10, show_default=True)
@click.option('--magnitude', '-mg', 'magnitude', help='magnitude value for distortion operation', default=8, show_default=True)
@click.option('--grid-width-height', '-gwh', 'grid', help='grid dimensions for distortion operation', default=8, show_default=True)
@click.option('--min-factor', '-minf', 'min_factor', help='min factor for scaling', default=1, show_default=True)
@click.option('--max-factor', '-maxf', 'max_factor', help='min factor for scaling', default=1.5, show_default=True)
@click.option('--num', '-n', 'num', help='number of output images after augmentation', default=500, show_default=True)

@click.option('--flip/--no-flip', default=True)
@click.option('--rotate/--no-rotate', default=True)
@click.option('--distortion/--no-distortion', default=True)
@click.option('--skew/--no-skew', default=True)
@click.option('--zoom/--no-zoom', default=True)

@click.argument('root_dir')
def augment(prob, num, flip, root_dir):
    """
    Dataset augmentation
    """
    pass
