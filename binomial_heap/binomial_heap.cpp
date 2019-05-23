#pragma once

template<class T>
class BinomialHeapNode
{
public:
	BinomialHeapNode(T v):
		m_degree(0),m_value(v),m_parent(nullptr),
		m_sibling(nullptr),m_child(nullptr)
	{
	}

	void print()
	{

	}

	template<class U> friend class BinomialHeap;

private:
	int m_degree;
	T m_value;
	BinomialHeap* m_parent, m_sibling, m_child;
};

template<class T>
class BinomialHeap
{
public:
	BinomialHeap():  m_root(nullptr)
	{ }
	

	void inert(T value)
	{

	}

	T GetMin()
	{

	}

	void extractMin()
	{

	}

	void remove(T v)
	{

	}

	void decrease(T old, T new)
	{

	}

private:
	BinomialHeapNode* m_root;

	BinomialHeapNode* find(T value)
	{

	}
	void link(const BinomialHeap<T>& h1, const BinomialHeap<T>& h2)
	{

	}
	void merge(const BinomialHeap<T>& h1, const BinomialHeap<T>& h2)
	{

	}
	void unionNode(const BinomialHeap<T>& h1, const BinomialHeap<T>& h2)
	{

	}
};
