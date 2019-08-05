import requests
import click

@click.command()
@click.argument('url')
@click.argument('filename', type=click.Path())

def d_file(url, filename):
    print('Downloading form {} to {}'.format(url, filename))
    rsp = requests.get(url)
    
    with open(filename, 'wb') as ofile:
        ofile.write(rsp.content)

if __name__ == '__main__':
    d_file()

