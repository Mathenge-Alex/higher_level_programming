#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list - Prints basic info about Python lists.
* @p: PyObject list pointer.
*
* Return: Prints the size of the list its allocated space,
* and type of each element in the list, if @p is a valid PyListObject,
* or an error message.
*/

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_GET_SIZE(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GET_ITEM(p, i);

		printf("Element %zd: %s\n", i, item->ob_type->tp_name);
	}
}


/**
* print_python_bytes - Prints basic info about Python bytes objects.
* @p: PyObject bytes pointer.
*
* Description: Prints the size of the bytes object, its string
* representation, and the first up to 10 bytes of the bytes object,
* or otherwise an error message.
*/

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	char *trying_str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", trying_str);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);

	for (Py_ssize_t i = 0; i < size + 1 && i < 10; i++)
	{
		printf(" %02hhx", trying_str[i]);
	}
	printf("\n");
}


/**
* print_python_float - Prints basic info about Python float objects.
* @p: PyObject float pointer.
*
* Description: Prints the value of the float,
* or an error message if @p is not a valid PyFloatObject
*/

void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	double val = PyFloat_AsDouble(p);

	printf("[.] float object info\n");
	printf("  value: %f\n", val);
}
