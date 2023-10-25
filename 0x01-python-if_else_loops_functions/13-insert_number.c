#include "lists.h"

/**
 * insert_node -> inserts number -> sorted singly linked list
 *@head: Head
 *@number: Number
 *Return: address of nnode || (NULL)-> failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nnood, *cunood;

	if (head == NULL)
	{
		return (NULL);

	}	nnood = malloc(sizeof(listint_t));

	if (nnood == NULL)
	{
		return (NULL);

	}	nnood->n = number;

	nnood->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		nnood->next = *head;
		*head = nnood;
		return (nnood);

	}	cunood = *head;

	while (cunood->next != NULL && cunood->next->n < number)
	{
		cunood = cunood->next;

	}	nnood->next = cunood->next;

	cunood->next = nnood;
	return (nnood);
}
