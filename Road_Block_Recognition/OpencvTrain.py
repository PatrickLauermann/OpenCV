import os
import Road_Block_Recognition.Utils as Utils

class OpenCvTrainer(object):
    def __init__(self, basedir, lock=True):

        """
            :param basedir: the location where this file is
            :param lock: weather the trainer activate the cmd

            you may put the file in "C:\\Users\\123456\\Desktop\\OpenCV\\Road_Block_Recognition"

            then you can use it as follow:

            base_dir = r'cd C:\\Users\\86158\\Desktop\\OpenCV\\Road_Block_Recognition'
            open_cv_trainer = OpencvTrain.OpenCvTrainer(basedir=base_dir, lock=False)

        """

        self.base_dir = basedir
        self.lock = lock

    def Prepare_Data(self, rename_list):
        """
            :param rename_list: the file you want to rename

            :return: None

            This method help you to rename the img you saved and build the negative img label file

            for example:

                open_cv_trainer.Prepare_Data(rename_list=['positive', 'negative', 'Test'])

            It will work only when you start you open_cv_trainer with lock=False

        """

        if self.lock is False:
            for file_name in rename_list:
                Utils.Rename_Img(file_name)
            Utils.Build_List_Negative(filename='negative', creat_filename='negative')

    def Cmd_Run(self, cmd):
        """

            :param cmd: the command you need to run in cmd

            :return: None

            For internal use, no need to care

        """
        if self.lock is False:
            command = self.base_dir + ' && ' + cmd
            os.system(command)
        else:
            print("OpenCv Trainer is locked!")

    def Cmd_Annotation(self, _a, _i, _m=None, _r=None, remark=True):
        """

            :param _a: the file saved the info of the object location which in the positive img, it will be the output with a file named _a
            :param _i: the source of positive img
            :param _m: if the picture is too large to show in screen, you can set _m,and when the img height > _m it will zoom with _r
            :param _r: the zoom rate
            :param remark: weather you need to remark the location

            :return: None

            for example:

                open_cv_trainer.Cmd_Annotation(_a='info', _i='positive/', _m=720, _r=6, remark=False)

            then you will creat a new file named "info.txt" in your basedir after you mark the img, the img comes from
            '(basedir)/positive', when the img height > 720, the img size will be zoomed with 6 times


            Attention:
                if this function worked, it will creat a nex txt file, it not, check it

        """

        if remark:
            cmd = 'opencv_annotation'
            annotations = ' -a={}.txt'.format(_a)
            images = ' -i={}'.format(_i)
            max_height = ' -m={}'.format(_m) if _m is not None else ''
            resize_factor = ' -r={}'.format(_r) if _r is not None else ''
            cmd = cmd + annotations + images + max_height + resize_factor
            self.Cmd_Run(cmd)

    def Cmd_Creat_Samples(self, _info, _vec, _img=None, _w=None, _h=None, _bg=None, _num=None):
        """

            :param _info: the output file you created by the method "Cmd_Annotation"
            :param _vec: this method will output this file as a result
            :param _img: input img file name
            :param _w: compressed picture width
            :param _h: compressed picture height
            :param _bg: negative sample description file, which contains a series of image filenames randomly selected as object backgrounds
            :param _num: the number of created positive samples

            :return: None

            for example:

                open_cv_trainer.Cmd_Creat_Samples(_info='info', _vec='vector', _w=24, _h=24)

            then you will get the vector.vec file sources from info.txt

            Attention:
                if this method worked, the debug info will be like:
                    Done. Created xx samples

        """

        cmd = 'opencv_createsamples'
        info = ' -info {}.txt'.format(_info)
        vec = ' -vec {}.vec'.format(_vec)
        img = ' -img {}'.format(_img) if _img is not None else ''
        bg = ' -bg {}'.format(_bg) if _bg is not None else ''
        num = ' -num {}'.format(_num) if _num is not None else ''
        w = ' -w {}'.format(_w) if _w is not None else ''
        h = ' -h {}'.format(_h) if _h is not None else ''
        cmd = cmd + info + vec + img + bg + num + w + h
        self.Cmd_Run(cmd)

    def Cmd_Train(self, _data, _vec, _bg, _numPos, _numNeg, _numStages, _w, _h,
                  _precalcValBufSize=1024, _precalcldxBufSize=1024, _weightTrimRate=0.95, _maxDepth=1,
                  _acceptanceRatioBreakValue=1.0e-5):
        """

            :param _data: where the xml file be created as output you saved in
            :param _vec: the vector.vec created by "Cmd_Creat_Samples"
            :param _bg: the negative.txt created by "open_cv_trainer.Prepare_Data(...)"
            :param _numPos: the number of positive img
            :param _numNeg: the number of negative img
            :param _numStages: the number of stages
            :param _w: must equal the _w you input in "Cmd_Creat_Samples"
            :param _h: must equal the _h you input in "Cmd_Creat_Samples"
            :param _precalcValBufSize: define by your computer
            :param _precalcldxBufSize: define by your computer
            :param _weightTrimRate: 0.95 works fine
            :param _maxDepth: 1 works fine
            :param _acceptanceRatioBreakValue: prevent over fitting error

            :return: None

            for example:
                open_cv_trainer.Cmd_Train(_data='model', _vec='vector', _bg='negative', _numPos=30, _numNeg=200, _numStages=20, _w=24, _h=24)

            then the cascade.xml will be created in model file, you can run Analyse to see weather it's fine

            Attention:
                if this method worked, the model file will creat a cascade.xml file and some stages.xml
        """
        cmd = 'opencv_traincascade'
        data = ' -data {}'.format(_data)
        vec = ' -vec {}.vec'.format(_vec)
        bg = ' -bg {}.txt'.format(_bg)
        numPos = ' -numPos {}'.format(_numPos)
        numNeg = ' -numNeg {}'.format(_numNeg)
        numStages = ' -numStages {}'.format(_numStages)
        w = ' -w {}'.format(_w)
        h = ' -h {}'.format(_h)
        precalcValBufSize = ' -precalcValBufSize {}'.format(_precalcValBufSize)
        precalcldxBufSize = ' -precalcldxBufSize {}'.format(_precalcldxBufSize)
        weightTrimRate = ' -weightTrimRate {}'.format(_weightTrimRate)
        maxDepth= ' -maxDepth {}'.format(_maxDepth)
        acceptanceRatioBreakValue = ' -acceptanceRatioBreakValue {}'.format(_acceptanceRatioBreakValue)
        cmd = cmd + data + vec + bg + numPos + numNeg + numStages + w + h + precalcValBufSize + precalcldxBufSize + \
              weightTrimRate + maxDepth + acceptanceRatioBreakValue
        self.Cmd_Run(cmd)



