#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int t;

	PyObjectList *obj = (PyObjectList *)p;

	printf("[*] Size of the Python List = %li\n", size);

	printf("[*] Allocated = %li\n", obj->allocated);

	for (t = 0; t < size; t++)

		printf("Element %i: %s\n", t, Py_TYPE(obj->ob_item[t])->tp_name);

}
