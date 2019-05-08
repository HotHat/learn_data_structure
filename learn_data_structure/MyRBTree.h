#pragma once
#include <queue>
#include <iostream>
#include <assert.h>

enum class Color
{
	RED, BLACK
};


class Node
{
public:
	int val;
	Color color;
	Node *left, *right, *parent;


	Node(int val) : val(val)
	{
		left = right = parent = nullptr;
		color = Color::RED;
	}

	bool isLeft()
	{
		assert(parent != nullptr);

		return parent->left == this;
	}

	Node *sibling()
	{
		assert(parent != nullptr);

		if (isLeft())
		{
			return parent->right;
		}
		else
		{
			return parent->left;
		}
	}

	Node *uncle()
	{
		assert(parent != nullptr && parent->parent != nullptr);

		return parent->sibling();
	}

	bool isLeaf()
	{
		assert(this != nullptr);

		return this->left == nullptr && this->right == nullptr;
	}
};


class MyRBTree
{
public:
	MyRBTree();

	
	void insert(int val);
	Node *find(int val);
	void remove(int val);

	void printRecursive();
	~MyRBTree();

private:
	Node *root;

	Node *search(int val);
	Node *successor(Node *node);
	void leftRotate(Node *node);
	void rightRotate(Node *node);
	void swapColor(Node *l, Node *r);
	void swapValue(Node *l, Node *r);
	void flipColor(Node *node);
	void printRecursive(std::queue<Node *> q);
	void fixRotate(Node *node);
	void fixRemove(Node *node);

	void removeNode(Node *node);
};
