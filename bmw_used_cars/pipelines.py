# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BmwUsedCarsPipeline:
    def open_spider(self):
        self.conn = sqlite3.connect("bmw_cars.db")
        self.cur = self.conn.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS cars(
            model TEXT,
            name TEXT,
            mileage INTEGER,
            registered TEXT,
            engine TEXT,
            range INTEGER,
            exterior TEXT,
            fuel TEXT,
            transmission TEXT,
            registration TEXT,
            upholstery TEXT
        )
        """)

    def process_item(self, item):
        self.cur.execute("""
        INSERT INTO cars VALUES (?,?,?,?,?,?,?,?,?,?,?)
        """, (
            item["model"],
            item["name"],
            item["mileage"],
            item["registered"],
            item["engine"],
            item["range"],
            item["exterior"],
            item["fuel"],
            item["transmission"],
            item["registration"],
            item["upholstery"],
        ))

        self.conn.commit()
        return item

    def close_spider(self):
        self.conn.close()

