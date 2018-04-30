import pymysql.cursors
import warnings

warnings.filterwarnings("ignore")


def select_by_lat_lon(business_id):

    with connection.cursor() as cursor:
        sql = """SELECT * FROM business WHERE `business_id` = '%s'""" % business_id
        number = cursor.execute(sql)
        for i in range(number):
            result = cursor.fetchone()
            print(result)


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='test',
                             cursorclass=pymysql.cursors.DictCursor)

if __name__ == '__main__':
    select_by_lat_lon('cF6riu75lFaHzKG4fK437w')

