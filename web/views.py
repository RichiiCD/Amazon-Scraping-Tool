import json
import random
import string
from multiprocessing import Process
from django.shortcuts import render
from django.http import JsonResponse
from amazonscraper.amazonscraper.spider_runner import run_spider
from amazonscraping.settings import MEDIA_ROOT


def home(request):
    return render(request, 'searcher.html', {})


def send_scraping(request):
    """
    Initiates a scraping process, retrieves the scraped file content, and sends it as a JSON response.

    Returns:
        JsonResponse: A JSON response containing the generated file name and its content.
    """
    search_value = request.GET.get('search')
    file_format = request.GET.get('format')
    
    file_name = generate_file_name(10) + '.' + file_format
    
    process = Process(target=run_spider, args=(search_value, file_name, file_format))
    process.start()
    process.join()

    file_content = get_file_content(file_name)

    if file_format == 'json':
        file_content = json.loads(file_content)

    return JsonResponse({'file_name': file_name, 'file_content': file_content})


def generate_file_name(num_characters):
    """
    Generates a random file name of specified length using uppercase letters and digits.

    Args:
        num_characters: Integer indicating the length of the file name to generate.

    Returns:
        str: A randomly generated file name.
    """
    return str(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num_characters)))


def get_file_content(file_name):
    """
    Reads and returns the content of a file located in the scraping directory.

    Args:
        file_name: String representing the name of the file to read.

    Returns:
        str: The content of the file as a string.
    """
    file_location = MEDIA_ROOT + "/scraping/" + file_name
    with open(file_location, 'r', encoding='utf-8') as file:
        return file.read()
