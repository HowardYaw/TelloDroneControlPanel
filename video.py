import time
import cv2
from threading import Thread, RLock
import socket
import numpy


class Video():

    def __init__(self):
        self.isStreamOn = False
        self.lock = RLock()
        self.tello = None

        # Setup UDP socket for video
        self.video_port = 1111
        self.video_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.video_socket.bind(('', self.video_port))

        # Start thread to receive frame streamed over UDP socket
        self.receive_video_thread = Thread(target=self.get_video)
        self.receive_video_thread.daemon = True
        self.receive_video_thread.start()
    
    def setTello(self, telloInstance):
        self.tello = telloInstance

    def streamOn(self):
        if self.tello is None: 
            print('Not Connected to Drone')
            return False
        print("Turn On Video Stream")
        if not self.isStreamOn:
            self.tello.send("streamon", 1)
            self.isStreamOn = True
        else:
            print('already start streaming')
        return True

    def streamOff(self):
        print("Turn Off Video Stream")
        if self.isStreamOn:
            self.receive_video_thread.join()
            self.tello.send("streamoff", 1)
            self.isStreamOn = False
        else:
            print('already off streaming')

    def get_video(self):
        s = ""
        while True:
            # with self.lock:
            data, ip = self.video_socket.recvfrom(2048)
            s += data
            if len(s) == (2048*20):
                self.frame = numpy.fromstring(s, dtype=numpy.uint8)
                self.frame = self.frame.reshape(480, 640, 3)
                # cv2.imshow("frame",frame)
                s = ""

    # *
    # Return the current frame
    # *
    def get_frame(self):
        return self.frame


# # *
# # Test Driver Code
# # *
# if __name__ == "__main__":
#     tello = Tello()
#     video_handler = Video(telloInstance=tello)
#     video_handler.streamOn()
#     video_handler.get_video()
#     video_handler.streamOff()
