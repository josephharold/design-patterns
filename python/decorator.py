# When to use?
#



# notifier interface defines what methods should the classes include
# in this case notify()
class INotifier:
    def notify(self, message: str)->str:
        pass

# A Concrete Class that provide the default impl of the INotifier
class Notifier(INotifier):
    """
    concrete components provide the default implementation of the notifier
    """
    def notify(self, message)-> str:
        sent_message = f"sent on slack: {message}"
        return sent_message

# The main blueprint for the INotifiers' decorators
# still implements INotifier
class NotifDecorator(INotifier):
    # the wrapee
    _notifier: INotifier = None
    def __init__(self, notifier: INotifier):
        self._notifier = notifier

    @property
    def notifier(self)-> INotifier:
        return self._notifier
    def notify(self, message: str)->str:
        self._notifier.notify(message)


class EmailNotifDecorator(NotifDecorator):
    def notify(self, message: str)->str:
        sent_message = f"email sent: {message}"
        return self._notifier.notify(sent_message)

class SMSNotifDecorator(NotifDecorator):
    def notify(self, message: str)-> str:
        sent_message = f"sms sent: {message}"
        return self._notifier.notify(sent_message)



notifier = Notifier()
notifier = SMSNotifDecorator(EmailNotifDecorator(notifier))
print(notifier.notify("helloworld"))




