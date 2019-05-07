#include "MyRBTree.h"


MyRBTree::MyRBTree()
{
	root = nullptr;
}




MyRBTree::~MyRBTree()
{
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
			delete v;
			return;
		}

		u = successor(v);

		if (u != nullptr)
		{
			swapValue(u, v);

			if (u->isLeaf()) {
				fixRemove(u);
				delete u;
				return;
			}
			else
			{
				v = u;
			}
		}
		else if (v->left != nullptr) {
			swapValue(u, v);
			v = u;
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

void MyRBTree::printRecurce(std::queue<Node*> q)
{
	Node* curr;
	std::queue<Node*> next;

	while (!q.empty()) {
		// while q is not empty 
		// dequeue 
		curr = q.front();
		q.pop();

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
		printRecurce(next);
	}

}

void MyRBTree::printRecurce()
{
	std::cout << "strict digraph REDBLACKTREE { " << std::endl;
	std::queue<Node*> q;
	q.push(root);
	printRecurce(q);

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
			if ((sibling->left == nullptr || sibling->left->color == Color::BLACK) ||
				(sibling->right == nullptr || sibling->right->color == Color::BLACK))
			{
				if (sibling->parent->color == Color::RED)
				{
					flipColor(sibling->parent);
					flipColor(sibling);
					removeNode(point);
					return;
				}
				else
				{
					flipColor(sibling);
					// TODO: Continue with parent
					point = sibling->parent;
				}
			}
		}
		else
		{
			if (sibling->isLeft())
			{
				leftRotate(sibling->parent);
			}
			else
			{
				rightRotate(sibling->parent);
			}
		}

	}

	

}

void MyRBTree::removeNode(Node * node)
{
	assert(node != nullptr && node->parent != nullptr);

	if (node->isLeft())
	{
		node->parent->left = nullptr;
	}
	else
	{
		node->parent->right = nullptr;
	}
}
