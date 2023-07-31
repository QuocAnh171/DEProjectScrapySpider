import scrapy
from newegg.items import NeweggItem

class SkuspiderSpider (scrapy.Spider):
    
    name = "skuspider"
    allowed_domains = ["www.newegg.com"]
    start_urls = ["https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48"]

    for i in range(2,101):
        based_url='https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48/Page-'
        url_p = based_url + str(i)
        start_urls.append(url_p)

    def parse(self, response):

        products_container = response.css('.item-cell')

        for product in products_container:
            #get the item_ID

            itemID = product.css('.item-container::attr(id)').get()
            title = product.css('a.item-title::text').get()
            brand =product.css('.item-branding img::attr(title)').get()
            rating = product.css('.item-rating ::attr(title)').get()
            number_rating = product.css('span.item-rating-num::text').get()
            price = product.css('li.price-current strong::text').get()
            price_decimal = product.css('li.price-current sup::text').get()
            ship = product.css('.price-ship::text').get()
            image_url = product.css('.item-img img::attr(src)').get()

            product_des_list = []
            product_des = product.css('ul.item-features')
            for feature in product_des:
                class_items = feature.css('li::text').getall()
                product_des_list.append(class_items)

            item = NeweggItem()

            item['itemID'] = itemID
            item['title'] = title
            item['brand'] = brand
            item['rating'] = rating
            item['number_rating'] = number_rating
            try:
                item['price'] = float(price.replace(',','') + price_decimal)
            except AttributeError:
                item['price'] = ''
            item['ship'] = ship
            item['image_url'] = image_url
            item['product_des'] = product_des_list

            yield item