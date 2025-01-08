#!/usr/bin/env python3

import json
import pathlib

import requests

DEFAUL_CONFIG_URL="https://raw.githubusercontent.com/DelilahEve/DinoDepot-RemoteConfig/main/passive-production-v2.json"

def main():
    response = requests.get(DEFAUL_CONFIG_URL)
    response.raise_for_status()
    passive_production = response.json()
    gryphons = json.loads(pathlib.Path("gryphons.json").read_text())
    passive_production["production"] += gryphons["production"]
    pathlib.Path("extended.json").write_text(json.dumps(passive_production, indent=2))


if __name__ == '__main__':
    main()
