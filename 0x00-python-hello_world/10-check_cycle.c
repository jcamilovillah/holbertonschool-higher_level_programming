#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: list.
 * Return: 1 or 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *x, *z;

	x = list;
	player2 = list;

	while (x != NULL && z != NULL && z->next != NULL && x->next != NULL)
	{
		x = x->next;
		z = z->next->next;
		if (x == z)
		{
			return (1);
		}
	}
	return (0);
}
