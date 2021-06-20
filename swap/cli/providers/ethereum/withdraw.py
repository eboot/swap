#!/usr/bin/env python
# coding=utf-8

import sys

from ....cli import click
from ....providers.ethereum.transaction import WithdrawTransaction
from ....providers.config import ethereum as config


@click.command("withdraw", options_metavar="[OPTIONS]",
               short_help="Select Ethereum Withdraw transaction builder.")
@click.option("-th", "--transaction-hash", type=str, required=True, help="Set Ethereum funded transaction hash/id.")
@click.option("-a", "--address", type=str, required=True, help="Set Ethereum recipient address.")
@click.option("-sk", "--secret-key", type=str, required=True, help="Set secret password/passphrase.")
@click.option("-hth", "--htlc-transaction-hash", type=str, default=None,
              help="Set Ethereum HTLC transaction hash.  [default: None]")
@click.option("-n", "--network", type=str, default=config["network"],
              help="Set Ethereum network.", show_default=True)
def withdraw(transaction_hash: str, address: str, secret_key: str, htlc_transaction_hash: str,  network: str):
    try:
        click.echo(
            WithdrawTransaction(
                network=network
            ).build_transaction(
                address=address,
                transaction_hash=transaction_hash,
                secret_key=secret_key,
                htlc_transaction_hash=htlc_transaction_hash
            ).transaction_raw()
        )
    except Exception as exception:
        click.echo(click.style("Error: {}")
                   .format(str(exception)), err=True)
        sys.exit()
