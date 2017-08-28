# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_LSystem')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_LSystem')
    _LSystem = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_LSystem', [dirname(__file__)])
        except ImportError:
            import _LSystem
            return _LSystem
        try:
            _mod = imp.load_module('_LSystem', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _LSystem = swig_import_helper()
    del swig_import_helper
else:
    import _LSystem
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _LSystem.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _LSystem.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _LSystem.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _LSystem.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _LSystem.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _LSystem.SwigPyIterator_equal(self, x)

    def copy(self):
        return _LSystem.SwigPyIterator_copy(self)

    def next(self):
        return _LSystem.SwigPyIterator_next(self)

    def __next__(self):
        return _LSystem.SwigPyIterator___next__(self)

    def previous(self):
        return _LSystem.SwigPyIterator_previous(self)

    def advance(self, n):
        return _LSystem.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _LSystem.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _LSystem.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _LSystem.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _LSystem.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _LSystem.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _LSystem.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _LSystem.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class VecFloat(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VecFloat, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VecFloat, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _LSystem.VecFloat_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _LSystem.VecFloat___nonzero__(self)

    def __bool__(self):
        return _LSystem.VecFloat___bool__(self)

    def __len__(self):
        return _LSystem.VecFloat___len__(self)

    def __getslice__(self, i, j):
        return _LSystem.VecFloat___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _LSystem.VecFloat___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _LSystem.VecFloat___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _LSystem.VecFloat___delitem__(self, *args)

    def __getitem__(self, *args):
        return _LSystem.VecFloat___getitem__(self, *args)

    def __setitem__(self, *args):
        return _LSystem.VecFloat___setitem__(self, *args)

    def pop(self):
        return _LSystem.VecFloat_pop(self)

    def append(self, x):
        return _LSystem.VecFloat_append(self, x)

    def empty(self):
        return _LSystem.VecFloat_empty(self)

    def size(self):
        return _LSystem.VecFloat_size(self)

    def swap(self, v):
        return _LSystem.VecFloat_swap(self, v)

    def begin(self):
        return _LSystem.VecFloat_begin(self)

    def end(self):
        return _LSystem.VecFloat_end(self)

    def rbegin(self):
        return _LSystem.VecFloat_rbegin(self)

    def rend(self):
        return _LSystem.VecFloat_rend(self)

    def clear(self):
        return _LSystem.VecFloat_clear(self)

    def get_allocator(self):
        return _LSystem.VecFloat_get_allocator(self)

    def pop_back(self):
        return _LSystem.VecFloat_pop_back(self)

    def erase(self, *args):
        return _LSystem.VecFloat_erase(self, *args)

    def __init__(self, *args):
        this = _LSystem.new_VecFloat(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _LSystem.VecFloat_push_back(self, x)

    def front(self):
        return _LSystem.VecFloat_front(self)

    def back(self):
        return _LSystem.VecFloat_back(self)

    def assign(self, n, x):
        return _LSystem.VecFloat_assign(self, n, x)

    def resize(self, *args):
        return _LSystem.VecFloat_resize(self, *args)

    def insert(self, *args):
        return _LSystem.VecFloat_insert(self, *args)

    def reserve(self, n):
        return _LSystem.VecFloat_reserve(self, n)

    def capacity(self):
        return _LSystem.VecFloat_capacity(self)
    __swig_destroy__ = _LSystem.delete_VecFloat
    __del__ = lambda self: None
VecFloat_swigregister = _LSystem.VecFloat_swigregister
VecFloat_swigregister(VecFloat)

class VectorPyBranch(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorPyBranch, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorPyBranch, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _LSystem.VectorPyBranch_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _LSystem.VectorPyBranch___nonzero__(self)

    def __bool__(self):
        return _LSystem.VectorPyBranch___bool__(self)

    def __len__(self):
        return _LSystem.VectorPyBranch___len__(self)

    def __getslice__(self, i, j):
        return _LSystem.VectorPyBranch___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _LSystem.VectorPyBranch___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _LSystem.VectorPyBranch___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _LSystem.VectorPyBranch___delitem__(self, *args)

    def __getitem__(self, *args):
        return _LSystem.VectorPyBranch___getitem__(self, *args)

    def __setitem__(self, *args):
        return _LSystem.VectorPyBranch___setitem__(self, *args)

    def pop(self):
        return _LSystem.VectorPyBranch_pop(self)

    def append(self, x):
        return _LSystem.VectorPyBranch_append(self, x)

    def empty(self):
        return _LSystem.VectorPyBranch_empty(self)

    def size(self):
        return _LSystem.VectorPyBranch_size(self)

    def swap(self, v):
        return _LSystem.VectorPyBranch_swap(self, v)

    def begin(self):
        return _LSystem.VectorPyBranch_begin(self)

    def end(self):
        return _LSystem.VectorPyBranch_end(self)

    def rbegin(self):
        return _LSystem.VectorPyBranch_rbegin(self)

    def rend(self):
        return _LSystem.VectorPyBranch_rend(self)

    def clear(self):
        return _LSystem.VectorPyBranch_clear(self)

    def get_allocator(self):
        return _LSystem.VectorPyBranch_get_allocator(self)

    def pop_back(self):
        return _LSystem.VectorPyBranch_pop_back(self)

    def erase(self, *args):
        return _LSystem.VectorPyBranch_erase(self, *args)

    def __init__(self, *args):
        this = _LSystem.new_VectorPyBranch(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _LSystem.VectorPyBranch_push_back(self, x)

    def front(self):
        return _LSystem.VectorPyBranch_front(self)

    def back(self):
        return _LSystem.VectorPyBranch_back(self)

    def assign(self, n, x):
        return _LSystem.VectorPyBranch_assign(self, n, x)

    def resize(self, *args):
        return _LSystem.VectorPyBranch_resize(self, *args)

    def insert(self, *args):
        return _LSystem.VectorPyBranch_insert(self, *args)

    def reserve(self, n):
        return _LSystem.VectorPyBranch_reserve(self, n)

    def capacity(self):
        return _LSystem.VectorPyBranch_capacity(self)
    __swig_destroy__ = _LSystem.delete_VectorPyBranch
    __del__ = lambda self: None
VectorPyBranch_swigregister = _LSystem.VectorPyBranch_swigregister
VectorPyBranch_swigregister(VectorPyBranch)

class LSystem(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LSystem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LSystem, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _LSystem.new_LSystem()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _LSystem.delete_LSystem
    __del__ = lambda self: None

    def loadProgram(self, fileName):
        return _LSystem.LSystem_loadProgram(self, fileName)

    def loadProgramFromString(self, program):
        return _LSystem.LSystem_loadProgramFromString(self, program)

    def setDefaultAngle(self, degrees):
        return _LSystem.LSystem_setDefaultAngle(self, degrees)

    def setDefaultStep(self, distance):
        return _LSystem.LSystem_setDefaultStep(self, distance)

    def getDefaultAngle(self):
        return _LSystem.LSystem_getDefaultAngle(self)

    def getDefaultStep(self):
        return _LSystem.LSystem_getDefaultStep(self)

    def getGrammarString(self):
        return _LSystem.LSystem_getGrammarString(self)

    def getIteration(self, n):
        return _LSystem.LSystem_getIteration(self, n)

    def process(self, *args):
        return _LSystem.LSystem_process(self, *args)

    def processPy(self, n, branches, flowers):
        return _LSystem.LSystem_processPy(self, n, branches, flowers)
LSystem_swigregister = _LSystem.LSystem_swigregister
LSystem_swigregister(LSystem)

VX = _LSystem.VX
VY = _LSystem.VY
VZ = _LSystem.VZ
VW = _LSystem.VW
PA = _LSystem.PA
PB = _LSystem.PB
PC = _LSystem.PC
PD = _LSystem.PD
RED = _LSystem.RED
GREEN = _LSystem.GREEN
BLUE = _LSystem.BLUE
KA = _LSystem.KA
KD = _LSystem.KD
KS = _LSystem.KS
ES = _LSystem.ES
EPSILON = _LSystem.EPSILON
class vec2(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vec2, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vec2, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _LSystem.new_vec2(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __iadd__(self, v):
        return _LSystem.vec2___iadd__(self, v)

    def __isub__(self, v):
        return _LSystem.vec2___isub__(self, v)

    def __imul__(self, d):
        return _LSystem.vec2___imul__(self, d)

    def __itruediv__(self, *args):
        return _LSystem.vec2___itruediv__(self, *args)
    __idiv__ = __itruediv__



    def Length(self):
        return _LSystem.vec2_Length(self)

    def SqrLength(self):
        return _LSystem.vec2_SqrLength(self)

    def Normalize(self):
        return _LSystem.vec2_Normalize(self)
    __swig_destroy__ = _LSystem.delete_vec2
    __del__ = lambda self: None
vec2_swigregister = _LSystem.vec2_swigregister
vec2_swigregister(vec2)
cvar = _LSystem.cvar
M_PI = cvar.M_PI
M_PI_2 = cvar.M_PI_2
M2_PI = cvar.M2_PI
Rad2Deg = cvar.Rad2Deg
Deg2Rad = cvar.Deg2Rad

class vec3(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vec3, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vec3, name)
    __repr__ = _swig_repr
    __swig_setmethods__["n"] = _LSystem.vec3_n_set
    __swig_getmethods__["n"] = _LSystem.vec3_n_get
    if _newclass:
        n = _swig_property(_LSystem.vec3_n_get, _LSystem.vec3_n_set)

    def __init__(self, *args):
        this = _LSystem.new_vec3(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __iadd__(self, v):
        return _LSystem.vec3___iadd__(self, v)

    def __isub__(self, v):
        return _LSystem.vec3___isub__(self, v)

    def __imul__(self, d):
        return _LSystem.vec3___imul__(self, d)

    def __itruediv__(self, *args):
        return _LSystem.vec3___itruediv__(self, *args)
    __idiv__ = __itruediv__



    def set(self, x, y, z):
        return _LSystem.vec3_set(self, x, y, z)

    def Length(self):
        return _LSystem.vec3_Length(self)

    def SqrLength(self):
        return _LSystem.vec3_SqrLength(self)

    def Normalize(self):
        return _LSystem.vec3_Normalize(self)

    def Cross(self, v):
        return _LSystem.vec3_Cross(self, v)

    def Print(self, title):
        return _LSystem.vec3_Print(self, title)
    __swig_destroy__ = _LSystem.delete_vec3
    __del__ = lambda self: None
vec3_swigregister = _LSystem.vec3_swigregister
vec3_swigregister(vec3)

def Prod(*args):
    return _LSystem.Prod(*args)
Prod = _LSystem.Prod

def Dot(*args):
    return _LSystem.Dot(*args)
Dot = _LSystem.Dot

def Distance(a, b):
    return _LSystem.Distance(a, b)
Distance = _LSystem.Distance

def DistanceSqr(a, b):
    return _LSystem.DistanceSqr(a, b)
DistanceSqr = _LSystem.DistanceSqr

class vec4(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vec4, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vec4, name)
    __repr__ = _swig_repr
    __swig_setmethods__["n"] = _LSystem.vec4_n_set
    __swig_getmethods__["n"] = _LSystem.vec4_n_get
    if _newclass:
        n = _swig_property(_LSystem.vec4_n_get, _LSystem.vec4_n_set)

    def __init__(self, *args):
        this = _LSystem.new_vec4(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def set(self, x, y, z, w):
        return _LSystem.vec4_set(self, x, y, z, w)

    def Print(self, title):
        return _LSystem.vec4_Print(self, title)
    __swig_destroy__ = _LSystem.delete_vec4
    __del__ = lambda self: None
vec4_swigregister = _LSystem.vec4_swigregister
vec4_swigregister(vec4)
axisX = cvar.axisX
axisY = cvar.axisY
axisZ = cvar.axisZ
vec3Zero = cvar.vec3Zero

class matrix_error(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, matrix_error, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, matrix_error, name)
    __repr__ = _swig_repr

    def __init__(self, what_arg):
        this = _LSystem.new_matrix_error(what_arg)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _LSystem.delete_matrix_error
    __del__ = lambda self: None
matrix_error_swigregister = _LSystem.matrix_error_swigregister
matrix_error_swigregister(matrix_error)

# This file is compatible with both classic and new-style classes.

