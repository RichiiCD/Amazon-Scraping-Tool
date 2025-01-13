from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from amazonscraping.settings import MEDIA_ROOT
from .spiders.product import ProductSpider


def run_spider(search, file_name, file_format):
    """
    Runs a Scrapy spider to scrape product data based on a search query and saves the output to a specified file.

    Args:
        search: String representing the search query for the spider to use.
        file_name: String representing the name of the output file where scraped data will be saved.
        file_format: String specifying the file format for the output (e.g., "json", "csv").

    Returns:
        None: The function starts and runs the spider, saving its output to the specified file.
    """
    settings = get_project_settings()

    file_location = MEDIA_ROOT + "/scraping/" + file_name

    settings["FEEDS"] = {
        file_location: {"format": file_format},
    }

    process = CrawlerProcess(settings)
    process.crawl(ProductSpider, search=search)
    process.start()
