"""
    You'd better read each function introduce detailed to know how to use it

    Brief Introduce:

        OpenCvTrainer help you to input parameter directly rather open the cmd
        You will replace the base_dir, which is the location of This File
        When the "lock" is True, the open_cv_trainer will do nothing when you use the Cmd method
        You can set remark --> False to avoid remark the label again

        The AnalyseMachine used to see weather your train works fine

        The only thing you need to do is put your picture in the right file:

        • negative --- put the picture different from your recognize objects
        • positive --- put your recognize objects
        • Test     --- put your test images

    Attention:

        Before you want to train again totally, please delete the following files:

        • info.txt
        • negative.txt
        • vector.vec
        • model

"""

import cv2
import Road_Block_Recognition.Utils as Utils
from Road_Block_Recognition.Analyse import AnalyseMachine
from Road_Block_Recognition import OpencvTrain

base_dir = r'cd C:\Users\86158\Desktop\OpenCV\Road_Block_Recognition'

if __name__ == "__main__":

    open_cv_trainer = OpencvTrain.OpenCvTrainer(basedir=base_dir, lock=True)
    open_cv_trainer.Prepare_Data(rename_list=['positive', 'negative', 'Test'])
    open_cv_trainer.Cmd_Annotation(_a='info', _i='positive/', _m=720, _r=6, remark=False)
    open_cv_trainer.Cmd_Creat_Samples(_info='info', _vec='vector', _w=24, _h=24)
    open_cv_trainer.Cmd_Train(_data='model', _vec='vector', _bg='negative', _numPos=30, _numNeg=200, _numStages=20, _w=24, _h=24)

    xml_dir = "model/cascade.xml"
    img = cv2.imread("Test/Test-img(3).jpg")
    img_list = Utils.Get_Img_List_From_File('Test')
    analyse_machine = AnalyseMachine()
    analyse_machine.Recognize_Picture(xml_dir=xml_dir, img=img, img_size=(700, 700))
