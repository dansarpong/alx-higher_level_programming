#include "lists.h"

/**
  * check_cycle - check if cycle is present in a loop
  * @list: pointer to head of node
  * Return: 1 if cycle is found, 0 otherwise
  */
int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	if (!list)
		return (0);

	first = list;
	second = list;
	
	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;

		if (first == second)
			return (1);
	}

	return (0);
}
