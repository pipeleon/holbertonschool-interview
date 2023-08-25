#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/* Task 0 - Insert in sorted linked list  */

/**
 * insert_node - insert in sorted linked list
 * @head: Head of the list
 * @number: Number to add
 *
 * Return: pointer to a list_t
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;

	if ((*head)->n >= number)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		new->n = number;
		new->next = *head;
		*head = new;
	}
	else
		new = add_nodeint_end(&((*head)->next), n);

	return (new);
}