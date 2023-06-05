#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *temp, *current;

	current = temp = list;
	while (current->next != NULL)
	{
		current = current->next;
		if (current == temp)
			return (1);
	}
	return (0);
}