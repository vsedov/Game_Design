from menu_controller import Starter


def real_start(frame=None):
    if frame is None:

        initial_start = Starter()
    else:
        initial_start = Starter(frame)


real_start()
