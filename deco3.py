from functools import wraps


def log(utf8_string, tags):
    # do some logging
    pass


def log_on_exception(*tags):
    """Decorate a function to log any exception it raises.
    This decorator provides functionality to log a message
    when an exception is raised from within the decorated
    function.
    :param tags: a sequence of tags
    :return: the result of the function it wraps
    """

    def func_decor(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            try:
                func_result = func(*args, **kwargs)

            except Exception as e:
                error_msg = getattr(e, 'message', repr(e))
                log(error_msg, tags)

                # re-raise exception
                raise

            return func_result

        return wrapper

    return func_decor
