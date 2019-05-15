def cm(a):
    print("entering")
    yield a
    print("exiting")


c = cm(3)
