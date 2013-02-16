__author__ = 'JohnLiu'
import thread
from time import ctime, sleep

#define the list loop functions
def loop_1():
    print 'start loop 0 at %s ' % ctime()
    sleep(4)
    print 'end loop 0  at %s' % ctime()

def loop_2():
    print 'start loop 1 at %s ' % ctime()
    sleep(2)
    print 'end loop 1 %s ' % ctime()

def main():
    print 'app starts at:', ctime()
    thread.start_new_thread(loop_1, ())
    thread.start_new_thread(loop_2, ())
    sleep(6)
    print 'app ends at:', ctime()

if __name__ == '__main__':
    main()