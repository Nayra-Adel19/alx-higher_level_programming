#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes -> print some basic
 *@p: Python Obj
*/


void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, oh, li;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;

	}	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);

	printf("  trying string: %s\n", str);

	if (size >= 10)
		li = 10;
	else
	{
		li = size + 1;

	}	printf("  first %ld bytes:", li);

	for (oh = 0;oh < li; oh++)

		if (str[oh] >= 0)
			printf(" %02x", str[oh]);
		else
		{
			printf(" %02x", 256 + str[oh]);

		}	printf("\n");
}

/**
 * print_python_list -> print basic info Python
 *@p: Python Obj
 */

void print_python_list(PyObject *p)
{
	long int size, pooh;

	PyListObject *lst;

	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;

	lst = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", lst->allocated);

	for (pooh = 0; pooh < size; pooh++)
	{
		obj = ((PyListObject *)p)->ob_item[pooh];

		printf("Element %ld: %s\n", pooh, ((obj)->ob_type)->tp_name);

		if (PyBytes_Check(obj))
		{
			print_python_bytes(obj);
		}
	}
}
