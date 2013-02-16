__author__ = 'JohnLiu'
import threading
from time import sleep, ctime

loops = [4,2]
class OneThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        #apply(self.func, self.args)  can be replaced by following code
        print 'starting ', self.name, 'at: ',ctime()
        self.res = apply(self.func, self.args)
        print self.name, 'finished at: ',ctime()

def loop(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()

def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))
    for i in nloops: # create all threads
        t = OneThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops: # start all threads
        threads[i].start()

    for i in nloops: # wait for completion
        threads[i].join()
    print 'all DONE at:', ctime()
if __name__ == '__main__':
    main()

