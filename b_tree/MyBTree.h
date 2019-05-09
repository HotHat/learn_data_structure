#pragma once
#include <iostream>
#include <vector>

template<class T>
class BTreeNode
{
public:
	template<class T> friend class BTree;
	BTreeNode(int t)
	{
		_degree = t;
		_capacity = 0;
		_keys = new std::vector<T>;
		_children = new std::vector<BTreeNode *>;
		_parent = nullptr;
		_isLeaf = true;

	}
	~BTreeNode()
	{

	}

	void isFull()
	{
		return _capacity == _degree;
	}

	bool isLeaf()
	{
		return _isLeaf;
	}

	void setLeaf(bool t)
	{
		_isLeaf = t;
	}

	void insert(T value, BTreeNode *left, BTreeNode *right)
	{

		(*_keys).push_back(value);
		_capacity += 1;
		int idx = sortKey();

		if (left != nullptr)
		{
			(*_children)[idx] = left;
		}

		if (right != nullptr)
		{
			(*_children)[idx + 1] = right;
		}

	}

private:
	int _degree;
	int _capacity;
	bool _isLeaf;
	std::vector<T> *_keys;
	std::vector<BTreeNode *> *_children;
	BTreeNode *_parent;

	int sortKey()
	{
		int p = _capacity - 1;

		while (p > 0 && (*_keys)[p] < (*_keys)[p - 1])
		{
			T tmp = (*_keys)[p - 1];
			(*_keys)[p - 1] = (*_keys)[p];
			(*_keys)[p] = tmp;

			if (!isLeaf())
			{
				BTreeNode *c = (*_children)[p];
				(*_children)[p] = (*_children)[p + 1];
				(*_children)[p + 1] = c;
			}

			p -= 1;
		}

		return p;
	}
};

template<class T>
class MyBTree
{
public:
	MyBTree(int t)
	{
		_degree = t;
		_root = nullptr;

	}

	~MyBTree() {

	}

	void insert(T value)
	{
		if (_root == nullptr)
		{
			_root = new BTreeNode<int>(_degree);
			_root->insert(value, nullptr, nullptr);

		}
		else
		{

		}


	}

private:
	BTreeNode<T> *_root;
	int _degree;



};

