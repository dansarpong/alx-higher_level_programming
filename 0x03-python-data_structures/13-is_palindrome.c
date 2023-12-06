#include <stdlib.h>
#include "lists.h"

listint_t *copy_and_reverse(listint_t *head);

/**
  * is_palindrome - checks if a singly linked list is a palindrome
  * @head: pointer to the head of the linked list
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *second_half;
	int result;

	if (head == NULL || *head == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	/* Odd number of nodes */
	if (fast)
		slow = slow->next;

	second_half = copy_and_reverse(slow);

	while (second_half && (*head)->n == second_half->n)
	{
		*head = (*head)->next;
		second_half = second_half->next;
	}

	result = (second_half == NULL) ? 1 : 0;
	free_listint(second_half);
	return (result);
}

/**
  * copy_and_reverse - copy and reverse linked list
  * @head: pointer to head of linked list to be reversed
  * Return: pointer to reversed linked list
  */
listint_t *copy_and_reverse(listint_t *head)
{
	listint_t *prev = NULL, *current = NULL;

	while (head != NULL)
	{
		current = malloc(sizeof(listint_t));
		current->n = head->n;
		current->next = prev;
		prev = current;
		head = head->next;
	}

	return (prev);
}
