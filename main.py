# Install FastAPI framework
# pip3 install "fastapi[all]"
# https://fastapi.tiangolo.com/tutorial/

# uvicorn main:app --reload

from fastapi import FastAPI, Response, status
from fastapi.staticfiles import StaticFiles

from setup import build_demo_house

app = FastAPI()

# http://localhost:8000/welcome/index.html
app.mount("/welcome", StaticFiles(directory="static"), name="static")


smart_house = build_demo_house()

def create_response(body, error_code):

    if body:
        return body

    return error_code

# http://localhost:8000/
@app.get("/")
async def root():
    return {"message": "Welcome to SmartHouse Cloud REST API - Powered by FastAPI"}


@app.get("/smarthouse")
async def read_smart_house():
    return create_response(smart_house, status.HTTP_404_NOT_FOUND)

@app.get("/smarthouse/floor/")
async def read_smart_house():
    return create_response(smart_house.floors, status.HTTP_404_NOT_FOUND)


@app.get("/smarthouse/floor/{fid}")
async def read_floor(fid: int):

    floor = smart_house.read_floor(fid)

    return create_response(floor, status.HTTP_404_NOT_FOUND)


@app.get("/smarthouse/floor/{fid}/room/")
async def read_rooms(fid: int):

    rooms = smart_house.read_rooms(fid)

    return create_response(rooms, status.HTTP_404_NOT_FOUND)


@app.get("/smarthouse/floor/{fid}/room/{rid}")
async def read_room(fid: int, rid: int):

    room = smart_house.read_room(fid, rid)

    return create_response(room, status.HTTP_404_NOT_FOUND)


@app.get("/smarthouse/device")
async def read_devices():

    devices = smart_house.read_devices()

    return create_response(devices, status.HTTP_404_NOT_FOUND)


@app.get("/smarthouse/device/{did}")
async def read_device(did: int):

    device = smart_house.read_device(did)

    return create_response(device, status.HTTP_404_NOT_FOUND)


@app.get("/smarthouse/device/{did}/state")
async def read_device(did: int):

    device = smart_house.read_device(did)

    if device and device.is_actuator():
        return device.get_current_state()

    return None


@app.get("/smarthouse/device/{did}/measurement")
async def read_device(did: int):

    device = smart_house.read_device(did)

    if device and device.is_sensor():
        return device.get_current_value()

    return None


# @app.put("/route/{rid}")
# async def update_route(rid: int, route: Route, response: Response):
#     updated_route = routes.update_route(rid, route)
#     if updated_route:
#         return updated_route
#     else:
#         response.status_code = status.HTTP_404_NOT_FOUND
#
#     return None
#
#
# @app.post("/route/", status_code=201)
# async def create_route(route: Route):
#     added_route = routes.create_route(route)
#     return added_route
#
#
# @app.delete("/route/{rid}")
# async def delete_route(rid: int, response: Response):
#     route = routes.delete_route(rid)
#     if route:
#         return route
#     else:
#         response.status_code = status.HTTP_404_NOT_FOUND
#
#     return None
#
#
# # GET /route/{rid}/gpspoint - all GPS points in the given route
# @app.get("/route/{rid}/gpspoint")
# async def read_gps_points(rid: int, response: Response):
#     gps_points = routes.read_gpspoints(rid)
#     if gps_points:
#         return gps_points
#     else:
#         response.status_code = status.HTTP_404_NOT_FOUND
#
#     return None
#
#
# # GET /route/{rid}/gpspoint/{pid}
# @app.get("/route/{rid}/gpspoint/{pid}")
# async def read_gps_point(rid: int, pid: int, response: Response):
#     print(f"rid: {rid} pid: {pid}")
#     gps_point = routes.read_gpspoint(rid, pid)
#     if gps_point:
#         return gps_point
#     else:
#         response.status_code = status.HTTP_404_NOT_FOUND
#
#     return None
#
#
# # PUT /route/{rid}/gpspoint/{pid} - update gps point
# @app.put("/route/{rid}/gpspoint/{pid}")
# async def update_point(rid: int, pid: int, gps_point: GPSPoint, response: Response):
#     gps_point = routes.update_gps_point(rid, pid, gps_point)
#     if gps_point:
#         return gps_point
#     else:
#         response.status_code = status.HTTP_404_NOT_FOUND
#
#     return None
#
#
# # POST /route/{rid}/gpspoint/ - add gps point to route
# @app.post("/route/{rid}/gpspoint", status_code=201)
# async def create_gps_point(rid: int, gps_point: GPSPoint):
#     added_gps_point = routes.create_gpspoint(rid, gps_point)
#     return added_gps_point
#
#
# # DELETE /route/{rid}/gpspoint/{pid} - delete gps point from route
# @app.delete("/route/{rid}/gpspoint/{pid}")
# async def delete_gps_point(rid: int, pid: int, response: Response):
#     gps_point = routes.delete_gps_point(rid, pid)
#     if gps_point:
#         return gps_point
#     else:
#         response.status_code = status.HTTP_404_NOT_FOUND
#
#     return None
