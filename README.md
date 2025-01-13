# Amazon Scraping Tool

A Python-based web scraping tool built with **Django** and **Scrapy** to search and download Amazon product listings. This tool allows users to search for products on Amazon and scrape details like product name, price, rating, and more. The scraped data can then be downloaded in various formats (CSV, JSON, XML).

![image](https://github.com/user-attachments/assets/fd228a74-436a-413b-989e-d8cab56b0cae)

## Features
- **Search Products**: Search for Amazon products by keywords.
- **Scrape Product Data**: Collect product name, price, rating, and other relevant information.
- **Download Data**: Export scraped data in **CSV**, **JSON**, or **XML** formats.
- **Built with Django & Scrapy**: Utilizes Django for the web interface and Scrapy for efficient web scraping.

## Requirements
- Python 3.11+
- Django 4.2
- Scrapy 2.12
- Other dependencies in `requirements.txt`

## Installation
1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/amazon-scraping-tool.git
   cd amazon-scraping-tool

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt

4. **Run Django Server**:

   ```bash
   python manage.py runserver
