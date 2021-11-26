import pymysql
import json
import logging


class MysqlPipeline(object):

    def open_spider(self, spider):
        # connection database
        self.connect = pymysql.connect(host='120.78.150.105', user='root', passwd='Root.123456', db='test')
        # get cursor
        self.cursor = self.connect.cursor()
        # 数据统计
        self.count = 0
        # 日志打印
        self.logger = logging.getLogger(None)

    def process_item(self, item, spider):
        if item['name'] and item['code']:
            # sql语句
            select_sql = """select * from item where code = %s"""
            insert_sql = """insert into item(code, shop, name, price, image, comments) VALUES (%s,%s,%s,%s,%s,%s)"""
            # 执行插入数据到数据库操作
            rows = self.cursor.execute(select_sql, (item['code']))
            if rows == 0:
                self.cursor.execute(insert_sql, (
                item['code'], item['shop'], item['name'], item['price'], item['image'], item['comments']))
                # 提交，不进行提交无法保存到数据库
                self.connect.commit()
                data = json.dumps(dict(item), ensure_ascii=False)
                self.logger.info(f'本次获取数据:{data}')
                self.logger.info(f'共获取数据{self.count}条')
                self.count = self.count + 1
            else:
                self.logger.info(f'{item["code"]}:数据已存在！')
        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.connect.close()
