#include "Python.h"

/**
 * print_python_float - Function to print details on Python float object
 * @p: A Python object
 */
void print_python_float(PyObject *p)
{
	char *buf = NULL;
	PyFloatObject *fl_ob = (PyFloatObject *)p;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!strcmp(p->ob_type->tp_name, "float"))
	{
		buf = PyOS_double_to_string(fl_ob->ob_fval, 'r', 0,
				Py_DTSF_ADD_DOT_0, NULL);
		printf("  value: %s\n", buf);
		PyMem_Free(buf);
		return;
	}
	printf("  [ERROR] Invalid Float Object\n");
}

/**
 * print_python_bytes - Function to print details on Python byte object
 * @p: Python byte object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, idx;
	PyBytesObject *bytes_ob = (PyBytesObject *)p;

	fflush(stdout);
	printf("[.] bytes object info\n");

	if (!strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
		printf("  trying string: %s\n", bytes_ob->ob_sval);

		if (((PyVarObject *)p)->ob_size >= 10)
			size = 10;
		else
			size = ((PyVarObject *)p)->ob_size + 1;

		printf("  first %ld bytes: ", size);
		for (idx = 0; idx < size; ++idx)
		{
			printf("%02hhx", bytes_ob->ob_sval[idx]);
			if (idx == (size - 1))
				printf("\n");
			else
				printf(" ");
		}
		return;
	}
	printf("  [ERROR] Invalid Bytes Object\n");
}
/**
 * print_python_list - C function to print information on a Python List object
 * @p: A python object.
 */
void print_python_list(PyObject *p)
{
	PyVarObject *object = (PyVarObject *)p;
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size, alloc, idx;
	const char *type;

	size  = object->ob_size;
	alloc  = list->allocated;

	fflush(stdout);
	printf("[*] Python list info\n");

	if (!strcmp(p->ob_type->tp_name, "list"))
	{
		printf("[*] Size of the Python List = %ld\n", object->ob_size);
		printf("[*] Allocated = %ld\n", alloc);

		for (idx = 0; idx < size; ++idx)
		{
			type = list->ob_item[idx]->ob_type->tp_name;
			printf("Element %ld: %s\n", idx, type);

			if (!strcmp(type, "bytes"))
				print_python_bytes(list->ob_item[idx]);
			else if (!strcmp(type, "float"))
				print_python_float(list->ob_item[idx]);
		}
		return;
	}
	printf("  [ERROR] Invalid List Object\n");
}
