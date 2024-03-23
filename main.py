import time
#time.sleep(60) # zzzzzzz

# Imports
from client_networktables import initialize_networktables, put_pose, put_has_pose

# Python imports
from detect_tags import detect_tag, get_tags
from estimate_pose import estimate_pose

# Initialize networktables
print("Initializing networktables")
initialize_networktables("10.67.31.2") # 10.TE.AM.2

# Imports
import numpy as np
import cv2
import gi

# import required library like Gstreamer and GstreamerRtspServer
gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GObject

cam = cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=960, height=540 ! nvvidconv flip-method=2 ! video/x-raw,format=BGRx ! videoconvert ! video/x-raw,format=BGR ! appsink")

def pa(pt):
    return [pt.x,pt.y]

def draw_tags(image, tags):
    '''
    Input: original unmodified frame image, tag data, time
    Output: rendered image with apriltag overlay
    '''
    for tag in tags:
        tag_id = tag.getId()
        center = [tag.getCenter().x, tag.getCenter().y]
        corners = [pa(tag.getCorner(0)),pa(tag.getCorner(1)),pa(tag.getCorner(2)),pa(tag.getCorner(3))]

        center = (int(center[0]), int(center[1]))
        corner_01 = (int(corners[0][0]), int(corners[0][1]))
        corner_02 = (int(corners[1][0]), int(corners[1][1]))
        corner_03 = (int(corners[2][0]), int(corners[2][1]))
        corner_04 = (int(corners[3][0]), int(corners[3][1]))

        # center
        cv2.circle(image, (center[0], center[1]), 5, (0, 0, 255), 2)

        # sides
        cv2.line(image, (corner_01[0], corner_01[1]),
                (corner_02[0], corner_02[1]), (255, 0, 0), 2)
        cv2.line(image, (corner_02[0], corner_02[1]),
                (corner_03[0], corner_03[1]), (255, 0, 0), 2)
        cv2.line(image, (corner_03[0], corner_03[1]),
                (corner_04[0], corner_04[1]), (0, 255, 0), 2)
        cv2.line(image, (corner_04[0], corner_04[1]),
                (corner_01[0], corner_01[1]), (0, 255, 0), 2)

        # tag name
        cv2.putText(image, str(tag_id), (center[0] - 10, center[1] - 10),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2, cv2.LINE_AA)

def streamReady():
    return cam.isOpened()
    
def captureForStream():
    ret, frame = cam.read()

    if not frame is None:
        startTime = time.perf_counter_ns()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detects tags
        tags = get_tags(gray)
        draw_tags(frame, tags)
        robot_to_april, tag_id = detect_tag(frame=gray)

        # If a tag exists:
        if robot_to_april:
            # Gets pose
            pose2d = estimate_pose(robot_to_april, tag_id)
            pose = [pose2d.translation().X(), pose2d.translation().Y(), pose2d.rotation().radians()]
            # Puts on networktables
            elapsed = time.perf_counter_ns() - startTime
            put_pose(pose, tag_id, elapsed / 1000)
            put_has_pose(True)
        else:
            put_has_pose(False)

    return ret, frame

# Sensor Factory class which inherits the GstRtspServer base class and add
# properties to it.
class SensorFactory(GstRtspServer.RTSPMediaFactory):
    def __init__(self, **properties):
        super(SensorFactory, self).__init__(**properties)
        self.number_frames = 0
        self.fps = 30
        self.duration = 1 / self.fps * Gst.SECOND  # duration of a frame in nanoseconds
        self.launch_string = 'appsrc name=source is-live=true block=true format=GST_FORMAT_TIME ' \
                             'caps=video/x-raw,format=BGR,width={},height={},framerate={}/1 ' \
                             '! videoconvert ! video/x-raw,format=I420 ' \
                             '! x264enc speed-preset=ultrafast tune=zerolatency ' \
                             '! rtph264pay config-interval=1 name=pay0 pt=96' \
                             .format(960, 540, self.fps)
    # method to capture the video feed from the camera and push it to the
    # streaming buffer.
    def on_need_data(self, src, length):
        if streamReady():
            ret, frame = captureForStream()
            if ret:
                data = frame.tostring()
                buf = Gst.Buffer.new_allocate(None, len(data), None)
                buf.fill(0, data)
                buf.duration = self.duration
                timestamp = self.number_frames * self.duration
                buf.pts = buf.dts = int(timestamp)
                buf.offset = timestamp
                self.number_frames += 1
                retval = src.emit('push-buffer', buf)
                if retval != Gst.FlowReturn.OK:
                    print(retval)
    # attach the launch string to the override method
    def do_create_element(self, url):
        return Gst.parse_launch(self.launch_string)
    
    # attaching the source element to the rtsp media
    def do_configure(self, rtsp_media):
        self.number_frames = 0
        appsrc = rtsp_media.get_element().get_child_by_name('source')
        appsrc.connect('need-data', self.on_need_data)

# Rtsp server implementation where we attach the factory sensor with the stream uri
class GstServer(GstRtspServer.RTSPServer):
    def __init__(self, **properties):
        super(GstServer, self).__init__(**properties)
        self.factory = SensorFactory()
        self.factory.set_shared(True)
        self.set_service(str(8554))
        self.get_mount_points().add_factory("/stream", self.factory)
        self.attach(None)

# initializing the threads and running the stream on loop.
GObject.threads_init()
Gst.init(None)
server = GstServer()
loop = GObject.MainLoop()
loop.run()

#while True:
#    captureForStream()
