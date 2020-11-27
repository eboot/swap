#!/usr/bin/env python3

from swap import __version__


def bitcoin(blockcypher_token=None) -> dict:
    if blockcypher_token is None:
        blockcypher_token = "c6ef693d3c024088810e6fac2a1494ee"
    return {
        "mainnet": {
            "blockchain": "https://blockchain.info",
            "smartbit": "https://api.smartbit.com.au/v1/blockchain",
            "blockcypher": {
                "url": "https://api.blockcypher.com/v1/btc/main",
                "token": blockcypher_token
            }
        },
        "testnet": {
            "blockchain": "https://testnet.blockchain.info",
            "smartbit": "https://testnet-api.smartbit.com.au/v1/blockchain",
            "blockcypher": {
                "url": "https://api.blockcypher.com/v1/btc/test3",
                "token": blockcypher_token
            }
        },
        "path": "m/44'/0'/0'/0/0",
        "BIP44": "m/44'/0'/{account}'/{change}/{address}",
        "symbol": "SATOSHI",
        "timeout": 60,
        "locktime": 0,
        "version": 2,
        "network": "mainnet",
        "sequence": 1000,
        "headers": {
            "User-Agent": f"Swap User-Agent {__version__}",
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json"
        }
    }


def bytom() -> dict:
    return {
        "mainnet": {
            "bytom-core": "http://localhost:9888",
            "blockmeta": "https://blockmeta.com/api/v3",
            "blockcenter": "https://bcapi.bystack.com/bytom/v3",
            "mov": "https://ex.movapi.com/bytom/v3"
        },
        "solonet": {
            "bytom-core": "http://localhost:9888",
            "blockmeta": None,
            "blockcenter": None,
            "mov": None
        },
        "testnet": {
            "bytom-code": "http://localhost:9888",
            "blockmeta": None,
            "blockcenter": None,
            "mov": None
        },
        "path": "m/44'/153/1/0/1",
        "BIP44": "m/44/153/{account}/{change}/{address}",
        "indexes": ["2c000000", "99000000", "01000000", "00000000", "01000000"],
        "symbol": "NEU",
        "timeout": 60,
        "asset": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
        "fee": 10_000_000,
        "confirmations": 1,
        "network": "mainnet",
        "forbid_chain_tx": False,
        "sequence": 1000,
        "headers": {
            "User-Agent": f"Swap User-Agent {__version__}",
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json"
        }
    }


def vapor() -> dict:
    return {
        "mainnet": {
            "vapor-core": "http://localhost:9889",
            "blockmeta": "https://vapor.blockmeta.com/api/v1",
            "blockcenter": "https://ex.movapi.com/vapor/v3",
            "mov": "https://ex.movapi.com/bytom/v3"
        },
        "solonet": {
            "vapor-core": "http://localhost:9889",
            "blockmeta": None,
            "blockcenter": None,
            "mov": None
        },
        "testnet": {
            "vapor-core ": "http://localhost:9889",
            "blockmeta": None,
            "blockcenter": None,
            "mov": None
        },
        "path": "m/44'/153/1/0/1",
        "BIP44": "m/44/153/{account}/{change}/{address}",
        "indexes": ["2c000000", "99000000", "01000000", "00000000", "01000000"],
        "symbol": "NEU",
        "timeout": 60,
        "asset": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
        "fee": 10_000_000,
        "confirmations": 1,
        "network": "mainnet",
        "forbid_chain_tx": False,
        "sequence": 1000,
        "headers": {
            "User-Agent": f"Swap User-Agent {__version__}",
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json"
        }
    }
