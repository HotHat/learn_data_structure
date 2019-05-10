// b_tree.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include "MyBTree.hpp"
#include <iostream>
#include <ctime>

int main()
{
    std::cout << "Hello World!\n"; 


	//tree.insert(120);
	//tree.insert(100);
	//tree.insert(50);

	//int arr[] = { 100, 50, 30, 500, 600, 500, 200, 200, 150, 300, 550, 580, 5, 28, 922, 82, 68, 182, 832, 234 };
	//int size = sizeof(arr) / sizeof(int);

	//for (int i = 0; i < size; ++i)
	//{
	//	tree.insert(arr[i]);
	//	tree.print();
	//}
	srand(time((time_t)0));
	

	MyBTree<int> tree(3);
	std::queue<int> q;

	for (int i = 120; i > 0; --i)
	{
		int n = rand() % 100;
		std::cout << n << " ";
		q.push(n);
		tree.insert(n);
	}
	std::cout << std::endl;

	tree.print();
	//tree.remove(10000);
	//int n = q.size() / 2;
	//for (int i = 0; i < n; ++i)
	//{
	//	int p = q.front();
	//	q.pop();
	//	std::cout << "delete: " << p << std::endl;
	//	tree.remove(p);
	//	tree.print();
	//}



}
