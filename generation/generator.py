"""
The code generator interface for upper device profile layer.
"""
import abc


class CodeGenerationInterface(object):
    @abc.abstractmethod
    def create(self):
        pass
