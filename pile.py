#!/usr/bin/env python3

import gphoto2cffi as gp

def pile():
    cam = gp.Camera()

    # capture preview, because focus can only be adjusted after capturing a preview
    #cam.get_preview()
    #cam.capture(to_camera_storage=True)

    cam.config['actions']['manualfocusdrive'] = 1000


if __name__ == '__main__':
    pile()
