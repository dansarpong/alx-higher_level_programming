#include "lists.h"

/**
  * check_cycle - check if cycle is present in a loop
  * @list: pointer to head of node
  * Return: 1 if cycle is found, 0 otherwise
  */
int check_cycle(listint_t *list)
{
	listint_t *tmp = list;

	while (tmp)
	{
		tmp = tmp->next;
			if (tmp == list)
				return (1);
	}

	return (0);
}
