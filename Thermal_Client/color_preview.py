from picamera2 import Picamera2
import time
import cv2
import argparse

# 建立解析器
parser = argparse.ArgumentParser()

parser.add_argument('--preview', action='store_true')
parser.add_argument('--save', action='store_true')
args = parser.parse_args()

picam2 = Picamera2()
config = picam2.create_still_configuration()
picam2.configure(config)
picam2.start()
time.sleep(2)

# start = time.time()
i = 0
while True:
    image = picam2.capture_array("main")

    if args.preview:
        image = cv2.resize(image, (640, 320))
        cv2.imshow("Preview", image)
    if args.save:
        filename = 'Output/image_{}.png'.format(i)
        cv2.imwrite(filename, image)
        i += 1

#     if time.time() - start > 2:
#         break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

if args.preview:
    cv2.destroyAllWindows()