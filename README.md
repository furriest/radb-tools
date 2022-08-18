# radb-tools

Tools for IP-ASN-Country mapping.

- The ip-country script generates an ip-\<country code\>.lst file which contains all the IPv4 prefixes announced by the country's ASNs.
- The asn-country script generates an asn-\<country code\>.lst file which contains all the autonomous system numbers by the country.
  
## Installation

```bash
git clone --depth=1 git@github.com:furriest/radb-tools.git
cd ./radb-tools
pip3 install -r requirements.txt
```

## Usage

```bash
./renew-db
python3 ./ip-country.py RU
python3 ./asn-country.py RU
````
or

```bash
python3 ./ip-country-ripe.py RU
````

## License
[MIT](https://choosealicense.com/licenses/mit/)
