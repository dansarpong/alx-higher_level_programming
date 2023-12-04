#include <stdlib.h>
#include "lists.h"

listint_t *create_rev_copy(listint_t *);

/**
  * is_palindrome - checks if a singly linked list is a palindrome
  * @head: pointer to the head of the linked list
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */
int is_palindrome(listint_t **head)
{
	listint_t *rev_copy = NULL, *check_a, *check_b;

	if (head == NULL || *head == NULL)
		return (1);

	rev_copy = create_rev_copy(*head);
	if (rev_copy == NULL)
		return (0);

	check_a = *head;
	check_b = rev_copy;
	while (check_a && check_b)
	{
		if (check_a->n != check_b->n)
		{
			free_listint(rev_copy);
			return (0);
		}
		check_a = check_a->next;
		check_b = check_b->next;
	}

	free_listint(rev_copy);
	return (1);
}

/**
  * create_rev_copy - create a copy of the linked list in reverse
  * @head: pointer to head of the original linked list
  * Return: pointer to the head of the new copy
  */
listint_t *create_rev_copy(listint_t *head)
{
	listint_t *new, *copy = NULL;

	if (!head)
		return (NULL);
	copy = create_rev_copy(head->next);
	new = add_nodeint_end(&copy, head->n);
	if (!new)
	{
		free_listint(copy);
		return (NULL);
	}

	return (copy);
}
