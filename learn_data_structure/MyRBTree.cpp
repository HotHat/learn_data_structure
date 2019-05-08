#include "MyRBTree.h"


MyRBTree::MyRBTree()
{
	root = nullptr;
}




MyRBTree::~MyRBTree()
{
	if (root == nullptr)
		return;

	std::queue<Node *> q;
	Node *curr;

	q.push(root);

	while (!q.empty()) {
		// dequeue 
		curr = q.front();
		q.pop();

		if (curr->left != nullptr)
			q.push(curr->left);
		if (curr->right != nullptr)
			q.push(curr->right);
	}
	std::cout << "It's clean" << std::endl;
}


Node * MyRBTree::search(int val)
{
	Node *current = root;
	Node *next = root;


	while (next != nullptr)
	{
		current = next;

		if (current == nullptr || current->val == val) {
			return nullptr;
		}

		if (current->val > val)
		{
			next = current->left;
		}
		else if (current->val < val)
		{
			next = current->right;
		}


	}

	return current;
}

Node * MyRBTree::successor(Node * node)
{
	Node *next = node->right;

	while (next != nullptr && next->left != nullptr)
	{
		next = next->left;
	}

	return next;
}

void MyRBTree::insert(int val)
{
	Node *node = new Node(val);

	if (root == nullptr)
	{
		node->color = Color::BLACK;
		root = node;
		return;
	}

	Node *current = search(val);

	// find the value
	if (current == nullptr) return;

	// add node
	if (current->val > val)
	{
		current->left = node;
	}
	else
	{
		current->right = node;
	}

	node->parent = current;

	while (node != root)
	{
		if (node->parent->color == Color::BLACK)
		{
			return;
		}
		else
		{

			Node *uncle = node->uncle();

			Node *parent = node->parent;
			Node *pparent = parent->parent;

			if (uncle == nullptr || uncle->color == Color::BLACK)
			{


				if (parent->isLeft())
				{
					if (node->isLeft())
					{
						rightRotate(pparent);
						swapColor(pparent, parent);
					}
					else
					{
						leftRotate(parent);
						rightRotate(pparent);
						swapColor(pparent, node);
					}
				}
				else
				{
					if (node->isLeft())
					{
						rightRotate(parent);
						leftRotate(pparent);
						swapColor(pparent, node);
					}
					else
					{
						leftRotate(pparent);
						swapColor(pparent, parent);

					}
				}


				return;

			}
			else
			{
				flipColor(parent);
				flipColor(uncle);
				flipColor(pparent);

				if (root->color == Color::RED) {
					root->color = Color::BLACK;
				}
				node = pparent;
			}
		}


	}

	
}

Node * MyRBTree::find(int val)
{
	Node *next = root;

	while (next != nullptr)
	{

		if (next->val == val) {
			return next;
		}
		else if (next->val > val)
		{
			next = next->left;
		}
		else 
		{
			next = next->right;
		}

	}

	return nullptr;
}

void MyRBTree::remove(int val)
{
	Node *v = find(val);
	Node *u;

	
	while (v != nullptr)
	{
		if (v->isLeaf())
		{
			fixRemove(v);
			return;
		}
		else
		{
			u = successor(v);

			if (u != nullptr)
			{
				swapValue(u, v);

				if (u->isLeaf()) {
					fixRemove(u);
					return;
				}
				else
				{
					v = u;
				}
			}
			// left child not null and change
			else {
				swapValue(v, v->left);
				v = v->left;
			}
		}


	}
}


void MyRBTree::leftRotate(Node * node)
{
	Node *right = node->right;

	if (root == node)
	{
		root = right;
		right->parent = nullptr;
	}
	else
	{
		if (node->isLeft()) {
			node->parent->left = right;
		}
		else
		{
			node->parent->right = right;
		}

		right->parent = node->parent;
	}


	node->right = right->left;

	if (right->left != nullptr)
	{
		right->left->parent = node;
	}


	right->left = node;
	node->parent = right;

}

void MyRBTree::rightRotate(Node * node)
{
	Node *left = node->left;

	if (root == node)
	{
		root = left;
		left->parent = nullptr;
	} 
	else
	{
		if (node->isLeft())
		{
			node->parent->left = left;
		}
		else
		{
			node->parent->right= left;
		}
		left->parent = node->parent;
	}


	node->left = left->right;

	if (left->right != nullptr)
	{
		left->right->parent = node;
	}

	left->right = node;
	node->parent = left;

}

void MyRBTree::swapColor(Node * l, Node * r)
{
	assert(l != nullptr && r != nullptr);

	Color tmp = l->color;
	l->color = r->color;
	r->color = tmp;
}

void MyRBTree::swapValue(Node * l, Node * r)
{
	int tmp = l->val;
	l->val = r->val;
	r->val = tmp;
}

void MyRBTree::flipColor(Node * node)
{
	assert(node != nullptr);

	if (node->color == Color::RED)
	{
		node->color = Color::BLACK;
	}
	else
	{
		node->color = Color::RED;
	}
}

void MyRBTree::printRecursive(std::queue<Node*> q)
{
	Node* curr;
	std::queue<Node*> next;

	while (!q.empty()) {
		// while q is not empty 
		// dequeue 
		curr = q.front();
		q.pop();

		// empty tree
		if (curr == nullptr) return;

		// print node value 
		std::cout << "	" << curr->val << "[";

		if (curr->color == Color::RED)
			std::cout << "color=red]" << std::endl;
		else {
			std::cout << "color=black]" << std::endl;
		}

		// push children to queue 
		if (curr->left != NULL)
		{
			std::cout << "	" << curr->val << " -> " << curr->left->val << std::endl;
			next.push(curr->left);
		}
		if (curr->right != NULL)
		{
			std::cout << "	" << curr->val << " -> " << curr->right->val << std::endl;
			next.push(curr->right);
		}

	}
	std::cout << std::endl;
	if (!next.empty()) {
		printRecursive(next);
	}

}

void MyRBTree::printRecursive()
{
	std::cout << "strict digraph REDBLACKTREE { " << std::endl;
	std::queue<Node*> q;
	q.push(root);
	printRecursive(q);

	std::cout << "}" << std::endl;
}

void MyRBTree::fixRotate(Node * node)
{

}

void MyRBTree::fixRemove(Node * node)
{
	if (node == root)
	{
		root = nullptr;
		removeNode(node);
		return;
	}

	if (node->color == Color::RED)
	{
		removeNode(node);
		return;
	}

	Node *point = node;

	while (point != root)
	{
		Node *sibling = point->sibling();
		if (sibling->color == Color::BLACK)
		{
			// sibling has two black children
			if ((sibling->left == nullptr || sibling->left->color == Color::BLACK) && 
				(sibling->right == nullptr || sibling->right->color == Color::BLACK))
			{
				if (sibling->parent->color == Color::RED)
				{
					sibling->parent->color = Color::BLACK;
					sibling->color = Color::RED;
					break;
				}
				else
				{
					sibling->color = Color::RED;
					sibling->parent->color = Color::BLACK;
					// TODO: Continue with parent
					point = sibling->parent;
				}
			}
			// sibling has a lease one red chidren
			if (sibling->left != nullptr && sibling->left->color == Color::RED)
			{
			// Left Left
				if (sibling->isLeft())
				{
					sibling->left->color = Color::BLACK;
					swapColor(sibling, sibling->parent);
	
					rightRotate(point->parent);
				}
				// Left right
				else
				{
					swapColor(sibling, sibling->left);
					rightRotate(sibling);

					Node *s = point->sibling();
					s->right->color = Color::BLACK;
					swapColor(s, s->parent);
					
					leftRotate(point->parent);
				}

				break;
			}

			if (sibling->right != nullptr && sibling->right->color == Color::RED)
			{
				
				// right right
				if (!sibling->isLeft())
				{
					sibling->right->color = Color::BLACK;
					swapColor(sibling, sibling->parent);

					leftRotate(point->parent);
				}
				// right left
				else
				{
					swapColor(sibling, sibling->right);
					leftRotate(sibling);

					Node *s = point->sibling();
					s->left->color = Color::BLACK;
					swapColor(s, s->parent);
					rightRotate(point->parent);
				}
				break;
			}
		}
		else
		{

			swapColor(sibling->parent, sibling);

			if (sibling->isLeft())
			{
				rightRotate(sibling->parent);
			}
			else
			{
				leftRotate(sibling->parent);
			}


		}

	}


	removeNode(node);
	

}

void MyRBTree::removeNode(Node * node)
{
	assert(node != nullptr);

	if (node->parent == nullptr)
	{
		delete node;
		return;
	}

	if (node->isLeft())
	{
		node->parent->left = nullptr;
	}
	else
	{
		node->parent->right = nullptr;
	}
		
	delete node;
}
