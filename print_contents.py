def print_directory_contents(sPath):
    # list comprehension
    # import os
    # only_files = [f for f in os.listdir(sPath) if os.path.isfile(os.path.join(sPath, f))]
    # return only_files

    # glob version
    # import glob
    # print(glob.glob('/home/paul/PycharmProjects/oop-test/*.*'))

    # https://www.codementor.io/sheena/essential-python-interview-questions-du107ozr6
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)
