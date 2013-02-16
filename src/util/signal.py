signal_subscriptions = {}


def subscribe(signal, function):
    if signal in signal_subscriptions:
        signal_subscriptions[signal].append(function)
    else:
        signal_subscriptions[signal] = [function]


def unsubscribe(signal, function):
    if signal in signal_subscriptions:
        if function in signal_subscriptions[signal]:
            signal_subscriptions[signal] = [f for f in signal_subscriptions[signal] if f != function]
            return True
    return False


def emit(signal, *args):
    if signal in signal_subscriptions:
        for f in signal_subscriptions[signal]:
            f(*args)
        return True
    else:
        return False


def peek(signal):
    return signal_subscriptions[signal]
