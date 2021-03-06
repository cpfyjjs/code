#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: 3.模块.py
@time: 18-9-6 下午5:31
@desc:
'''


import sys
import myclass


"""
先从sys.modules 查看是否已经被导入
如果没有被导入，就依据sys.path 路径寻找模块
找到就导入 ，没有报错
创建这个模块的命名空间
执行文件、把文件中的名字都放到命名空间里
"""

"""
内置模块
扩展模块，第三方模块
自己写的模块
"""


myclass.Vector()

print(sys.modules.keys())

# dict_keys(['builtins', 'sys', '_frozen_importlib', '_imp', '_warnings', '_thread', '_weakref', '_frozen_importlib_external', '_io', 'marshal', 'posix', 'zipimport', 'encodings', 'codecs', '_codecs', 'encodings.aliases', 'encodings.utf_8', '_signal', '__main__', 'encodings.latin_1', 'io', 'abc', '_weakrefset', 'site', 'os', 'errno', 'stat', '_stat', 'posixpath', 'genericpath', 'os.path', '_collections_abc', '_sitebuiltins', 'sysconfig', '_sysconfigdata_m_linux_x86_64-linux-gnu', '_bootlocale', '_locale', 'types', 'functools', '_functools', 'collections', 'operator', '_operator', 'keyword', 'heapq', '_heapq', 'itertools', 'reprlib', '_collections', 'weakref', 'collections.abc', 'importlib', 'importlib._bootstrap', 'importlib._bootstrap_external', 'warnings', 'importlib.util', 'importlib.abc', 'importlib.machinery', 'contextlib', 'mpl_toolkits', 'sphinxcontrib', 'sitecustomize', 'matplotlib', '__future__', 'six', 'struct', '_struct', 'atexit', 'distutils', 'distutils.version', 're', 'enum', 'sre_compile', '_sre', 'sre_parse', 'sre_constants', 'copyreg', 'distutils.sysconfig', 'distutils.errors', 'inspect', 'ast', '_ast', 'dis', 'opcode', '_opcode', 'linecache', 'tokenize', 'token', 'locale', 'logging', 'time', 'traceback', 'string', '_string', 'threading', 'shutil', 'fnmatch', 'zlib', 'bz2', '_compression', '_bz2', 'lzma', '_lzma', 'pwd', 'grp', 'tempfile', 'random', 'math', 'hashlib', '_hashlib', '_blake2', '_sha3', 'bisect', '_bisect', '_random', 'matplotlib.cbook', 'six.moves', 'datetime', '_datetime', 'glob', 'gzip', 'numbers', 'numpy', 'numpy._globals', 'numpy.__config__', 'numpy.version', 'numpy._import_tools', 'numpy.add_newdocs', 'numpy.lib', 'numpy.lib.info', 'numpy.lib.type_check', 'numpy.core', 'numpy.core.info', 'numpy.core.multiarray', 'numpy.core.umath', 'numpy.core._internal', 'numpy.compat', 'numpy.compat._inspect', 'numpy.compat.py3k', 'pathlib', 'ntpath', 'urllib', 'urllib.parse', 'ctypes', '_ctypes', 'ctypes._endian', 'numpy.core.numerictypes', 'numpy.core.numeric', 'pickle', '_compat_pickle', '_pickle', 'numpy.core.fromnumeric', 'numpy.core._methods', 'numpy.core.arrayprint', 'numpy.core.defchararray', 'numpy.core.records', 'numpy.core.memmap', 'numpy.core.function_base', 'numpy.core.machar', 'numpy.core.getlimits', 'numpy.core.shape_base', 'numpy.core.einsumfunc', 'numpy.testing', 'unittest', 'unittest.result', 'unittest.util', 'unittest.case', 'difflib', 'pprint', 'unittest.suite', 'unittest.loader', 'unittest.main', 'argparse', 'copy', 'textwrap', 'gettext', 'unittest.runner', 'unittest.signals', 'signal', 'numpy.testing.decorators', 'numpy.testing.nose_tools', 'numpy.testing.nose_tools.decorators', 'numpy.testing.nose_tools.utils', 'numpy.lib.utils', 'numpy.testing.nosetester', 'numpy.testing.nose_tools.nosetester', 'numpy.testing.utils', 'numpy.lib.ufunclike', 'numpy.lib.index_tricks', 'numpy.lib.function_base', 'numpy.lib.twodim_base', 'numpy.matrixlib', 'numpy.matrixlib.defmatrix', 'numpy.lib.stride_tricks', 'numpy.lib.mixins', 'numpy.lib.nanfunctions', 'numpy.lib.shape_base', 'numpy.lib.scimath', 'numpy.lib.polynomial', 'numpy.linalg', 'numpy.linalg.info', 'numpy.linalg.linalg', 'numpy.linalg.lapack_lite', 'numpy.linalg._umath_linalg', 'numpy.lib.arraysetops', 'numpy.lib.npyio', 'numpy.lib.format', 'numpy.lib._datasource', 'numpy.lib._iotools', 'numpy.lib.financial', 'decimal', '_decimal', 'numpy.lib.arrayterator', 'numpy.lib.arraypad', 'numpy.lib._version', 'numpy._distributor_init', 'numpy._mklinit', 'numpy.fft', 'numpy.fft.info', 'numpy.fft.fftpack', 'numpy.fft.fftpack_lite', 'numpy.fft.helper', 'mkl_fft', '_cython_0_27_3', 'cython_runtime', 'mkl_fft._pydfti', 'numpy.core.multiarray_tests', 'mkl_fft._numpy_fft', 'numpy.polynomial', 'numpy.polynomial.polynomial', 'numpy.polynomial.polyutils', 'numpy.polynomial._polybase', 'numpy.polynomial.chebyshev', 'numpy.polynomial.legendre', 'numpy.polynomial.hermite', 'numpy.polynomial.hermite_e', 'numpy.polynomial.laguerre', 'numpy.random', 'numpy.random.info', 'mtrand', 'numpy.random.mtrand', 'numpy.ctypeslib', 'numpy.ma', 'numpy.ma.core', 'numpy.ma.extras', 'matplotlib.cbook.deprecation', 'matplotlib.cbook._backports', 'matplotlib.compat', 'matplotlib.compat.subprocess', 'subprocess', '_posixsubprocess', 'select', 'selectors', 'matplotlib.rcsetup', 'matplotlib.testing', 'matplotlib.fontconfig_pattern', 'pyparsing', 'matplotlib.colors', 'matplotlib._color_data', 'cycler', 'six.moves.urllib', 'six.moves.urllib.request', 'urllib.request', 'base64', 'binascii', 'email', 'http', 'http.client', 'email.parser', 'email.feedparser', 'email.errors', 'email._policybase', 'email.header', 'email.quoprimime', 'email.base64mime', 'email.charset', 'email.encoders', 'quopri', 'email.utils', 'socket', '_socket', 'email._parseaddr', 'calendar', 'email.message', 'uu', 'email._encoded_words', 'email.iterators', 'ssl', 'ipaddress', '_ssl', 'urllib.error', 'urllib.response', 'matplotlib._version', 'json', 'json.decoder', 'json.scanner', '_json', 'json.encoder', 'dateutil', 'dateutil._version', 'myclass'])


