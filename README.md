# simple-crawler
![version](https://img.shields.io/badge/version-1.0.0-blue)

This is a simple web crawler script that can be used to crawl a website and all pages linked to it. It retrieves all the links from a web page and follows those links to crawl additional pages. The crawler has a maximum depth limit to control how far it should follow the links.

## Disclaimer:

This crawler tool has been developed for educational purposes and to assist in personal challenges. It is important to note that I am not responsible for any malicious actions taken with this tool. The intention behind creating this tool is to learn and explore web crawling techniques, not to encourage or support any illegal or unethical activities.

It is crucial to use this tool responsibly and in accordance with applicable laws and regulations. Any misuse or unauthorized access to websites or sensitive information is strictly prohibited. Always obtain proper authorization before conducting any scanning or crawling activities on a website.

I strongly advise against using this tool for any malicious or harmful purposes. It is your responsibility to use this tool ethically and respect the privacy and security of others. By using this tool, you agree to take full responsibility for your actions and any consequences that may arise from them.

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
python3 crawler.py url [-h] [-m MAX_DEPTH] [-o OUTPUT] [--headers]
```

## Example
```bash
python3 crawler.py https://www.example.com -m 2 -o results.txt --headers "Authorization: Bearer token" "Content-Type: application/json"
```

## License
[MIT](https://choosealicense.com/licenses/mit/)