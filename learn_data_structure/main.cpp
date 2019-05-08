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

	MyRBTree tree;
	std::queue<int> q;

	for (int i = 20; i > 0; --i)
	{
		int n = rand() % 100;
		std::cout << n << " ";
		q.push(n);
		tree.insert(n);
	}
	std::cout << std::endl;

	tree.printRecurce();
	tree.remove(10000);
	int n = q.size() / 2;
	for (int i = 0; i < n; ++i)
	{
		int p = q.front();
		q.pop();
		std::cout << "delete: " << p << std::endl;
		tree.remove(p);
		tree.printRecurce();
	}

	//int arr[] = { 99, 91, 85, 92, 96, 48, 71, 44, 79, 28, 82, 32, 64, 10, 99, 51, 53, 50, 1, 23 };

	//int size = sizeof(arr) / sizeof(int);

	//for (int i = 0; i < size; ++i)
	//{
	//	tree.insert(arr[i]);
	//}

	//tree.printRecurce();
	//tree.remove(99);
	//tree.remove(91);
	//tree.remove(85);
	//tree.remove(92);
	//tree.remove(96);
	////tree.printRecurce();
	//tree.remove(48);
	////tree.printRecurce();
	//tree.remove(71);
	////tree.printRecurce();
	//tree.remove(44);
	//tree.remove(79);
	//tree.remove(28);
	//tree.remove(82);
	//tree.remove(32);
	//tree.remove(64);
	//tree.remove(10);
	//tree.remove(99);
	//tree.remove(51);
	//tree.remove(50);
	//tree.remove(53);
	//tree.remove(50);
	//tree.remove(1);
	//tree.printRecurce();
	//tree.remove(23);
	//tree.printRecurce();
	//tree.insert(98);
	//tree.insert(99);
	//tree.insert(64);
	//tree.insert(49);
	//tree.insert(55);
	//tree.insert(38);
	//tree.insert(84);
	//tree.insert(26);
	//tree.insert(25);
	//tree.insert(7);
	//tree.insert(5);
	//tree.insert(52);
	//tree.insert(46);
	//tree.insert(58);
	//tree.insert(86);
	//tree.insert(74);
	//tree.insert(46);
	//tree.insert(33);
	//tree.insert(68);
	//tree.insert(2);

	//tree.remove(98);

	return 0;
}