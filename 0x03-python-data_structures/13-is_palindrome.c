#include "lists.h"
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
/**
* is_palindrome - checkes if a list is palindrome
* @head: the begining of the list.
*
* Return: 1 if it is palindrome and 0 if not.
*/
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head, *prev_slow, *mid, *second_h, *first_h;
	int ispal = 1;

	if (*head == NULL || *(head)->next == NULL	)
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
	second_h = reverse_list(&slow);
	first_h = *head;
	while (second_h != NULL && first_h != NULL)
	{
		if (second_h->n != first_h->n)
		{
			ispal = 0;
			break;
		}
		second_h = second_h->next;
		first_h = first_h->next;
	}
	second_h = reverse_list(&slow);
	if (mid == NULL)
	{
		prev_slow->next = second_h;
	}
	else
	{
		prev_slow->next = mid;
		mid->next = second_h;
	}
	return (ispal);
}
