# import time
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler


# class Watcher:
#     DIRECTORY_TO_WATCH = "/Volumes/grau'"+"s/0-proj/_faces/narciatio/v4/output/crop/"

#     def __init__(self):
#         self.observer = Observer()

#     def run(self):
#         event_handler = Handler()
#         self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
#         self.observer.start()
#         try:
#             while True:
#                 time.sleep(5)
#         except:
#             self.observer.stop()
#             print "Error"

#         self.observer.join()


# class Handler(FileSystemEventHandler):

#     @staticmethod
#     def on_any_event(event):
#         if event.is_directory:
#             return None

#         elif event.event_type == 'created':
#             # Take any action here when a file is first created.
#             print "Received created event - %s." % event.src_path
# 			# ser.write("1")



# if __name__ == '__main__':
#     w = Watcher()
#     w.run()

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import serial

##Boolean that will represent if arduino is connected
connected = False

##open serial port with the arduino
ser = serial.Serial (port="/dev/cu.usbmodem1411",baudrate=9600)
##loop until arduino says it is ready
while not connected:
  serin = ser.read()
  connected = True

class Watcher:
    DIRECTORY_TO_WATCH = "/Volumes/grau'"+"s/0-proj/_faces/narciatio/v4/output/crop/"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print "Error"

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            ser.write("0")
            return None


        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print 'file created'
            print "%s." % event.src_path
            ## Tell arduino to blink
            ser.write("1")

if __name__ == '__main__':
    w = Watcher()
    w.run()

##Wait until arduino says it finesh blinking
while ser.read()=='1':
  ser.read()

##Close the port
ser.close()
