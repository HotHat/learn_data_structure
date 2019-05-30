#pragma once
#include "binomial_heap.hpp"

struct DJKNode
{
	int number;
	int weight;

	DJKNode() :number(0), weight(0) {}
	DJKNode(int n, int w) :number(n), weight(w) {}
	bool operator<(const DJKNode& r)
	{
		return weight < r.weight;
	}
	bool operator<=(const DJKNode& r)
	{
		return weight <= r.weight;
	}
	bool operator==(const DJKNode& r)
	{
		return weight == r.weight;
	}
	bool operator>(const DJKNode& r)
	{
		return weight > r.weight;
	}

	friend std::ostream& operator<< (std::ostream& stream, const DJKNode& node)
	{
		stream << node.number << "_" << node.weight;
		return stream;
	}

};


class DJKHeap : public BinomialHeap<DJKNode>
{

protected:
	BinomialHeap<DJKNode>::BinomialHeapNode* Find(DJKNode value)
	{
		std::cout << "Hello warld" << std::endl;
		return nullptr;
	}
};