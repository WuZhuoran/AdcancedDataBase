import pymysql.cursors
import warnings

warnings.filterwarnings("ignore")


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='test',
                             cursorclass=pymysql.cursors.DictCursor)


def select_by_lat_lon(latitude, longitude, radius):

    with connection.cursor() as cursor:
        sql = """SELECT *,(6371 * 2 * ASIN(SQRT(POWER(SIN(('%s' - abs(latitude)) * pi()/180 / 2),2) + COS('%s' * pi()/180 ) * COS(abs(latitude) *pi()/180) * POWER(SIN(('%s' - longitude) *pi()/180 / 2), 2) ))) AS distance FROM business HAVING distance < '%s' ORDER BY distance LIMIT 5;""" % (
            latitude, latitude, longitude, radius)
        number = cursor.execute(sql)
        res = dict()
        res['number'] = number
        res['detail'] = []
        for i in range(number):
            result = cursor.fetchone()
            single = dict()
            single['ID'] = result['ID']
            single['business_id'] = result['business_id']
            single['name'] = result['name']
            single['latitude'] = result['latitude']
            single['longitude'] = result['longitude']
            single['categories'] = result['categories']
            res['detail'].append(single)

        return res


if __name__ == '__main__':
    select_by_lat_lon(33.3306902, -111.9785992, 0.4)

