#include "lists.h"
#include <stdlib.h>

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
