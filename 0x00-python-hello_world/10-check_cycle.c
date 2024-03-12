#include "lists.h"
#include <stdio.h>

/**
  * check_cycle - Function checks if a singly linked
  * list has a cycle in it
  * @list: The singly linked list to be checked
  *
  * Return: Returns 1 if it has a cycle in it or 0 if not
  */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list, *hare = list;
	int found_cycle = 0;

	while ((turtle && hare) && hare->next)
	{
		turtle = turtle->next;

		if (hare->next || hare->next->next)
			hare = hare->next->next;
		else
			break;

		if (turtle == hare)
		{
			found_cycle = 1;
			break;
		}
	}

	return (found_cycle);
}
