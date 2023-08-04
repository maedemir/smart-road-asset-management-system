import numpy as np
import utm
from exif import Image
import math
import geopy.distance
from pyproj import Proj



def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == "S" or ref == "W":
        decimal_degrees = -decimal_degrees
    return decimal_degrees


def image_coordinates(image_path):
    with open(image_path, 'rb') as src:
        img = Image(src)
        if img.has_exif:
            try:
                coords = (decimal_coords(img.gps_latitude,
                          img.gps_latitude_ref),
                          decimal_coords(img.gps_longitude,
                          img.gps_longitude_ref))
            except AttributeError:
                print('No Coordinates')
        else:
            print('The Image has no EXIF information')
            print(f"Image {src.name}, OS Version:{img.get('software', 'Not Known')} ------")
    return coords


def convert_gps_to_utm(image_path):
    dlat, dlon = image_coordinates(image_path)
    # Convert GPS coordinates to UTM
    easting, northing, zone_num, zone_letter = utm.from_latlon(dlat, dlon)
    # print('Easting:', easting)
    # print('Northing:', northing)
    # print('Zone Number:', zone_num)
    # print('Zone Letter:', zone_letter)
    return easting, northing, zone_num, zone_letter



def utm_to_cartesian(utm_easting, utm_northing, zone_number, zone_letter):
    # Define the UTM projection
    proj_utm = Proj(proj='utm', zone=zone_number, zone_letter = zone_letter, ellps='WGS84', datum='WGS84')

    # Convert UTM coordinates to Cartesian (x, y)
    x, y = proj_utm(utm_easting, utm_northing)

    return x, y

def lat_lon_to_cartesian(gps):
    R = 6371000
    x = R * math.cos(gps[0]) * math.cos(gps[1])
    y = R * math.cos(gps[0]) * math.sin(gps[1])
    z = R * math.sin(gps[0])
    return [x,y,z]

address1 = '/Users/maedehmirzazadeh/Desktop/temppp/6.jpg'
address2 = '/Users/maedehmirzazadeh/Desktop/temppp/7.jpg'

lat_lon1 = image_coordinates(address1)  # latitude and longitude
lat_lon2 = image_coordinates(address2)

gps1 = [convert_gps_to_utm(address1)[0], convert_gps_to_utm(address1)[1]]  # easting and northing first location ( UTM 39S zone)
gps2 = [convert_gps_to_utm(address2)[0], convert_gps_to_utm(address2)[1]]  # easting and northing first location ( UTM 39S zone)

# gps1 = lat_lon_to_cartesian(lat_lon1)
# gps2 = lat_lon_to_cartesian(lat_lon2)

print(lat_lon1) # coordinated in latitude longitude
print(lat_lon2)
print(gps1) # coordinated in UTM
print(gps2)


dx = gps2[0]-gps1[0]
dy = gps2[1]-gps1[1]
d = math.sqrt(dx**2 + dy**2)

# Calculate unit vector of difference vector
ux = dx / d
uy = dy / d

# Calculate angle between vectors in radians

angle = math.atan(uy/ux) #in radian
print(angle)
angle_degrees = (angle * (180/math.pi)) # this angle is the angle between diff vector and x-axis

print(angle_degrees)
# # Print angle in degrees
# print("Angle between difference vector and UTM reference axis: %.2f degrees" % math.degrees(angle))
#
# # calculating rotations of camera axis in respect to utm reference axis
# rot_x = -math.pi/2
# rot_y = 90-angle_degrees
# rot_z = 0
#
# rot_x_matrix = np.array([   [1, 0, 0],
#                             [0, np.cos(rot_x), -np.sin(rot_x)],
#                             [0, np.sin(rot_x), np.cos(rot_x)],
#                             ])
#
# rot_y_matrix = np.array([[np.cos(rot_y), 0, np.sin(rot_y)],
#                             [0, 1, 0],
#                             [-np.sin(rot_y), 0, np.cos(rot_y)]])
#
# rot_z_matrix = np.array(    [[np.cos(rot_z), -np.sin(rot_z), 0],
#                             [np.sin(rot_z), np.cos(rot_z), 0],
#                             [0, 0, 1]])
#
#
# rotation_matrix = rot_x_matrix @ rot_y_matrix @ rot_z_matrix
#
# camera_position = [gps1[0], gps1[1], 10]     # Position of the camera in UTM coordinate
# extrinsic_matrix = np.eye(4)
# # extrinsic_matrix[:3, :3] = rotation_matrix
# extrinsic_matrix[:3, 3] = camera_position
# # print(extrinsic_matrix)
# inv_ext = np.linalg.inv(extrinsic_matrix)
#
# K = [[1415.46024, 0, 964.916262],      # intrinsic matrix
# [0, 1676.70492, 606.212729],
# [0, 0, 1]]
#
# uv = np.array([1190, 666, 30])                               # homogeneous pixel coordinates
#
# c_u = K[0][2]
# c_v = K[1][2]
# f_u = K[0][0]
# f_v = K[1][1]
#
# x = ((uv[0]-c_u)*uv[2])/f_u
# y = ((uv[1]-c_v)*uv[2])/f_v
# z = 30
# Xc = np.array([x, y, z, 1])
#
# Xw = rotation_matrix.T @ Xc + (rotation_matrix @ camera_position)     # transform to world coordinates
# # Xw = np.matmul(inv_ext, Xc)
# print(Xw)

rot_x = -math.pi/2
rot_y = angle_degrees
rot_z = 0

rot_z_matrix = np.array([[np.cos(rot_x), -np.sin(rot_x), 0],
                            [np.sin(rot_x), np.cos(rot_x), 0],
                            [0, 0, 1]])

rot_x_matrix = np.array([[np.cos(rot_y), 0, np.sin(rot_y)],
                            [0, 1, 0],
                            [-np.sin(rot_y), 0, np.cos(rot_y)]])

rot_y_matrix = np.array([[1, 0, 0],
                            [0, np.cos(rot_z), -np.sin(rot_z)],
                            [0, np.sin(rot_z), np.cos(rot_z)]])



rotation_matrix = rot_x_matrix @ rot_y_matrix @ rot_z_matrix

camera_position = [gps1[0], gps1[1], 100]     # Position of the camera in UTM coordinate
extrinsic_matrix = np.eye(4)
extrinsic_matrix[:3, :3] = rotation_matrix
extrinsic_matrix[:3, 3] = camera_position

inv_ext = np.linalg.inv(extrinsic_matrix)

K = [[1415.46024, 0, 964.916262],      # intrinsic matrix
[0, 1676.70492, 606.212729],
[0, 0, 1]]

uv = np.array([20, 100, 1])                               # homogeneous pixel coordinates

inv_K = np.linalg.inv(K)

ray = inv_K @ uv
depth = 20  # this depth is calculated for pixel (1190,666) using zoe depth
Xc = depth * ray        # ray direction vector in camera coordinates

print(Xc)

Xw = rotation_matrix.T @ Xc + (rotation_matrix @ camera_position)     # transform to world coordinates

print(Xw)

