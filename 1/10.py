import math

latitude_beijing = 39.9075000
longitude_beijing = 116.3972300
latitude_kyiv = 50.4546600
longitude_kyiv = 30.5238000

x1 = math.radians(latitude_beijing)
y1 = math.radians(longitude_beijing)
x2 = math.radians(latitude_kyiv)
y2 = math.radians(longitude_kyiv)

distance = 6371.032 * math.acos(math.sin(x1) * math.sin(x2) +
                                 math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

print(f"{'Distance (km):':>15} {distance:>10.3f}")
