import cv2
import mediapipe as mp
import time
from datetime import datetime
import math
import matplotlib.pyplot as plt
import matplotlib.dates
import numpy as np
from matplotlib.animation import FuncAnimation
import collections



class poseDetector():
    def __init__(self, mode=False, model_complexity=1, smooth=True, enable_segmentation=False, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.model_complexity = model_complexity
        self.smooth = smooth
        self.enable_segmentation = enable_segmentation
        self. detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpPose = mp.solutions.pose
        self.mpDraw = mp.solutions.drawing_utils
        self.pose = self.mpPose.Pose(self.mode, self.model_complexity, self.smooth, self.enable_segmentation, self.detectionCon, self.trackCon)

    def findPose(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img


    def findPosition(self, img, draw=True):
        self.lmlist = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

        return self.lmlist


    def find_angle(self, img, p1, p2, p3, draw=True):

        # Get landmarks
        x1, y1 = self.lmlist[p1][1:]
        x2, y2 = self.lmlist[p2][1:]
        x3, y3 = self.lmlist[p3][1:]

        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))

        if angle < 0:
            angle += 360

        # Draw angle
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0),3)
            cv2.line(img, (x2, y2), (x3, y3), (0, 255, 0),3)

            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)

            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)

            cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)

            cv2.putText(img, str(int(angle)), (x2 - 70, y2 - 10), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255))
        return angle

    def plotTimeSeries(x, y, exercise):
        import io
        fig = plt.figure
        plt.plot_date(x, y)
        plt.title(f'{exercise} Range Of Motion / time')
        plt.gcf().autofmt_xdate()
        img_buf = io.BytesIO()
        print('Saved...')
        plt.savefig(img_buf, format='png')
        return fig

    def printResults(count, tlist):
        rep_time = max(tlist) - min(tlist)
        return int(rep_time.seconds), round(rep_time.seconds / count, 2)


def main():
    cap = cv2.VideoCapture("squats.mp4")
    ptime = 0
    detector = poseDetector()

    while True:
        success, img = cap.read()
        img = detector.findPose(img)

        lmlist = detector.findPosition(img)

        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()