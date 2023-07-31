# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class RatingTransformer:
    def rating_transformer(self,field):
        #perform the field transformation here:
        # 'Rating + 4.9' ==> "4.9"
        
        try:
            transformed_field = field.split(' ')[-1]
            return transformed_field
        except:
            pass
class NumberRatingTransformer:
    def number_rating_transformer(self,field):
        
        # '(60)' ==> '60'
        
        try:
            #perform the field transformation here:
            transformed_field=int(field.strip('()'))
            return transformed_field
        except:
            pass

class ShipTrasnformer:
    def ship_transformer(self,field):
        if field == 'Free Shipping':
            transformed_field=0
        else:
            transformed_field=field
        return transformed_field

class NeweggPipeline:
    def __init__(self):
        #create the instance of class RatingTransformer, assign to the rating_transformer object
        self.rating_transformer = RatingTransformer()

        #create the instance of class NumberRatingTransformer, assign to the number_rating_transformer object
        self.number_rating_transformer = NumberRatingTransformer()

        self.ship_transfomer = ShipTrasnformer()
        self.items=[]

    def open_spider(self,spider):
        pass

    def close_spider(self,spider):
        df = pd.DataFrame(self.items)
        df.to_csv('data.csv', index=False)

    def process_item(self, item, spider):
        #access the rating_transformer object, call the rating_transformer method to the item's field
        rating_transformed = self.rating_transformer.rating_transformer(item['rating'])

        # access the number_rating_transformer object, call the number_rating_transformer method to the item's field
        number_rating_transformed = self.number_rating_transformer.number_rating_transformer(item['number_rating'])

        #access the ship_transfomer object, call the ship_transformer method to the item's field
        ship_transformed = self.ship_transfomer.ship_transformer(item['ship'])

        transformed_item = {
            'itemID': item['itemID'],
            'title': item['title'],
            'brand': item['brand'],
            'rating': rating_transformed,
            'number_rating': number_rating_transformed,
            'price' : item['price'],
            'ship': ship_transformed,
            'image_url': item['image_url'],
            'product_des': item['product_des']
        }
        self.items.append(dict(transformed_item))
        return transformed_item