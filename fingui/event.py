# Someday: Right now, subclasses need the exact same arguments their originals
#          took. It'd be nice if they did not...

from functools import wraps

def camelPrefix(prefix, original):
    return prefix + original[0].upper() + original[1:]

def eventSource(cls):
    methodsToAdd = {}
    for name, method in cls.__dict__.iteritems():
        if not getattr(method, 'bindable', False):
            continue
        # Create another method and add it to the class.
        def bindMethod(self, method):
            setattr(self, camelPrefix('bound', bindMethod.name), method)
        bindMethod.name = name
        methodsToAdd[camelPrefix('bind', name)] = bindMethod
        delattr(method, 'bindable')
    for name, method in methodsToAdd.iteritems():
        setattr(cls, name, method)
    return cls

def event(function):
    function.bindable = True
    name = function.__name__
    @wraps(function)
    def wrapped(self, *args, **kwargs):
        # Map arguments passed by position into kwargs.
        for argName, arg in zip(function.__code__.co_varnames[1:], args):
            kwargs[argName] = arg

        # Send the message to the instance.
        ret = sendMessage(function, self, **kwargs)

        # Send the message to the delegate, if it has one.
        if hasattr(self, 'delegate'):
            if hasattr(self.delegate, name):
                sendMessage(getattr(self.delegate, name), **kwargs)

        # Send the message to the bound companion, if it has one.
        boundName = camelPrefix('bound', name)
        if hasattr(self, boundName):
            sendMessage(getattr(self, boundName), **kwargs)
        return ret
    return wrapped

def sendMessage(function, *instance, **kwargs):
    code = function.__code__
    if code.co_flags & 0x08:  # Accepts arbitrary kwargs
        return function(*instance, **kwargs)
    return function(*instance, **{key: kwargs[key] for key in kwargs if key in code.co_varnames})