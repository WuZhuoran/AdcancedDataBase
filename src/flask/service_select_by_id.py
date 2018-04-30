import pymysql.cursors
import warnings
import simplejson

warnings.filterwarnings("ignore")

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='test',
                             cursorclass=pymysql.cursors.DictCursor)


def select_by_id(id):

    with connection.cursor() as cursor:
        sql = """SELECT * FROM business WHERE ID = %s""" % id
        number = cursor.execute(sql)
        for i in range(number):
            result = cursor.fetchone()
            res = dict()
            res['ID'] = result['ID']
            res['business_id'] = result['business_id']
            res['latitude'] = result['latitude']
            res['longitude'] = result['longitude']
            res['categories'] = result['categories']
            return res


if __name__ == '__main__':
    select_by_id(1)
