#ifndef LISTS_H
#define LISTS_H


#include <stdio.h>
#include <string.h>
#include <stdlib.h>


/**
 * struct listint_s - singly linked list
 *@n: int
 *@next: points to nnode
 *Description: singly linked list => node structure
 */


typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/* PROTOTYPY */


size_t print_listint(const listint_t *h);


void free_listint(listint_t *head);


int check_cycle(listint_t *list);


listint_t *add_nodeint(listint_t **head, const int n);


#endif
