SET @lat = 33.3;
SET @lon =-111.9;
SET @rad = 0.5;

SELECT
    *,
    (6371 * 2 * ASIN(SQRT(
            POWER(SIN((@lat - abs(latitude)) * pi()/180 / 2),
            2) + COS(@lat * pi()/180 ) * COS(abs(latitude) *
            pi()/180) * POWER(SIN((@lon - longitude) *
            pi()/180 / 2), 2) ))) AS distance
FROM
    business
HAVING distance < @rad
LIMIT 5;