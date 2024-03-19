#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>

/**
 * print_python_list_info - Function prints information
 * about a Python list object
 * @p: Pointer to the Python list object
 *
 * Function prints various information about
 * a Python list object, including its length,
 * allocated memory, and elements.
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

}
