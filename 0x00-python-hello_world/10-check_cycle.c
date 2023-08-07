#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - check if linked list have a cycle or not
 * @list: head of the linked list
 * Return: 0 if not have a cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list || !list->next)
		return (0);

	slow = list->next;
	fast = list;

	while (slow)
	{
		while (fast != slow)
		{
			if (slow->next == fast)
			{
				return (1);
			}

			fast = fast->next;
		}

		slow = slow->next;
		fast = list;
	}

	return (0);
}
