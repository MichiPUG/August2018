from traceback import format_exception_only
from time import strftime
from sys import stdout, stderr, exc_info
from os import environ
import inspect

def print_traceback(remove=None):
    if remove is None:
        remove = 2

    stdout.flush()
    stderr.flush()
    stderr.write(stack_trace(remove) + '\n\n' + stack_dump(max(1, remove-1)))

def exception_handler(exc_type=None, exc_value=None, exc_tb=None):
    print_exception(exc_type, exc_value, exc_tb)
    exit(0)

def print_exception(exc_type=None, exc_value=None, exc_tb=None):
    stdout.flush()
    stderr.flush()
    stderr.write(exception_dump(exc_type, exc_value, exc_tb))

def exception_dump(exc_type=None, exc_value=None, exc_tb=None):
    traceback_env = environ.get('TRACEBACK')
    if traceback_env == 'debug':
        raise

    output = ''

    if traceback_env is None:
        trackback_env = 'normal'
        output += "Current Time: %s\n\n" % strftime('%c')

    if exc_type is None:
        exc_type, exc_value, exc_tb = exc_info()

    output += '\nException:\n'
    output += stack_trace(None, exc_type, exc_value, exc_tb)
    if trackback_env.lower() == 'small':
        return output
    return output + '\n' + stack_dump(None, exc_tb)

def stack_trace(remove=1, exc_type=None, exc_value=None, exc_tb=None):
    """
    Returns a string for the standard python trace back
    """
    # if exec_type is not passed in ask system for exception
    if exc_type is None:
        exc_type, exc_value, exc_tb = exc_info()

    if exc_type is None:
        # if no exception get current stack frame to start of program
        lines = ['Stack Trace (most recent call last):']
        frames = inspect.getouterframes(inspect.currentframe())[remove:]
        frames = reversed(frames)
    else:
        # if exception get  exc_tb.tb_frame to start of program
        lines = ['Traceback (most recent call last):']
        frames = inspect.getinnerframes(exc_tb)

    for frame in frames:
        lines.append(u'Frame File %s at line %s in %s' % (
            frame.filename, frame.lineno, frame.function))
        lines.append(frame.code_context[0].rstrip())

    if exc_type is not None:
        lines.append("%s: %s" % (exc_type.__name__, str(exc_value)))

    output = '\n'.join(lines)

    return output

def stack_dump(remove=None, exc_tb=None):

    # if exec_tb is not passed in ask system for traceback
    if exc_tb is None:
        exc_tb = exc_info()[2]

    if exc_tb is None:
        # if no exception get current stack frame to start of program
        frames = inspect.getouterframes(inspect.currentframe())[remove:]
        frames = reversed(frames)
    else:
        # if exception get  exc_tb.tb_frame to start of program
        frames = inspect.getinnerframes(exc_tb)

    lines = ['Locals by Frame, most recent call last']

    for frame in frames:
        lines.append('')
        lines.append('Frame File %s at line %s in %s' % (
            frame.filename, frame.lineno, frame.function))

        for key, value in frame.frame.f_locals.items():
            if isinstance(value, str):
                value = value[:8192]
            try:
                lines.append('\t%20s = %s' % (key, value))
            except Exception:
                lines.append('\t%20s <ERROR WHILE GETTING VALUE>' % key)

    return '\n'.join(lines) + '\n'



