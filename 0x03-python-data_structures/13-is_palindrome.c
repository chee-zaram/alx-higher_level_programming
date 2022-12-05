#include "lists.h"

/**
 * is_palindrome - Checks for palindrome in listint_t singly linked list.
 * @head: Address of head pointer
 *
 * Return: 1 if list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = NULL;
	int *buff, beg, end, len = 0, idx = 0, reval = 0;

	if (head)
	{
		if (*head)
		{
			for (temp = *head; temp; temp = temp->next)
				len++;

			buff = malloc(sizeof(int) * len);
			if (!buff)
			{
				write(2, "Could not check list", 20);
				return (FAIL); /* should call exit() but not allowed */
			}

			for (temp = *head; temp; temp = temp->next)
				buff[idx++] = temp->n;
			beg = 0;
			end = idx - 1;
			reval = check_match(&buff[beg], &buff[end]);
			free(buff);
			if (!reval)
				return (NO_PAL);
		}
		return (PAL);
	}
	return (NO_PAL);
}

/**
 * check_match - Checks if integers in alternate positions in an address match
 * @big: Pointer to beginning address as at last function call.
 * @end: Pointer to ending address as at last function call.
 *
 * Return: Returns 0 if not matching, 1 if matching.
 */
int check_match(int *big, int *end)
{
	if (big < end)
	{
		if (*(big) == *(end))
			return (check_match(++big, --end));
		else
			return (0);
	}
	else
	{
		return (1);
	}
}
