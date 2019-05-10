#pragma once
#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <cassert>

template<class T>
class BTreeNode
{
public:
	template<class U> friend class MyBTree;

	BTreeNode(int t) 
	{
		_degree = t;
		_capacity = 0;
		_parent = nullptr;
		_isLeaf = true;
		_sn = serial_number;
		serial_number += 1;
		_keys.resize(t);
		_children.resize(t + 1);
	}
	~BTreeNode()
	{

	}

	bool isFull()
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


	T middle()
	{
		int mid = 0;
		assert(isFull());

		if (_degree % 2 == 0)
		{
			mid = _degree / 2 - 1;
		}
		else
		{
			mid = _degree / 2;
		}

		return _keys[mid];
	}

	std::string name()
	{
		return std::string("node_") + std::to_string(_sn);
	}

	int findNext(T value)
	{
		for (int i = 0; i < _capacity; ++i)
		{
			if (value < _keys[i])
			{
				return i;
			}
		}

		return _capacity;
	}

	void print()
	{
		std::cout << "node_" << _sn;
		std::cout << "[label=\" ";
		for (int i = 0; i < _capacity; ++i)
		{
			std::cout << "<f" << (i * 2)  << ">| <f" << (i * 2 + 1) << ">" <<  _keys[i] << "|";
		}

		std::cout << "<f" << _capacity * 2 << ">\"]" << std::endl;
	}

	void insert(T value, BTreeNode *left, BTreeNode *right)
	{

		_keys[_capacity] = value;
		_capacity += 1;
		int idx = sortKey();

		if (left != nullptr)
		{
			_children[idx] = left;
			left->_parent = this;
		}

		if (right != nullptr)
		{
			_children[idx + 1] = right;
			right->_parent = this;
		}

	}

private:
	int _degree;
	int _capacity;
	bool _isLeaf;
	std::vector<T> _keys;
	std::vector<BTreeNode *> _children;
	BTreeNode *_parent;
	int _sn;

	static int serial_number;


	int sortKey()
	{
		int p = _capacity - 1;

		while (p > 0 && _keys[p] < _keys[p - 1])
		{
			T tmp = _keys[p - 1];
			_keys[p - 1] = _keys[p];
			_keys[p] = tmp;

			if (!isLeaf())
			{
				BTreeNode *c = _children[p];
				_children[p] = _children[p + 1];
				_children[p + 1] = c;
			}

			p -= 1;
		}

		return p;
	}
};

template<class T>
int BTreeNode<T>::serial_number = 1;


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
			_root = new BTreeNode<T>(_degree);
			_root->insert(value, nullptr, nullptr);
			return;
		}

		auto *p = _root;
		while (true)
		{
			

			if (p->isFull())
			{
				auto *parent = p->_parent;

				T mid = p->middle();
				auto *right = splite(p);

				if (parent == nullptr)
				{
					_root = new BTreeNode<T>(_degree);
					_root->insert(mid, p, right);
					_root->setLeaf(false);
					p = _root;
				}
				else
				{
					parent->insert(value, p, right);
					int idx = parent->findNext(mid);
					p = parent->_children[idx];
				}
			}
			else
			{
				if (p->isLeaf())
				{
					p->insert(value, nullptr, nullptr);
					return;
				}

				int idx = p->findNext(value);
				p = p->_children[idx];
			}
		}


	}


	BTreeNode<T> *splite(BTreeNode<T> *node)
	{
		assert(node->isFull());

		auto right = new BTreeNode<T>(_degree);
		right->setLeaf(node->isLeaf());

		int mid = 0;
		if (_degree % 2 == 0)
		{
			mid = _degree / 2 - 1;
		}
		else
		{
			mid = _degree / 2;
		}

		right->_capacity = mid;
		node->_capacity = mid;

		// copy right half content to right node
		int start = mid + 1;
		for (int i = 0; i < mid; ++i)
		{
			int m = i + start;
			right->_keys[i] = node->_keys[m];

			if (node->_children[m] != nullptr)
			{
				right->_children[i] = node->_children[m];
				node->_children[m]->_parent = right;
			}
		}

		// then last child
		if (node->_children[_degree])
		{
			right->_children[mid] = node->_children[_degree];
			node->_children[_degree]->_parent = right;
		}

		// erase right half content in left node
		node->_keys.erase(node->_keys.begin() + mid, node->_keys.begin() + node->_capacity) ;
		node->_children.erase(node->_children.begin() + mid + 1, node->_children.begin() + (node->_capacity + 1));

		return right;
	}

	void print()
	{
		if (_root == nullptr) return;

		std::cout << "digraph structs { node [shape=record]; " << std::endl;
		BTreeNode<T> *curr;
		std::queue<BTreeNode<T> *> q;

		q.push(_root);
		while (!q.empty()) {
			// while q is not empty 
			// dequeue 
			curr = q.front();
			q.pop();

			curr->print();
			std::string name = curr->name();

			for (int i = 0; i < curr->_capacity + 1; ++i)
			{
				BTreeNode<T> *c = curr->_children[i];
				if (c != nullptr)
				{
					std::cout << name << ":f" << 2 * i << " -> " << c->name() << std::endl;
					q.push(c);
				}
			}

		}
		std::cout << std::endl;

		std::cout << "}" << std::endl;
	}

private:
	BTreeNode<T> *_root;
	int _degree;


};

