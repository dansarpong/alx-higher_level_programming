#include "lists.h"
#include <stdlib.h>

/**
  * insert_node - inserts a number into a sorted singly linked list
  * @head: pointer to the head of linked list
  * @number: number to be inserted
  * Return: pointer to the new node, NULL if it failed
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head, *prev, *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!head)
	{
		*head = new;
		return (new);
	}
	while (!tmp)
	{
		if (number >= tmp->n)
		{
			prev = tmp;
			tmp = tmp->next;
		}
	}
	if (!tmp)
	{
		prev->next = new;
		return (new);
	}
	new->next = tmp->next;
	tmp->next = new;
	return (new);
}
