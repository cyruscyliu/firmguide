"""
install, clean, clean all interfaces
"""
import abc


class ExternalPackage(object):
    @abc.abstractmethod
    def install(self):
        """
        download, patch and install
        """
        pass

    @abc.abstractmethod
    def clean(self):
        """
        remove uncompressed dirs
        """
        pass

    @abc.abstractmethod
    def clear(self):
        """
        remove all files and dirs
        """
        pass

