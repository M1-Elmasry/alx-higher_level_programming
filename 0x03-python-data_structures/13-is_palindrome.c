#include "lists.h"

/**
 * list_to_arr - covert linked list to arr
 * @head: head of the linked list
 * @arr: the arr that will be filled with the values of the list
 * @buffer_size: preallocated memory to returned arr
 * Return: the length of the arr
 */
int list_to_arr(listint_t **head, int *arr, int buffer_size)
{
	int len;
	listint_t *curr = NULL;

	curr = *head;

	for (len = 0; curr != NULL; len++)
	{
		if (len == buffer_size - 1)
		{
			buffer_size *= 2;
			arr = realloc(arr, sizeof(int) * buffer_size);
		}

		arr[len] = curr->n;
		curr = curr->next;
	}

	return (len);
}

/**
 * is_palindrome - check if linked list is palindrome
 * @head: head of linked list
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	int ptr, n_list;
	int *arr = NULL, buffer_size = 16;

	arr = malloc(sizeof(int) * buffer_size);
	n_list = list_to_arr(head, arr, buffer_size);

	for (ptr = 0; ptr < n_list / 2; ptr++)
		if (arr[ptr] != arr[n_list - ptr - 1])
		{
			return (0);
		}

	return (1);
}
