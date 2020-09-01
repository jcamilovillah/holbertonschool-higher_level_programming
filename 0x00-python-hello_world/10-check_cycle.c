#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: list.
 * Return: 1 or 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *i, *j;

	player1 = list;
	player2 = list;

	while (player1 != NULL && player2 != NULL && player2->next != NULL && player1->next != NULL)
	{
		player1 = player1->next;
		player2 = player2->next->next;
		if (player1 == player2)
		{
			return (1);
		}
	}
	return (0);
}
