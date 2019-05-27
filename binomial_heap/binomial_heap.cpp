#pragma once
#include <boost/algorithm/string/join.hpp>
#include <boost/foreach.hpp>
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <cassert>

template<class T>
class BinomialHeapNode
{
public:
	BinomialHeapNode(T v):
		degree_(0),value_(v),parent_(nullptr),
		sibling_(nullptr),child_(nullptr)
	{
		sn_ = serial_number;
		serial_number += 1;
	}

	void Print()
	{
		std::queue<BinomialHeapNode<T>*> q;
		if (this != nullptr)
		{
			q.push(this);
		}

		while (!q.empty())
		{
			auto root = q.front();
			q.pop();
			auto idx = root;

			std::vector<std::string> s;

			while (idx != nullptr)
			{
				s.push_back(idx->Name());
				auto sb = idx->sibling_;

				if (sb != nullptr)
				{
					q.push(sb);
					if (idx->parent_ == nullptr)
					{
						std::cout << idx->Name() << " -> " << sb->Name() << std::endl;
					}
				}
				idx = sb; 
			}

			BOOST_FOREACH(std::string i, s)
			{
				std::cout << i << std::endl;
			}

			if (s.size() > 1)
			{
				std::cout << "{rank=same; " 
					<< boost::algorithm::join(s, " ") << " } " << std::endl;
			}

			auto c = root->child_;
			if (c != nullptr)
			{
				std::vector<std::string> s2;
				while (c != nullptr)
				{
					s2.push_back(c->Name());
					q.push(c);
					c = c->sibling_;
				}

				if (s2.size() > 1)
				{
					std::cout << "{rank=same; " 
						<< boost::algorithm::join(s2, " ") << " }" << std::endl;
				}
				BOOST_FOREACH(std::string i, s2)
				{
					std::cout << root->Name() << " -> " << i << std::endl;
				}
			}
		}
	}

	std::string Name()
	{
		std::string name;
		return name + "s" + std::to_string(sn_) + "_" + std::to_string(value_);
	}

	template<class U> friend class BinomialHeap;

private:
	int degree_;
	T value_;
	int sn_;
	BinomialHeapNode<T>* parent_, *sibling_, *child_;
	static int serial_number;
};

template<class T>
int BinomialHeapNode<T>::serial_number = 1;

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
	void Print()
	{
		std::cout << "strict digraph binomial_heap {" << std::endl;

		if (root_ != nullptr)
		{
			root_->Print();
		}

		std::cout << "}" << std::endl;
	}
private:
	BinomialHeapNode<T>* root_;

	BinomialHeapNode<T>* find(T value)
	{

	}
	BinomialHeapNode<T> *Link(BinomialHeapNode<T>* h1, BinomialHeapNode<T>* h2)
	{
		if (h1 == nullptr)
		{
			return h2;
		}

		if (h2 == nullptr)
		{
			return h1;
		}

		BinomialHeapNode<T>* root;
		if (h1->degree_ <= h2->degree_)
		{
			root = h1;
		}
		else
		{
			root = h2;
		}

		while (h1 != nullptr && h2 != nullptr)
		{
			if (h1->degree_ <= h2->degree_)
			{
				if (h1->degree_ == h2->degree_ || h1->sibling_ == nullptr || h1->sibling_->degree_ > h2->degree_)
				{
					auto tmp = h1->sibling_;
					h1->sibling_ = h2;
					h1 = h2;
					h2 = tmp;
				}
				else
				{
					h1 = h1->sibling_;
				}
			}
			else
			{
				auto tmp = h1;
				h1 = h2;
				h2 = tmp;
			}

		}

		return root;
	}
	void Merge(BinomialHeapNode<T>* h1, BinomialHeapNode<T>* h2)
	{
		assert(h1->degree_ == h2->degree_ && "Merge must have same degree");
		if (h1->value_ > h2->value_)
		{
			h1->sibling_ = h2->child_;
			h2->child_ = h1;
			h1->parent_ = h2;
			h1->degree_ += 1;
		}
		else
		{
			h2->sibling_ = h1->child_;
			h1->child_ = h2;
			h2->parent_ = h1;
			h1->degree_ += 1;
		}

	}
	void Fix(const BinomialHeapNode<T> &h)
    {

    }

	void Union(BinomialHeapNode<T>* h1, BinomialHeapNode<T>* h2)
	{
	   root_ =  Link(h1, h2);

	   auto x = root_;
	   auto f = x;

	   while (x != nullptr)
	   {
		   auto nxt = x->sibling_;
		   if (nxt == nullptr)
		   {
			   return;
		   }

		   if (nxt->sibling_ != nullptr && nxt->sibling_->degree_ == x->degree_)
		   {
			   x = nxt;
		   }
		   else if (x->degree_ == nxt->degree_)
		   {
			   if (x->value_ <= nxt->value_)
			   {
				   x->sibling_ = nxt->sibling_;
				   Merge(x, nxt);
			   }
			   else
			   {
				   if (x == root_)
				   {
					   root_ = nxt;
					   f = nxt;
				   }
				   else
				   {
					   f->sibling_ = nxt;
				   }
				   Merge(nxt, x);
				   x = nxt;
			   }

		   }
		   else
		   {
			   if (x != root_)
			   {
				   f = f->sibling_;
			   }
			   x = nxt;
		   }
	   }

	}
};
