#include <Python.h>

/**
 * print_python_string - Prints Python strings
 * @p: Pointer to a PyObject
 */
void print_python_string(PyObject *p)
{
	PyObject *tempBytes = NULL;
	char *string = NULL;

	if (PyUnicode_Check(p))
	{
		tempBytes = PyUnicode_AsEncodedString(p, "utf-8", "strict");

		if (tempBytes != NULL)
		{
			string = PyBytes_AS_STRING(tempBytes);
			printf("[.] string object info\n"
				"  type: compact unicode object\n"
				"  length: %ld\n"
				"  value: %s\n", PyUnicode_GET_LENGTH(p), string);
			Py_DECREF(tempBytes);
		}
	}
	else if (PyBytes_Check(p))
	{
		string = PyBytes_AS_STRING(p);
		printf("[.] string object info\n"
			"  type: compact ascii\n"
			"  length: %ld\n"
			"  value: %s\n", PyBytes_GET_SIZE(p), string);
	}
	else
	{
		printf("[.] string object info\n  [ERROR] Invalid String Object\n");
	}
}
