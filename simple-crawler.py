import argparse
import pyfiglet

from utils.Crawler import Crawler

if __name__ == "__main__":
    print(pyfiglet.figlet_format("Simple-crawler", font="slant"))

    parser = argparse.ArgumentParser(description="Crawl a website and all pages linked to it")
    parser.add_argument("url", help="URL to crawl")
    parser.add_argument("-m", "--max-depth", type=int, default=3, help="Maximum depth to crawl")
    parser.add_argument("-o", "--output", type=str, default="output.txt", help="Output file to save results")
    parser.add_argument("--headers", nargs='*', metavar='HEADER', default=None, help="Add headers")
    args = parser.parse_args()

    headers = {}
    if args.headers:
        for header in args.headers:
            key, value = header.split(':')
            headers[key.strip()] = value.strip()

    crawler = Crawler(base_url=args.url, max_depth=args.max_depth, output=args.output, headers=headers)
    crawler.process()