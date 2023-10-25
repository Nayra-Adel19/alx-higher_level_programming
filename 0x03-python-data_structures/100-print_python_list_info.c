#include <Python.h>

/**
 * print_python_list_info - Prints list Python
 *@p: PyObj
 *Return: VOID
 */

void print_python_list_info(PyObject *p)
{
	int qq;

	PyListObject *objList = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", PyList_Size(p));

	printf("[*] Allocated = %li\n", objList->allocated);

	for (qq = 0; qq < PyList_Size(p); qq++)

		printf("Element %i: %s\n", qq, Py_TYPE(objList->ob_item[qq])->tp_name);

}
