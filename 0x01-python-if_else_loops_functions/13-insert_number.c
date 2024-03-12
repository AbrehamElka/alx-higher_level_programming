#include <stdlib.h>
#include "lists.h"
/**
* insert_node - inserts a node with a specific number in a sorted linked list.
* @head: pointer to a pointer to the head of the linked list
* @number: the new number to be inserted
*
* Return: pointer to the new node, or NULL if it fails
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
	new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current = *head;
	while (current->next != NULL && current->next->n <= number)
	{
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}

