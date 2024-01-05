#ifndef LISTS_H
#define LISTS_H
#include <stdio.h>
#include <stdlib.h>
/**
 * struct listint_s - linked list
 * @i: integer
 * @p: points to the next node
 *
 * Description: linked list project
 */
typedef struct listint_s
{
  int i;
  struct listint_s *p;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int i);
void free_listint(listint_t *head);
int is_palindrome(listint_t **head);

#endif /* LISTS_H */
