def tracer(msg):
    print("[TRACE]%s" % msg)


def logger(func):
    tracer("logger")
    def inner(username,passwd):
        tracer("inner")
        print("call %s" % func.__name__)
        return func(username,passwd)
    return inner

def login_debug_helper(show_debug_info=False):
    tracer("login_debug_helper")
    def proxy_fun(func):
        tracer("proxy_fun")
        def delegate_fun(username,passwd):
            tracer("delegate_fun")
            if show_debug_info:
                print("username:%s \npasswd:%s"%(username,passwd))
            return func(username,passwd)
        return delegate_fun
    return proxy_fun

print("Declaring login_a")


@logger
@login_debug_helper(show_debug_info=True)
def login_a(username,passwd):
    tracer("login_a")
    print("do some login authentication")
    return True


print("call login_a")
login_a("md","pwd")
