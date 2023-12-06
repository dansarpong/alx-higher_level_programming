#include <stdlib.h>
#include "lists.h"

/**
  * reverse - reverse a linked list
  * @head: pointer to linked list to reverse
  * Return: pointer to reversed linked list
  */
listint_t *reverse(listint_t *head)
{
	listint_t *prev = NULL, *next = NULL;

	while (head != NULL)
	{
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}
	return (prev);
}

/**
  * compareLists - compare 2 linked lists
  * @head1: pointer to linked list to reverse
  * @head2: pointer to linked list to reverse
  * Return: 1 if identical, 0 if not
  */
int compareLists(listint_t *head1, listint_t *head2)
{
	while (head1 != NULL && head2 != NULL)
	{
		if (head1->n != head2->n)
			return (0);

		head1 = head1->next;
		head2 = head2->next;
	}

	if (head1 == NULL && head2 == NULL)
		return (1);

	return (0);
}

/**
  * is_palindrome - check if a linked list is a palindrome
  * @head: pointer to head of linked list
  * Return: 1 if palindrome, 0 if not
   */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *second_half, *prev_slow = NULL;
	int res = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
			slow = slow->next;

		second_half = slow;
		prev_slow->next = NULL;
		second_half = reverse(second_half);

		res = compareLists(*head, second_half);

		prev_slow->next = reverse(second_half);
	}
	return (res);
}
