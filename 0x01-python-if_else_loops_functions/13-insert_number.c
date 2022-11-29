#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Address of head pointer.
 * @number: Integer to insert in list.
 *
 * Return: The address of the new node, or NULL if failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL, *newNode = NULL, *tempNode = NULL;

	newNode = malloc(sizeof(*newNode));
	if (!newNode || !head)
	{
		if (newNode)
			free(newNode);
		return (NULL);
	}

	newNode->n = number;
	newNode->next = NULL;
	if (!*head)
	{
		*head = newNode;
		return (newNode);
	}

	if ((*head)->n > number)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}
	for (temp = *head; temp; temp = temp->next)
	{
		if (!temp->next)
		{
			temp->next = newNode;
			break;
		}
		if (temp->next->n > number)
		{
			tempNode = temp->next;
			temp->next = newNode;
			newNode->next = tempNode;
			return (newNode);
		}
	}
	return (newNode);
}

