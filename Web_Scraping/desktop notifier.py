from plyer import notification
def notification_on(title,message,time):
    notification.notify(title=title,message=message,timeout=time)

notification_on("Hey!!!","how r u????",10)