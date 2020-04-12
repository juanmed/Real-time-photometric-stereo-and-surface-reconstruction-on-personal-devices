
import sys
import numpy as np
import pyzed.sl as sl
import cv2

# Create a ZED camera object
zed = sl.Camera()

# Set configuration parameters
input_type = sl.InputType()
#if len(sys.argv) >= 2 :
#    input_type.set_from_svo_file(sys.argv[1])
init = sl.InitParameters(input_t=input_type)
init.camera_resolution = sl.RESOLUTION.HD720
init.depth_mode = sl.DEPTH_MODE.PERFORMANCE
init.coordinate_units = sl.UNIT.MILLIMETER


# Open the camera
err = zed.open(init)
if err != sl.ERROR_CODE.SUCCESS :
    print(repr(err))
    zed.close()
    sys.exit(1)


# Create an RGBA sl.Mat object
image_zed = sl.Mat(zed.get_camera_information().camera_resolution.width, zed.get_camera_information().camera_resolution.height, sl.MAT_TYPE.U8_C4)
# Retrieve data in a numpy array with get_data()
image_ocv = image_zed.get_data()

while True:

    if zed.grab() == sl.ERROR_CODE.SUCCESS :
        # Retrieve the left image in sl.Mat
        zed.retrieve_image(image_zed, sl.VIEW.LEFT)
        # Use get_data() to get the numpy array
        image_ocv = image_zed.get_data()
        # Display the left image from the numpy array
        cv2.imshow("Image", image_ocv)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

sys.exit(1)