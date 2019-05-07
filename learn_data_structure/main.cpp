// learn_data_structure.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include "MyRBTree.h"
#include <iostream>
#include <ctime>
#include <cstdlib>


int main()
{
	//std::cout << "Hello World" << std::endl;
	srand(time(0));

	MyRBTree tree;

	//for (int i = 100; i > 0; --i)
	//{
	//	int n = rand() % 100;
	//	//std::cout << n << " ";
	//	tree.insert(n);
	//}



	tree.insert(7);
	tree.insert(3);
	tree.insert(18);
	tree.insert(10);
	tree.insert(22);
	//tree.printRecurce();
	tree.insert(8);
	tree.insert(11);
	tree.insert(26);
	tree.insert(2);
	//tree.printRecurce();
	tree.insert(6);
	//tree.printRecurce();
	tree.insert(13);
	std::cout << std::endl;
	//tree.printRecurce();

	//std::cout << std::endl << "Deleting 18, 11, 3, 10, 22" << std::endl;

	tree.remove(18);
	tree.printRecurce();

	tree.remove(11);
	tree.printRecurce();

	tree.remove(3);
	tree.printRecurce();

	tree.remove(10);
	tree.printRecurce();

	tree.remove(22);
	tree.printRecurce();
	return 0;
}