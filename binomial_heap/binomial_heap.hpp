#pragma once
#include <boost/algorithm/string/join.hpp>
#include <boost/foreach.hpp>
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <cassert>
#include <stack>
#include <utility>

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

	std::pair<T, bool> GetMin()
	{
		auto r = FindMin();
		if (r.second)
		{
			return std::make_pair(r.first->value_, true);
		}
		else
		{
			return std::make_pair(T{}, false);
		}
	}

	void ExtractMin()
	{
		auto f = FindMin();

		if (!f.second)
		{
			return;
		}

		auto min = f.first;
		ExtractMinNode(min);
	}

	void Remove(T v)
	{
		auto p = Find(v);
		if (p == nullptr)
		{
			return;
		}

		auto min = BubbleUp(p, true);

		
		ExtractMinNode(min);
	}

	bool Decrease(T old, T target)
	{
		auto t = Find(old);
		if (t == nullptr)
		{
			return false;
		}

		t->value_ = target;

		BubbleUp(t, false);

		return true;

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

	BinomialHeapNode<T>* Find(T value)
	{
		if (root_ == nullptr)
		{
			return nullptr;
		}

		std::queue<BinomialHeapNode<T>*> q;
		auto s = GetSibling(root_);
		for (auto i : s)
		{
			q.push(i);
		}

		while (!s.empty())
		{
			auto n = q.front();
			q.pop();

			if (n->value_ == value)
			{
				return n;
			}
			else if (n->value_ < value)
			{
				auto c = GetSibling(n->child_);
				for (auto i : c)
				{
					q.push(i);
				}
			}
		}

		return nullptr;

	}

	std::pair<BinomialHeapNode<T> *, bool>FindMin()
	{
		auto r = root_;
		if (root_ == nullptr)
		{
			return std::make_pair(nullptr, false);
		}
		auto min = root_;

		while (r != nullptr)
		{
			if (r->value_ < min->value_)
			{
				min = r;
			}
			r = r->sibling_;
		}

		return std::make_pair(min, true);

	}
	std::pair<BinomialHeapNode<T> *, bool>FindPre(BinomialHeapNode<T> *s)
	{
		auto r = root_;
		if (root_ == nullptr)
		{
			return std::make_pair(nullptr, false);
		}

		while (r != nullptr && r->sibling_ != s)
		{
			r = r->sibling_;
		}

		return std::make_pair(r, true);

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

	BinomialHeapNode<T> *Reverse(BinomialHeapNode<T> *root)
	{
		std::stack<BinomialHeapNode<T>*> s;
		auto idx = root;
		while (idx != nullptr)
		{
			s.push(idx);
			idx = idx->sibling_;
		}
		
		if (s.empty())
		{
			return nullptr;
		}

		BinomialHeapNode<T> *r = s.top();
		s.pop();
		idx = r;

		while (!s.empty())
		{
			auto i = s.top();
			s.pop();

			idx->sibling_ = i;
			idx = i;
		}

		idx->sibling_ = nullptr;

		return r;

	}

	std::vector<BinomialHeapNode<T>*> GetSibling(BinomialHeapNode<T> *n)
	{
		std::vector<BinomialHeapNode<T>*> result;
		while (n != nullptr)
		{
			result.push_back(n);
			n = n->sibling_;
		}

		return result;
	}

	// if to top true bubble node to root
	BinomialHeapNode<T>* BubbleUp(BinomialHeapNode<T> *n, bool to_top)
	{
		if (to_top) {
			while (n->parent_ != nullptr)
			{
				auto f = n->parent_;
				auto tmp = f->value_;
				f->value_ = n->value_;
				n->value_ = tmp;
				n = f;

			}
		}
		else
		{
			while (n->parent_ != nullptr && n->value_ < n->parent_->value_)
			{
				auto f = n->parent_;
				auto tmp = f->value_;
				f->value_ = n->value_;
				n->value_ = tmp;
				n = f;

			}
		}

		
		return n;
	}

	void RemoveNode(BinomialHeapNode<T> *n)
	{
		assert(n != nullptr && "remove node must not nullptr");
		assert(n->parent_ == nullptr && "remove node must be root(have not parent) level");

		auto s = GetSibling(n->child_);

		for (auto i : s)
		{
			i->parent_ = nullptr;
		}

		delete n;
	}

	void ExtractMinNode(BinomialHeapNode<T> *min)
	{
		auto pre = FindPre(min);
		if (!pre.second)
		{
			return;
		}

		// min in the first position
		if (pre.first == nullptr)
		{
			root_ = min->sibling_;
		}
		else
		{
			pre.first->sibling_ = min->sibling_;
		}
		min->sibling_ = nullptr;

		auto c = min->child_;

		RemoveNode(min);

		auto r = Reverse(c);
		Union(root_, r);
	}
};
