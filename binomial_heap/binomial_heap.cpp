#pragma once

template<class T>
class BinomialHeapNode
{
public:
	BinomialHeapNode(T v):
		degree_(0),value_(v),parent_(nullptr),
		sibling_(nullptr),child_(nullptr)
	{
	}

	void Print()
	{

	}

	template<class U> friend class BinomialHeap;

private:
	int degree_;
	T value_;
	BinomialHeapNode<T>* parent_, *sibling_, *child_;
};

template<class T>
class BinomialHeap
{
public:
	BinomialHeap():  root_(nullptr)
	{ }
	

	void Insert(T value)
	{
	    auto node = new BinomialHeapNode<T>(value);
        Union(root_, node);
	}

	T GetMin()
	{

	}

	void ExtractMin()
	{

	}

	void Remove(T v)
	{

	}

	void Decrease(T old, T target)
	{

	}

private:
	BinomialHeapNode<T>* root_;

	BinomialHeapNode<T>* find(T value)
	{

	}
	BinomialHeapNode<T> *Link(const BinomialHeapNode<T>* h1, const BinomialHeapNode<T>* h2)
	{

	}
	void Merge(const BinomialHeapNode<T>& h1, const BinomialHeapNode<T>* h2)
	{

	}
	void Fix(const BinomialHeapNode<T> &h)
    {

    }

	void Union(const BinomialHeapNode<T>* h1, const BinomialHeapNode<T>* h2)
	{
	   root_ =  Link(h1, h2);


	}
};
