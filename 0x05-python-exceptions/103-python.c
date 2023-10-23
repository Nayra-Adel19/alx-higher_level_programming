#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_bytes -> function -> give data
 *@p: the PyObject
 *Return: V successful
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t sizepy = 0, gg = 0;
	char *str = NULL;

	fflush(stdout);

	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;

	}	sizepy = PyBytes_Size(p);

	printf("  size: %zd\n", sizepy);
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", sizepy < 10 ? sizepy + 1 : 10);

	while (gg < sizepy + 1 && gg < 10)
	{
		printf(" %02hhx", str[gg]);

		gg++;

	}	printf("\n");
}

/**
 * print_python_float -> function -> give data
 *@p: the PyObject
 *Return: V successful
 */

void print_python_float(PyObject *p)
{
	fflush(stdout);

	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;

	}	char *str = NULL;

	str = PyOS_double_to_string
		(((PyFloatObject *)p)->ob_fval,'r', 0, Py_DTSF_ADD_DOT_0, NULL);

	printf("  value: %s\n", str);
}

/**
 * print_python_list -> function -> give data
 *@p: -> the PyObject
 *Return: V successful
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *opject;
	int b = 0;

	fflush(stdout);
	printf("[*] Python list info\n");

	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);

		printf("[*] Size of the Python List = %zd\n", size);

		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		while (b < size)
		{
			opject = PyList_GET_ITEM(p, b);
			printf("Element %d: %s\n", b, opject->ob_type->tp_name);

			if (PyBytes_Check(opject))
				print_python_bytes(opject);

			else if (PyFloat_Check(opject))
			{
				print_python_float(opject);
			}			b++;
		}
	}

	else
	{
		printf("  [ERROR] Invalid List Object\n");
	}
}
