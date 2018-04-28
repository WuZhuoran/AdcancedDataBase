import re

import pandas as pd
import pymysql.cursors

BUSSINESS_FILE = 'yelp_business.csv'
business = pd.read_csv("../../data/" + BUSSINESS_FILE)


def insert_row(row):
    """
    Given a business row, insert into mysql database business table.
    :param row: A business row instance
    :return:
    """
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `business` (`business_id`, " \
              "`name`, " \
              "`neighborhood`, " \
              "`address`, " \
              "`city`, " \
              "`state`," \
              "`postal_code`," \
              "`latitude`," \
              "`longitude`," \
              "`stars`," \
              "`review_count`," \
              "`is_open`," \
              "`categories`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (str(row['business_id']),
                             re.sub(r'[^\x00-\x7f]', r'', str(row['name'])),
                             re.sub(r'[^\x00-\x7f]', r'', str(row['neighborhood'])),
                             re.sub(r'[^\x00-\x7f]', r'', str(row['address'])),
                             re.sub(r'[^\x00-\x7f]', r'', str(row['city'])),
                             re.sub(r'[^\x00-\x7f]', r'', str(row['state'])),
                             re.sub(r'[^\x00-\x7f]', r'', str(row['postal_code'])),
                             str(row['latitude']),
                             str(row['longitude']),
                             int(row['stars']),
                             int(row['review_count']),
                             int(row['is_open']),
                             str(row['categories'])))

    connection.commit()


def create_database(connection):
    """
    Create database table.
    :return:
    """
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS test;"
        cursor.execute(sql)

    connection.commit()


def create_table(connection):
    with connection.cursor() as cursor:
        sql = "CREATE TABLE IF NOT EXISTS `test`.`business` (" \
              "`ID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT," \
              "`business_id` VARCHAR(45) NOT NULL," \
              "`name` VARCHAR(200) NOT NULL," \
              "`neighborhood` VARCHAR(45) NULL," \
              "`address` VARCHAR(200) NULL," \
              "`city` VARCHAR(45) NULL," \
              "`state` VARCHAR(45) NULL," \
              "`postal_code` VARCHAR(6) NULL," \
              "`latitude` VARCHAR(45) NOT NULL," \
              "`longitude` VARCHAR(45) NOT NULL," \
              "`stars` DECIMAL NULL," \
              " `review_count` INT NULL," \
              "`is_open` INT NULL," \
              "`categories` VARCHAR(255) NULL," \
              "PRIMARY KEY (`ID`));"
        cursor.execute(sql)

    connection.commit()


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='test',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    create_database(connection)
    create_table(connection)

    for index, row in business.iterrows():
        insert_row(row)

except:
    print('Error with MySQL.')
    print(row)

finally:
    connection.close()
