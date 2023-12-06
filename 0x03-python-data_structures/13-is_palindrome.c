#include <stdlib.h>
#include "lists.h"

/**
  * is_palindrome - checks if a singly linked list is a palindrome
  * @head: pointer to the head of the linked list
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */
int is_palindrome(listint_t **head)
{
	listint_t *check_a = *head, *check_b = *head, *check_c;
	int len = 0, hwDeep = 0, j;

	if (head == NULL || *head == NULL)
		return (1);

	while (check_b)
	{
		len++;
		check_b = check_b->next;
	}

	for (hwDeep = 1; hwDeep <= len / 2; hwDeep++)
	{
		check_c = check_a->next;
		check_b = check_a;
		for (j = 1; check_c; check_c = check_c->next)
		{
			if (j != hwDeep)
				j++;
			else
				check_b = check_b->next;
		}
		if (check_b->n != check_a->n)
			return (0);
		check_a = check_a->next;
	}

	return (1);
}
