// binomial_heap.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include "binomial_heap.cpp"

int main()
{
    BinomialHeap<int> heap;
	std::vector<int> v{ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

	for(auto i : v)
	{
		heap.Insert(i);
		heap.Print();
	}

}

