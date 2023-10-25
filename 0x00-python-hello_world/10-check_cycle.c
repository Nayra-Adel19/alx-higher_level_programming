#include "lists.h"


/**
 * check_cycle -> checks -> singly linked list has cycle
 *@list: refer -> arg (1)
 *Return: (0)-> is no cycle & (1)-> is cycle
 */


int check_cycle(listint_t *list)
{
	listint_t *qq = list, *d = list;

	if (list == NULL)
	{
		return (0);

	}	qq = list->next;

	d = list;

	while (qq != NULL && qq->next != NULL)
	{
		d = d->next;
		qq = qq->next->next;

		if (d == qq)

			return (1);

	}	return (0);
}
