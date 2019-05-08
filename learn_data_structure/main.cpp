// learn_data_structure.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include "MyRBTree.h"
#include <iostream>
#include <queue>
#include <ctime>
#include <cstdlib>


int main()
{
	//std::cout << "Hello World" << std::endl;
	srand(time(0));
	{

		MyRBTree tree;
		std::queue<int> q;

		for (int i = 120; i > 0; --i)
		{
			int n = rand() % 100;
			std::cout << n << " ";
			q.push(n);
			tree.insert(n);
		}
		std::cout << std::endl;

		tree.printRecurce();
		//tree.remove(10000);
		int n = q.size() / 2;
		for (int i = 0; i < n; ++i)
		{
			int p = q.front();
			q.pop();
			std::cout << "delete: " << p << std::endl;
			tree.remove(p);
			tree.printRecurce();
		}
	}

	std::cout << "Well Done!" << std::endl;

	//int arr[] = { 99, 91, 85, 92, 96, 48, 71, 44, 79, 28, 82, 32, 64, 10, 99, 51, 53, 50, 1, 23 };

	//int size = sizeof(arr) / sizeof(int);

	//for (int i = 0; i < size; ++i)
	//{
	//	tree.insert(arr[i]);
	//}

	//tree.printRecurce();
	

	return 0;
}