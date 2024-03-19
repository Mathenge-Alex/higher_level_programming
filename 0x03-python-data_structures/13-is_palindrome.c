#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
* is_palindrome - Checks if a singly linked list is a palindrome
* @head: The head of the singly linked list
*
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *start = NULL, *end = NULL;
	unsigned int j = 0, len = 0, turn_len = 0, list_len = 0;

	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (1);

	start = *head;
	len = listint_len(start);
	turn_len = len * 2;
	list_len = turn_len - 2;
	end = *head;

	for (; j < turn_len; j = j + 2)
	{
		if (start[j].n != end[list_len].n)
			return (0);

		list_len = list_len - 2;
	}

	return (1);
}

/**
* get_nodeint_at_index - Gets a node from a linked list
* @head: The head of the linked list
* @index: The index to find in the linked list
*
* Return: The specific node of the linked list
*/
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *current = head;
	unsigned int iterations_cnt = 0;

	if (head)
	{
		while (current != NULL)
		{
			if (iterations_cnt == index)
				return (current);

			current = current->next;
			++iterations_cnt;
		}
	}

	return (NULL);
}

/**
* slistint_len - Counts the number of elements in a linked list
* @h: The linked list to count
*
* Return: Number of elements in the linked list
*/
size_t listint_len(const listint_t *h)
{
	int length = 0;

	while (h != NULL)
	{
		++length;
		h = h->next;
	}

	return (length);
}
