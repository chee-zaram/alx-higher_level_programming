#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_list_info - Display details on items in a list using PyObject
 * @list: List for which items' details should be displayed
 *
 * Description: Note that Python.h is provided by the Python build and contains
 * all the headers used in this file.
 */
void print_python_list_info(PyObject *list)
{
	PyObject *item;
	ssize_t listLen, listAlloc_d, idx;

	if (PyList_CheckExact(list))
	{
		listLen = PyList_Size(list);
		listAlloc_d = ((PyListObject *)list)->allocated;

		printf("[*] Size of the Python List = %lu\n", listLen);
		printf("[*] Allocated = %lu\n", listAlloc_d);
		for (idx = 0; idx < listLen; idx++)
		{
			item = PyList_GetItem(list, idx);
			printf("Element %lu: %s\n", idx, item->ob_type->tp_name);
		}
	}
}
