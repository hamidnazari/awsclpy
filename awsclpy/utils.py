import os
import collections

def log(log, time, logdir):
    if not os.path.exists(logdir):
        os.mkdir(logdir)

    date = time.strftime('%Y%m%d')
    time = time.strftime('%H%M%S')

    with open('%s/%s' % (logdir, date), 'a') as logfile:
        logfile.write("%s_%s: %s\n" % (date, time, log))

# By Cristian http://stackoverflow.com/a/2158532/227992
def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, basestring):
            for sub in flatten(el):
                yield sub
        else:
            yield str(el)
