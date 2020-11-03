import rosbag
#import os
import cv2
import numpy as np
from cv_bridge import CvBridge
import sys


# read bag files:
bag = rosbag.Bag(sys.argv[1])

bridge = CvBridge()

# create bag files:
processed_bag = rosbag.Bag('mounted_volume/amod20-rh3-ex-process-xiaoao-song.bag', 'w')

# parameters for place the text on the image
font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (20,40)
fontScale = 1
fontColor = (255,255,255)
lineType = 2


# For the image message in the bag file, do the following:
# 	Extract the timestamp from the message
# 	Extract the image data from the message
# 	Draw the timestamp on top of the image
# 	Write the new image to the new bag file, with the same topic name, same timestamp, 
#   		and the same message type as the original message

init = 0
# Reading info from bag
for topic, msg, t in bag.read_messages(topics=['/jcdgo/camera_node/image/compressed']):
    np_arr = np.fromstring(msg.data, np.uint8)
    image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    cv2.putText(image_np,str(t), 
                 bottomLeftCornerOfText, 
                 font, 
                 fontScale,
                 fontColor,
                 lineType)
    if init %10000 ==0:
    	cv2.imwrite("testimgs.png", image_np)
    	print("Saved the first testpic", init)
    	init = init +1
    	print("info of this image:")
    	print("topic=",topic)
    	print("t=",t)
#     	print("msg=",msg)
    	
    
	
# 	Converting OpenCV images to ROS image messages
    compressed_img_msg = bridge.cv2_to_compressed_imgmsg(image_np, dst_format='jpg')
    
#     Write the results to a new bag file
    processed_bag.write('/jcdgo/camera_node/image/compressed', compressed_img_msg, t)

bag.close()
processed_bag.close()