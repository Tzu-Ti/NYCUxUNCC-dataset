import time
import cv2
import argparse
import numpy as np
import configparser
import sys
import os

from pylepton.Lepton3 import Lepton3
from picamera2 import Picamera2
import _thread

def get_parse():
    # 建立解析器
    parser = argparse.ArgumentParser()

    parser.add_argument('--preview', action='store_true')
    parser.add_argument('--save', action='store_true')
    parser.add_argument('--folder_path', required='--save' in sys.argv)
    args = parser.parse_args()
    return args

class ColorCamera():
    def __init__(self, config):
        self.picam2 = Picamera2()
        mode = self.picam2.sensor_modes[3]
        for m in self.picam2.sensor_modes:
            print(m)
        piconfig = self.picam2.create_preview_configuration()
        piconfig['raw']['size'] = mode['size']
        piconfig['raw']['format'] = 'SRGGB8'
        piconfig['main']['format'] = 'BGR888'
        for conf in piconfig:
            print(conf, piconfig[conf])
        self.picam2.configure(piconfig)
        self.picam2.start()
        
        self.visible_win_h = int( config.get( 'visible', 'win_h' ) )
        self.visible_win_w = int( config.get( 'visible', 'win_w' ) )
        self.startX = int( config.get( 'stereo', 'startX' ) )
        self.startY = int( config.get( 'stereo', 'startY' ) )
        self.endX = int( config.get( 'stereo', 'endX' ) )
        self.endY = int( config.get( 'stereo', 'endY' ) )

    def capture(self):
        image = self.picam2.capture_array("main")
        return image

    def process(self, img):
        if img.shape[1] != self.visible_win_w:
            img = cv2.resize(img, (self.visible_win_h, self.visible_win_w))
        img = img[self.startY: self.endY, self.startX: self.endX]
        return img

def process_thermal(img):
    cv2.normalize( img, img, 0, 65535, cv2.NORM_MINMAX )
    np_img = img.copy()
    np.right_shift( img, 8, img )
    img = np.asarray( img, np.uint8 )

    return np_img, img

def save_rgb( filename, img):
    filename = filename+".jpg"
    cv2.imwrite(filename, img)

def save_npy( filename, img):
    np.save(filename, img)

def main():
    args = get_parse()
    config = configparser.ConfigParser()
    config.read( './fusion.conf' )
    
    cap = ColorCamera(config)

    while True:
        start = time.time()
        
        # get thermal
        with Lepton3() as leptonCap:
            thermal, _ = leptonCap.capture()
        np_thermal, thermal = process_thermal(thermal)

        # get RGB
        rgb = cap.capture()
        rgb = cap.process(rgb)
        if args.preview:
            thermal_rgb = cv2.applyColorMap( thermal, cv2.COLORMAP_HOT )
            img1 = cv2.resize( thermal_rgb, (320, 240), interpolation=cv2.INTER_NEAREST)

            img2 = cv2.resize(rgb, (320, 240))

            horizontal = np.hstack((img1, img2))
            cv2.imshow("dual_camera", horizontal)

        if args.save:
            filename = f"{time.time_ns()}"
            filepath = os.path.join(args.folder_path, filename)
            
            save_rgb(filepath, rgb)
            save_npy(filepath, np_thermal)

        if cv2.waitKey( 1 ) & 0xFF == ord( "q" ):
            break
        print(f"\rfps:{1/(time.time()-start):.2f}", end = '')


if __name__ == '__main__':
    main()
    cv2.destroyAllWindows()
    
