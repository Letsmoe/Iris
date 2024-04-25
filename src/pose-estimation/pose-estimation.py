import posecamera
import cv2
import os
import sys
import numpy as np

def get_script_path():
		return os.path.dirname(os.path.realpath(sys.argv[0]))

image = cv2.imread(get_script_path() + "/examples/example.webp")
# Scale image down to improve performance
# At most 640x480
# Get the scaling factor
scale_factor = 640 / image.shape[1]
# Resize the image
image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)

det = posecamera.pose_tracker.PoseTracker()

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

boxes, weights = hog.detectMultiScale(image, winStride=(8, 8), padding=(32, 32), scale=1.05)

boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

for (xA, yA, xB, yB) in boxes:
	# display the detected boxes in the colour picture
	cv2.rectangle(image, (xA, yA), (xB, yB),
										(0, 255, 0), 2)
	
	# get a subimage of the detected person
	subimage = image[yA:yB, xA:xB]
	# detect the pose of the person
	pose = det(subimage)
	for name, (y, x, score) in pose.keypoints.items():
		cv2.circle(image, (int(xA + x), int(yA + y)), 4, (255, 0, 0), -1)


cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

exit(0)