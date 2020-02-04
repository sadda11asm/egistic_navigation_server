from .worker_conf import app
import shapely.wkt as shwkt
from lgblkb_navigation.field_geometry.field_utils import FieldPoly
# from lgblkb_navigation.global_support import simple_logger
import json
from functools import partial
import pyproj
from shapely.ops import transform
import geopandas
from shapely.geometry import MultiPoint


# logger = simple_logger
@app.task(bind=True, name='get_equally_separated_points')
def get_equally_separated_points(self, wkt, parcel_area, epsg):
    # logger.info("WKT: %s", wkt)
    # project = partial(
    #     pyproj.transform,
    #     pyproj.Proj(init='epsg:4326'),  # source coordinate system
    #     pyproj.Proj(init='epsg:3857'))  # destination coordinate system
    poly_init = shwkt.loads(wkt)
    # poly = transform(project, poly_init)
    s = geopandas.GeoSeries(poly_init)
    s.crs = {'init':'epsg:{epsg}'.format(epsg=epsg), 'no_defs': True}
    s.to_crs(epsg=3857)
    print(s)
    field_poly = FieldPoly.as_valid(s[0])
    centers = field_poly.get_subparcel_centers(parcel_area=parcel_area).tolist()
    centers_final = []
    for center in centers:
        original = pyproj.Proj(init='EPSG:3857')
        destination = pyproj.Proj(init='EPSG:{epsg}'.format(epsg=epsg))
        x,y = pyproj.transform(original, destination, center[0], center[1])
        centers_final.append([x, y])

    multipoint = MultiPoint(centers_final)
    json_dump = json.dumps({'multipoint': multipoint.wkt})
    return json_dump


