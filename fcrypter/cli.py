# -*- coding: utf-8 -*-

import click
from fcrypter import get_supported_ciphers


supported_ciphers = get_supported_ciphers()
cipher_names = [y.name for y in supported_ciphers]


@click.command()
@click.option("--cipher", type=click.Choice(cipher_names),
              help="Cipher mode used for encryption")
@click.option("--mode", type=click.Choice(["encrypt", "e", "decrypt", "d"]))
@click.option("--file-in", prompt=True)
@click.option("--file-out", prompt=True)
def main(cipher, mode, file_in, file_out):
    """Console script for fcrypter"""
    click.echo("Replace this message by putting your code into "
               "fcrypter.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()
