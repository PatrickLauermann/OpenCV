"""
    date: 2021-10-22
    author: Ji Xiaoyu
"""

import cv2

class AnalyseMachine(object):
    def __init__(self):
        pass

    def __str__(self):
        pass

    __repr__ = __str__

    def Recognize_Single_Picture(self, xml_dir, img):
        try:
            roadblock_cascade = cv2.CascadeClassifier(xml_dir)
        except:
            Exception("xml_dir error!")
            return None
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        location = roadblock_cascade.detectMultiScale(gray_image, 1.2, 5)
        for (x, y, w, h) in location:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow('Analise Result', img)
        if len(location) is not 0:
            print("The rectangle lower left starting point is ({},{}) and the width is {},height is {}".format(location[0][0], location[0][1], location[0][2], location[0][3]))
        else:
            print("Not Found!")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return location

    def Recognize_Pictures(self, xml_dir, img_list, img_size):
        img_num = len(img_list)
        right_cnt = 0
        print("press 0 to continue")
        for img in img_list:
            img = cv2.resize(img, img_size)
            location = self.Recognize_Single_Picture(xml_dir, img)
            if len(location) > 0:
                right_cnt += 1
        if img_num is not 1:
            print("recognize rate:{:.2f}".format(right_cnt / img_num * 100) + '%')

    def Recognize_Picture(self, xml_dir, img, img_size=(500, 500)):
        if type(img) is not list:
            img = cv2.resize(img, img_size)
            self.Recognize_Single_Picture(xml_dir, img)
        else:
            self.Recognize_Pictures(xml_dir, img, img_size)

class AnalyseRealtimeMachine(AnalyseMachine):
    def __init__(self, camera_id):
        super().__init__()
        self.camera = cv2.VideoCapture(camera_id)

    def Realtime_Recognize(self, xml_dir, img_size=(500, 500)):
        while True:
            _ , img = self.camera.read()
            self.Recognize_Picture(xml_dir, [img], img_size=img_size)
            if cv2.waitKey(60) == 27:
                break
        self.camera.release()
        cv2.destroyAllWindows()
