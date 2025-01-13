from itemadapter import ItemAdapter


class AmazonscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        price = adapter.get('price')
        if price:
            adapter['price'] = price.replace('$', '')

        stars = adapter.get('stars')
        if stars:
            adapter['stars'] = stars.split(' ')[0]

        return item
    