from notify_run import Notify

notify = Notify()
notify.endpoint('https://notify.run/2F87xZFS1t7nXTXh')

notify.send("Test")
#
# notify.urlparse('https://notify.run/2F87xZFS1t7nXTXh')
