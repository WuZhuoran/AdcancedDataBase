import pymysql.cursors
import warnings
import googlemaps

warnings.filterwarnings("ignore")

gmaps = googlemaps.Client(key='AIzaSyAPIvyw4rfushMMOVuVHLwCtct-eIIbc9o')

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='test',
                             cursorclass=pymysql.cursors.DictCursor)


def select_by_lat_lon_location(latitude, longitude, radius, star):

    with connection.cursor() as cursor:
        sql = """SELECT *,(6371 * 2 * ASIN(SQRT(POWER(SIN(('%s' - abs(latitude)) * pi()/180 / 2),2) + COS('%s' * pi()/180 ) * COS(abs(latitude) *pi()/180) * POWER(SIN(('%s' - longitude) *pi()/180 / 2), 2) ))) AS distance FROM business WHERE stars = '%s' HAVING distance < '%s' ORDER BY distance LIMIT 20;""" % (
            latitude, latitude, longitude, star, radius)
        number = cursor.execute(sql)
        res = dict()
        res['number'] = number
        res['location'] = dict()
        res['location']['latitide'] = latitude
        res['location']['longitude'] = longitude
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
            single['stars'] = result['stars']
            res['detail'].append(single)
        print(res)
        return res


def select_by_location(location, rad, star):
    geocode_result = gmaps.geocode(location)
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']
    return select_by_lat_lon_location(lat, lng, rad, star)


if __name__ == '__main__':
    # select_by_lat_lon_location(33.3306902, -111.9785992, 0.4, 4)
    select_by_location("Chicago", 500, 5)

