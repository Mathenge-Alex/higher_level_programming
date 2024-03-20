#include "/usr/include/python3.4/Python.h"
#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: PyObject list pointer
 */
void print_python_list(PyObject *p)
{
	long int size = ((PyVarObject *)p)->ob_size;

	PyListObject *list = (PyListObject *)p;
	const char *type_name;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (Py_ssize_t i = 0; i < size; i++)
	{
		type_name = list->ob_item[i]->ob_type->tp_name;
		printf("Element %zd: %s\n", i, type_name);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: PyObject byte object pointer
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	long size = ((PyVarObject *)p)->ob_size;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);

	printf("  first %ld bytes: ", size < 10 ? size + 1 : 10);
	for (int i = 0; i < size + 1 && i < 10; i++)
	{

		printf("%02hhx ", bytes->ob_sval[i]);
	}
	printf("\n");
}
