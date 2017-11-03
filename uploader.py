import xmltodict
import struct
from time import ctime
from threading import Thread, Lock
from queue import Queue
from uploaderconstant import Constant

class Worker(Thread):

    def __init__(self, func, args, name=''):
        super(Worker, self).__init__()

        #: Job to do.
        self.func = func

        #: Arguments for working.
        self.args = args

        #: Job name.
        self.name = name

class Uploader(object):

    def __init__(self, config_file):

        #: Config file path for initializing uploader.
        self.config_file = config_file

        #: Config params dict, which data from config file.
        self.config_params = {}

        #: Protocol Module, main function include:
        #: 1.Packs data for sending to center.
        #: 2.Unpacks data for receiving from center.
        self.protocol = None

        #: Queue for fetch sending data.
        #: Put: various jobs put data into it.
        #: Get: send job get data from it.
        self.send_queue = Queue(Constant.SEND_QUEUE_CAPACITY)

        #: Queue for fetch receiving data
        #: Put: recv job put data into it.
        #: Get: analyze job get data from it.
        self.recv_queue = Queue(Constant.RECV_QUEUE_CAPACITY)

    def fetchConfigParam(self):
        """Fetchs config param from config file, fill self.config_params.
        """
        pass

    def fetchRealtimeVehicle(self):
        """Check whether has realtime vehicle data, if existed,
        packing by :class:`protocol`
        :rtype: :class:`bytes`
        """
        pass

    def fetchRetryVehicle(self):
        pass

    def PutHeartbeat(self):
        """Check whether need to pack heartbeat data, if needed,
        packing by :class:`protocol` and put packed data into send queue.
        """
        pass

    def PutAlarm(self):
        """Check whether system is abnormal, if it is,
        packing by :class:`protocol` and put packed data into send queue.
        """
        pass

    def checkRecvData(self):
