nclude <stdio.h>
#include <Python.h>
/**
 * print_python_bytes - A program that prints bytes information
 * @p: Python Object
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, t, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (t = 0; t < limit; t++)
		if (string[t] >= 0)
			printf(" %02x", string[t]);
		else
			printf(" %02x", 256 + string[t]);

	printf("\n");
}
/**
 * print_python_list - A funt that prints list information
 * @p: Python Object
 */
void print_python_list(PyObject *p)
{

	long int size, t;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (t = 0; t < size; t++)
	{
		obj = ((PyListObject *)p)->ob_item[t];
		printf("Element %ld: %s\n", t, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);

}
