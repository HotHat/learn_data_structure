// b_tree.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include "MyBTree.hpp"
#include <iostream>

int main()
{

	MyBTree<int> tree(3);

	int arr[] = { 86, 17, 14, 2, 23, 92, 29, 56, 88, 91, 38, 41, 2, 66, 12, 73, 66, 71, 17, 0 };
	int size = sizeof(arr) / sizeof(int);

	for (int i = 0; i < size; ++i)
	{
		std::cout << "Add item: " << arr[i] << std::endl;
		tree.insert(arr[i]);
	}
	tree.print();

	for (int i = 0; i < size; ++i)
	{
		std::cout << "Delete: " << arr[i] << std::endl;
		tree.remove(arr[i]);
		tree.print();
	}
	//srand(time((time_t)0));
	

	//MyBTree<int> tree(3);
	//std::queue<int> q;

	//for (int i = 20; i > 0; --i)
	//{
	//	int n = rand() % 100;
	//	std::cout << n << ", ";
	//	q.push(n);
	//	tree.insert(n);
	//}
	//std::cout << std::endl;
	//tree.print();

	//tree.print();
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
