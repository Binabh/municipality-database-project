import time
while True:
    localtime = time.localtime()
    mytime = time.strftime("%I:%M:%S %p", localtime)
    print("Keeping container alive at {}!".format(mytime))
    time.sleep(15) 