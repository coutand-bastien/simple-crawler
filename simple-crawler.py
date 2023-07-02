import argparse
import pyfiglet

from .utils.Crawler import Crawler

if __name__ == "__main__":
    print(pyfiglet.figlet_format("Simple-crawler", font="slant"))

    parser = argparse.ArgumentParser(description="Crawl a website and all pages linked to it")
    parser.add_argument("url", help="URL to crawl")
    parser.add_argument("-m", "--max-depth", type=int, default=3, help="Maximum depth to crawl")
    parser.add_argument("-o", "--output", type=str, default="output.txt", help="Output file to save results")
    args = parser.parse_args()

    crawler = Crawler(args.url)
    crawler.crawl(base_url=args.url, max_depth=args.max_depth, output=args.output)