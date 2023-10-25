#include "lists.h"

/**
 * is_palindrome -> checks linked list
 *@head: A double pointer
 *Return: (1) <-||-> (0)
 */

int is_palindrome(listint_t **head)
{
	int check_palindrome = 1;
	listint_t *prev = NULL;
	listint_t *nnode;
	listint_t *sPtr = *head;
	listint_t *fPtr = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (check_palindrome);
	while (fPtr != NULL && fPtr->next != NULL)
	{
		fPtr = fPtr->next->next;
		nnode = sPtr;
		sPtr = sPtr->next;
		nnode->next = prev;
		prev = nnode;
	}

	if (fPtr != NULL)
		sPtr = sPtr->next;
	while (sPtr != NULL)
	{
		if (prev->n != sPtr->n)
		{
			check_palindrome = 0;
			break;
		}		prev = prev->next;
		sPtr = sPtr->next;
	} nnode = NULL;
	fPtr = prev;
	while (fPtr != NULL)
	{
		prev = fPtr->next;
		fPtr->next = nnode;
		nnode = fPtr;
		fPtr = prev;
	} *head = nnode;
	return (check_palindrome);
}
