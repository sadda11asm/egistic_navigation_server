import shapely.wkt as shwkt
# from egistic_navigation.field_geometry.field_utils import FieldPoly
import matplotlib.pyplot as plt

def get_equally_separated_points(wkt, epsg):
    poly = shwkt.loads('POLYGON((10.689 -25.092, 34.595 -20.170, 38.814 -35.639, 13.502 -39.155, 10.689 -25.092))')
    print(type(poly))
    # field_poly = FieldPoly.as_valid(poly)
    # field_poly.plot()
    # plt.show()
    return "success"

get_equally_separated_points("safds", "sdf")
