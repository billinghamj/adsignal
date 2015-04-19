from liblo import *
import sys
import time
import signal
import json

class MuseServer(ServerThread):
    #listen for messages on port 5001 
    concentrations = []
    mellows = []

    def __init__(self):
        ServerThread.__init__(self, 5000)
    
    #receive EEG data

    @make_method('/muse/elements/experimental/concentration', 'f')
    def concentration_callback(self, path, args):
        concentration = args
        self.concentrations.append(concentration[0])
        print concentration

    @make_method('/muse/elements/experimental/mellow', 'f')
    def mellow_callback(self, path, args):
        mellow = args
        self.mellows.append(mellow[0])

try:
    server = MuseServer()

except ServerError, err:
    print str(err)
    sys.exit()


def signal_handler(signal, frame):
        
        # build array

        dictionary = {}

        averages = {}

        averages['concentration'] = sum(server.concentrations) / float(len(server.concentrations))
        averages['mellowness'] = sum(server.mellows) / float(len(server.mellows))

        master = []

        for i in range(0,len(server.mellows)):
            row = []
            row.append(i/10.0) # frane number
            row.append(server.concentrations[i])
            row.append(server.mellows[i])
            master.append(row)

        dictionary['avg'] = averages
        dictionary['data'] = master

        json_ = json.dumps(dictionary)
        text_file = open("data.json", "w")
        text_file.write(json_)
        text_file.close()

        server.stop()
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
server.start()

if __name__ == "__main__":
    while 1:
        time.sleep(1)
