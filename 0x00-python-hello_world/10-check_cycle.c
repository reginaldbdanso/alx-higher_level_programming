#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *temp, *current;

	temp = list;
	while (temp->next != NULL)
	{
		current = temp->next;
		while (current->next != NULL)
		{
			if(current == temp)
				return (1);
			current = current->next;
			/* temp = current->next; */
			/* current->next = head; */
		}
		temp = temp->next;
	}
	return (0);
}