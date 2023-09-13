# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import _sqlite3

class QuotetutorialPipeline:
    def __init__(self) -> None:
        self.create_connection()
        self.create_table()
    
    
    def create_connection(self):
        path = os.path.dirname(__file__)
        path_out = os.path.join(path,"mysqlite3.db")

        self.conn = _sqlite3.connect(path_out)
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute("""drop table if exists quotes_tb""")
        self.curr.execute("""create table quotes_tb(
                        title text,
                        author tex,
                        tag text
                        )""")
    
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self, item):
        self.curr.execute("""insert into quotes_tb values(?,?,?)""",(
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.conn.commit()
