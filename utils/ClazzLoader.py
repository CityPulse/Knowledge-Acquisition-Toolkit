import importlib

__author__ = 'frieder'


def loadClazz(mod_name, classname):
    module = importlib.import_module(mod_name)
    clazz = getattr(module, classname)
    return clazz
