# radb-tools

Tools for IP-ASN-Country mapping.

- ip-country script generates ip-<country code>.lst file which consists all IPv4 prefixes announced from given country ASNs.

## Installation

```bash
git clone --depth==1 git@github.com:furriest/radb-tools.git
cd ./radb-tools
pip install -r requirements.txt
```

## Usage

```bash
renew-db
python3 ip-country.py RU
````

## License
[MIT](https://choosealicense.com/licenses/mit/)
