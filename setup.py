from distutils.core import setup
import py2exe
import zmq
import os
import matplotlib

os.environ["PATH"] = \
    os.environ["PATH"] + \
    os.path.pathsep + os.path.split(zmq.__file__)[0]
setup(
    name='IAT',
    version='',
    packages=['logic', 'logic.dimreduce', 'logic.featurex','logic.preproc', 'logic.abstraction', 'utils', 'test', 'view'],
    url='',
    license='LGPL',
    author='frieder',
    author_email='F.Ganz@surrey.ac.uk',
    description='Information Abstraction Toolkit',
    console=['view/KATView.py']
    ,
    data_files=matplotlib.get_py2exe_datafiles(),
    options={
        "py2exe": {
            "includes":
                ["zmq.utils", "zmq.utils.jsonapi",
                 "zmq.utils.strtypes","matplotlib.backends.backend_tkagg","pysparse"]}}
)