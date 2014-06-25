import evilframe
import inspect
from collections import Counter


def gimme_frame():
    return inspect.currentframe()

if __name__ == '__main__':
    frame = gimme_frame()
    test = evilframe.frame(frame, gimme_frame.__code__, globals(), locals())

    assert frame is test.f_back

    test = evilframe.frame(None, gimme_frame.__code__, globals(), locals())
    assert gimme_frame.__code__ is test.f_code
    assert test.f_back is None


#demo smooshing stack frames
if __name__ == '__main__':
    
    def stack_me_a(func, iterations):
        if iterations == 0:
            return func()
        elif iterations % 3 == 0:
            return stack_me_b(func, iterations-1)
        return stack_me_a(func, iterations-1)

    def stack_me_b(func, iterations):
        return stack_me_a(func, iterations-1)

    def stack_me(iterations=10):
        return stack_me_a(gimme_frame, 10)


    def count_funcnames(start):
        count = Counter(x[0].f_code.co_name for x in inspect.getouterframes(start))
        return count

    def make_stack(start):
        return [x[0] for x in inspect.getouterframes(start)]

    def smoosh(start, *omit_names):
        """Start is an innermost frame (of course, as it's a singly linked list).

        We want to find the outermost frame, and start building our new stack
        from there. We know its f_back is None. If we find any frame named in
        omit_names, we skip adding it. Return the new innermost frame.
        """
        #get a list instead of the start. The 0th element is the innermost frame.
        stack = make_stack(start)
        current = None
        while stack:
            frame = stack.pop()
            if frame.f_code.co_name in omit_names:
                continue
            current = evilframe.frame(current, frame.f_code, frame.f_globals,
                                      frame.f_locals)
        return current


    def test_smoosh():
        inner_frame = stack_me()
        start_stack = make_stack(inner_frame)
        #module frame, test_smoosh (that's us!), stack_me,
        #11 calls to stack_me_a/b, gimme_frame == 15 calls
        assert len(start_stack) == 15
        count = Counter(x.f_code.co_name for x in start_stack)
        assert count['stack_me_a'] == 8
        assert count['stack_me_b'] == 3
        new_inner_frame = smoosh(inner_frame, 'stack_me_b')
        end_stack = make_stack(new_inner_frame)
        assert len(end_stack) == 12
        count = Counter(x.f_code.co_name for x in end_stack)
        assert count['stack_me_a'] == 8
        assert count['stack_me_b'] == 0


    test_smoosh()
    print('OK!')








