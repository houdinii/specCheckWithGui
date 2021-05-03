import cv2


class WebcamRecord:
    def __init__(self, source=None, status=None):
        self.source = source
        self.status = status


class WebcamRecords:
    """
    A list of Webcam Records
    """
    def __init__(self, webcam_record_list=None):
        # Check if all list items are WebcamRecord and if so, add them to self.
        if webcam_record_list and all(isinstance(x, WebcamRecord) for x in webcam_record_list):
            self.list = webcam_record_list
        else:
            self.list = []

    def addRecord(self, webcam_record):
        if isinstance(webcam_record, WebcamRecord):
            self.list.append(webcam_record)

    def test(self):
        self.list = []
        count = 0
        cap = None

        while True:
            cap = cv2.VideoCapture(count, cv2.CAP_DSHOW)
            if cap is None or not cap.isOpened():
                if count > 10:
                    break
            else:
                self.addRecord(WebcamRecord(source=count+1, status=True))
            count += 1

        cv2.destroyAllWindows()

        if len(self.list) == 0:
            self.addRecord(WebcamRecord(source=0, status=False))
        return self

