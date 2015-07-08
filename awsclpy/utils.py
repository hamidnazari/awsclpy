import os
import collections
from six import string_types


def log(message, time, logdir):
    if not os.path.exists(logdir):
        os.mkdir(logdir)

    date = time.strftime('%Y%m%d')
    time = time.strftime('%H%M%S')

    with open('%s/%s' % (logdir, date), 'a') as logfile:
        logfile.write("%s_%s: %s\n" % (date, time, message))


# By Cristian http://stackoverflow.com/a/2158532/227992
def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and \
                not isinstance(el, string_types):
            for sub in flatten(el):
                yield sub
        else:
            yield el
