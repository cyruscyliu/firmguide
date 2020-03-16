import types
import logging


logger = logging.getLogger()


class Common(object):
    def set_attributes(self, attrs):
        if isinstance(attrs, list):
            for attr in attrs:
                self.__dict__[attr] = None
                self.__setattr__('set_'+attr, lambda x, a=attr: self.__dict__.__setitem__(a, x))
                self.__setattr__('get_'+attr, lambda a=attr: self.__dict__.__getitem__(a))
        elif isinstance(attrs, dict):
            for k, v in attrs.items():
                self.__dict__[k] = v

    def get_attributes(self):
        attrs = {}

        for k, v in self.__dict__.items():
            if isinstance(v, types.FunctionType):
                continue
            attrs[k] = v

        return attrs

    def info(self, action, message, status):
        logger.info(' - '.join([self.__class__.__name__, action, message, status]))

    def debug(self, action, message, status):
        logger.warning(' - '.join([self.__class__.__name__, action, message, status]))

    def warning(self, action, message, status):
        logger.debug(' - '.join([self.__class__.__name__, action, message, status]))

