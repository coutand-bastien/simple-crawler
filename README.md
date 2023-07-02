# simple-crawler
![version](https://img.shields.io/badge/version-1.0.0-blue)

This is a simple web crawler script that can be used to crawl a website and all pages linked to it. It retrieves all the links from a web page and follows those links to crawl additional pages. The crawler has a maximum depth limit to control how far it should follow the links.

## Dependencies
The crawler script requires the following dependencies:
* [Python 3](https://www.python.org/downloads/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [requests](https://requests.readthedocs.io/en/master/)
* [argparse](https://docs.python.org/3/library/argparse.html)
* [pyfiglet](https://pypi.org/project/pyfiglet/)
* [urllib](https://docs.python.org/3/library/urllib.html)

## Installation
To install the dependencies, run the following command:
```bash
pip3 install -r requirements.txt
```

## Usage
To use the crawler, you need to provide a URL to crawl. Optionally, you can specify the maximum depth to crawl and the output file to save the results.

```bash
python3 crawler.py url [-h] [-m MAX_DEPTH] [-o OUTPUT]
```

## Example
```bash
python3 crawler.py https://www.example.com -m 2 -o results.txt
```

## License
[MIT](https://choosealicense.com/licenses/mit/)