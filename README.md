# radb-tools

Tools for IP-ASN-Country mapping.

- The ip-country script generates an ip-\<country code\>.lst file which contains all the IPv4 prefixes announced by the country's ASNs.
  
## Installation

```bash
git clone --depth=1 git@github.com:furriest/radb-tools.git
cd ./radb-tools
pip install -r requirements.txt
```

## Usage

```bash
./renew-db
python3 ./ip-country.py RU
````

## License
[MIT](https://choosealicense.com/licenses/mit/)
