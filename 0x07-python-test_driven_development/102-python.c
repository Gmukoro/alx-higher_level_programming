#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_string - Prints information about a Python string object
 * @p: Pointer to the Python string object
 */
void print_python_string(PyObject *p)
{
    PyUnicodeObject *unicode;

    printf("[.] string object info\n");
    
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    unicode = (PyUnicodeObject *)p;

    printf("  type: %s\n", (PyUnicode_IS_COMPACT_ASCII(unicode)) ? "compact ascii" : "compact unicode object");
    printf("  length: %zd\n", PyUnicode_GET_LENGTH(unicode));
    printf("  value: %ls\n", PyUnicode_AS_UNICODE(unicode));
}

/**
 * main - Entry point for testing the print_python_string function
 * Return: Always 0
 */
int main(void)
{
    PyObject *s;

    s = PyUnicode_DecodeUTF8("The spoon does not exist", 24, NULL);
    print_python_string(s);
    Py_XDECREF(s);

    s = PyUnicode_DecodeUTF8("ложка не существует", 19, NULL);
    print_python_string(s);
    Py_XDECREF(s);

    s = PyUnicode_DecodeUTF8("La cuillère n'existe pas", 24, NULL);
    print_python_string(s);
    Py_XDECREF(s);

    s = PyUnicode_DecodeUTF8("勺子不存在", 5, NULL);
    print_python_string(s);
    Py_XDECREF(s);

    s = PyUnicode_DecodeUTF8("숟가락은 존재하지 않는다.", 14, NULL);
    print_python_string(s);
    Py_XDECREF(s);

    s = PyUnicode_DecodeUTF8("スプーンは存在しない", 10, NULL);
    print_python_string(s);
    Py_XDECREF(s);

    s = PyBytes_FromString("The spoon does not exist");
    print_python_string(s);
    Py_XDECREF(s);

    return 0;
}

