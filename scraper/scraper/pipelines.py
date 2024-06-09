# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pyodbc
import csv
from .spiders.sohoavnexpress import SohoaVnexpressNet

class ScraperPipeline:

    def __init__(self):
        server = 'BANHBAOTHAPCAM\SQL2019'
        database = 'TEST'
        username = 'Qcuong103'
        password = '10032000'
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()
        print('Conected')

    def process_item(self, item, spider):
        print('Inserting a new row into table')
        # Insert Query
        tsql = "INSERT INTO table_3 (title, description, content, author, publish_date) VALUES (?,?,?,?,?);"
        # with self.cursor.execute(tsql, 'Tạp chí có chữ ký Steve Jobs được bán giá 50.000 USD',
        #                     'Cuốn tạp chí phát hành năm 1988 khi Jobs chuẩn bị ra mắt máy tính NeXT đầu tiên được bán với giá gấp 50 lần con số khởi điểm.',
        #                     ' <p class="Normal">', 'Tuấn Hưng', 'Chủ nhật, 29/10/2017, 21:44 (GMT+7)'):
        with self.cursor.execute(tsql,(item['title'], item['description'], item['content'], item['author'], item['publish_date'])):
            print('Successfully Inserted!')
        # self.cursor.execute(tsql, item)

        return item

    def close_spider(self, spider):
        print("ScraperPipeline 45")
        SohoaVnexpressNet.file.close()
        print("ScraperPipeline 47")

    # def open_spider(self, spider):
    #     self.file = open("output.csv", "w", newline="")
    #     print("ScraperPipeline 38")
    #     self.writer = csv.DictWriter(self.file, fieldnames=["title", "description", "content", "author", "publish_date"])
    #     print("ScraperPipeline 40")
    #     self.writer.writeheader()
    #     print("ScraperPipeline 42")
    #
    # def close_spider(self, spider):
    #     print("ScraperPipeline 45")
    #     self.file.close()
    #     print("ScraperPipeline 47")
    #
    # def process_item(self, item, spider):
    #     print("ScraperPipeline 50")
    #     self.writer.writerow(item)
    #     print("ScraperPipeline 52")
    #     return item