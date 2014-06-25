import evilframe
import inspect


def gimme_frame():
    return inspect.currentframe()


frame = gimme_frame()
test = evilframe.frame(frame, gimme_frame.__code__, globals(), locals())

assert frame is test.f_back

test = evilframe.frame(None, gimme_frame.__code__, globals(), locals())
assert gimme_frame.__code__ is test.f_code
assert test.f_back is None

print('OK!')
