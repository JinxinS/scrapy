# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
reload(sys)   
sys.setdefaultencoding('utf8')

from sqlalchemy.orm import sessionmaker
from models import  Movie, db_connect, create_movie_table 
class WebspiderPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_movie_table(engine) 
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        movie = Movie(**item)
#        print movie.name,movie.link
        try:
            session.merge(movie)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
#        return item
