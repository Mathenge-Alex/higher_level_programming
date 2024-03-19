#include "/usr/include/python3.10/Python.h"
#include "/usr/include/python3.10/listobject.h"
#include "/usr/include/python3.10/object.h"
#include <stdio.h>
#include <python3.10/object.h>

/*
* void print_python_list_info - Function prints some
* basic info about Python lists
* Return - Returns nothing
*/

void print_python_list_info(PyObject *p)
{
	int j = 0, list_len = 0;

	PyObject *item;
	PyListObject *clone = (PyListObject *) p;

	list_len = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", (int) clone->allocated);

	for (; j < list_len; ++j)
	{
		item = PyList_GET_ITEM(p, j);
		printf("Element %d: %s\n", j, item->ob_type->tp_name);
	}

	return;
}
