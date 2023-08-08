#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert node on sorted linked list
 * head: pointer to the head of list
 * number: data of node
 * Return: pointer to inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *curr, *node, *temp;

  if (!head)
    return NULL;

  node = malloc(sizeof(listint_t));
  node->n = number;
  node->next = NULL;

  /* if the list is empty or the node is the smallest */
  if (!*head || (*head)->n >= node->n)
  {
    temp = *head;
    *head = node;
    node->next = temp;
    return (node);
  }
  
  curr = *head;

  while (curr->next)
  {
    if (curr->next->n >= node->n)
      break;

    curr = curr->next;
  }
  temp = curr->next;
  curr->next = node;
  node->next = temp;

  return node;
}
