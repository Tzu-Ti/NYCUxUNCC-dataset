from pylepton.Lepton3 import Lepton3

import numpy as np
import cv2
import argparse
import time

# 建立解析器
parser = argparse.ArgumentParser()

parser.add_argument('--preview', action='store_true')
parser.add_argument('--save', action='store_true')
args = parser.parse_args()

with Lepton3() as leptonCap:
    start = time.time()
    i = 0
    while True:
        thermal, _ = leptonCap.capture()
        cv2.normalize( thermal, thermal, 0, 65535, cv2.NORM_MINMAX )
        np_thermal = thermal.copy()
        np.right_shift( thermal, 8, thermal )
        thermal = np.asarray( thermal, np.uint8 )

        if args.preview:
            cv2.imshow("Preview", thermal)
        if args.save:
            filename = 'Output/image_{}.png'.format(i)
            cv2.imwrite(filename, thermal)
            i += 1

        if time.time() - start > 2:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()