#include <Python.h>
#include <frameobject.h>

static PyFrameObject *
makeframe(PyFrameObject *back_frame, PyCodeObject *code, PyObject *globals, PyObject *locals)
{
    PyFrameObject *f;
    PyThreadState *t;
    t = malloc(sizeof(PyThreadState));
    t->frame = back_frame;
    /* This will incref on t->frame in a roundabout sort of way...
    It will hit all the other stuff, too. */
    f = PyFrame_New(t, code, globals, locals);
    free(t);
    return f;
}


static PyObject *
frame(PyObject *self, PyObject *args)
{
    PyFrameObject *back_frame;
    PyCodeObject *code;
    PyObject *globals;
    PyObject *locals;
    PyObject *ret;
    if (!PyArg_ParseTuple(args, "OO!O!O!", (PyObject *)&back_frame, &PyCode_Type, &code, &PyDict_Type, &globals, &PyDict_Type, &locals)){
        return NULL;
    }
    ret = (PyObject *)makeframe(back_frame, code, globals, locals);
    Py_XINCREF(ret);
    return ret;

}

PyDoc_STRVAR(frame_doc, "Make a frame!");


static PyMethodDef EvilFrameMethods[] = {
    {"frame", frame, METH_VARARGS, frame_doc},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef evilframemodule = {
    PyModuleDef_HEAD_INIT,
    "evilframe",
    NULL, /* docs are for wusses */
    -1, /*sate is for wusses too */
    EvilFrameMethods
};

PyMODINIT_FUNC
PyInit_evilframe(void)
{
    return PyModule_Create(&evilframemodule);
}
