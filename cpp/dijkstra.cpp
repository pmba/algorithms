#include <stdio.h>
#include <iostream>

using namespace std;

typedef struct s_node node;

struct s_node
{
	int value;
	node* next;
}

node* create_graph()
{
	return NULL;
}

node* create_node(int value)
{
	node* newElement = malloc(sizeof(node));
	newElement->value = value;
	return newElement; 
}

node* add_vertex(node* head, int origin, int target)
{
	node* current = head;

	while (head->value != origin) {
		current = current->next;
	}

	if (current == NULL) {
		current = 
	}
}

void dijkstra(int s);

int main()
{


	return 0;
}

void dijkstra(int s)
{
	priority_queue<ii, vii, less<ii>> queue;

	distance[s] = 0;
	queue.push({distance[s], s});
}