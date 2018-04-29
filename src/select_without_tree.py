import pymysql.cursors
import warnings

warnings.filterwarnings("ignore")


def select_without_tree(latitude, longitude, radius):

    with connection.cursor() as cursor:
        sql = """SELECT *,(6371 * 2 * ASIN(SQRT(POWER(SIN(('%s' - abs(latitude)) * pi()/180 / 2),2) + COS('%s' * pi()/180 ) * COS(abs(latitude) *pi()/180) * POWER(SIN(('%s' - longitude) *pi()/180 / 2), 2) ))) AS distance FROM business HAVING distance < '%s' ORDER BY distance LIMIT 5;""" % (
            latitude, latitude, longitude, radius)
        number = cursor.execute(sql)
        for i in range(number):
            result = cursor.fetchone()
            print(result)


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='test',
                             cursorclass=pymysql.cursors.DictCursor)


select_without_tree(33.3306902, -111.9785992, 0.4)
