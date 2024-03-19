#include "lists.h"
#include <stddef.h>
/**
 * reverse_list - reverses a linked list.
 * @head: head of the linked list.
 *
 * Return: head of the new reversed linked list.
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *current = *head, *prev = NULL, *temp;

	while (current != NULL)
	{
		temp = current->next;
		current->next = prev;
		prev = current;
		current = temp;
	}
	return (prev);
}
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head, *prev_slow, *mid, *second_half, *first_half;
	int ispal = 1;

	if (*head == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}
	prev_slow->next = NULL;
	second_half = reverse_list(&slow);
	first_half = *head;
	while (second_half != NULL && first_half != NULL)
	{
		if (second_half->n != first_half->n)
		{
			ispal = 0;
			break;
		}
		second_half = second_half->next;
		first_half = first_half->next;
	}
	second_half = reverse_list(&slow);
	if (mid == NULL)
	{
		prev_slow->next = second_half;
	}
	else
	{
		prev_slow->next = mid;
		mid->next = second_half;
	}
	return (ispal);
}
