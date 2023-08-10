#include "lists.h"

/**
* check_cycle - A program that checks if there is a loop in the linked list
* @list: The head node passed
* Return: 0 if no loop, 1 if loop.
*/

int check_cycle(listint_t *list)
{
	listint_t *speed1 = NULL;
	listint_t *speed2 = NULL;

	if (!list || !list->next)
		return (0);

	speed2 = list;
	speed1 = list->next;
	while (speed1 && speed1->next)
	{
		speed2 = speed2->next;
		speed1 = speed1->next->next;
		if (speed2 == speed1)
			return (1);
	}

	return (0);
}
