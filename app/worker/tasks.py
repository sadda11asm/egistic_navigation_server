from .worker_conf import app
import shapely.wkt as shwkt
from lgblkb_navigation.field_geometry.field_utils import FieldPoly
# from lgblkb_navigation.global_support import simple_logger
import json

# logger = simple_logger
@app.task(bind=True, name='get_equally_separated_points')
def get_equally_separated_points(self, wkt, parcel_area, epsg):
    # logger.info("WKT: %s", wkt)
    poly = shwkt.loads(wkt)
    field_poly = FieldPoly.as_valid(poly)
    centers = field_poly.get_subparcel_centers(parcel_area=parcel_area).tolist()

    json_dump = json.dumps({'centers': centers})
    return json_dump


