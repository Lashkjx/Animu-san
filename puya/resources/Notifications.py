from notify_run import Notify

notify = Notify()
notify.read_config()

def pushNotification(msg):
    notify.send('Kanan-chan! A new episode available: ' + msg)

def pushSadNotification(msg):
    notify.send(msg)

