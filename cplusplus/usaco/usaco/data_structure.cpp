//
//  data_structure.cpp
//  usaco
//
//  Created by Ryo Shen on 4/17/14.
//  Copyright (c) 2014 Rio Shen. All rights reserved.
//

#include "data_structure.h"
#include <queue>
#include <iostream>

using namespace std;

int main() {
    priority_queue<int> queue;

    for (int i = 0; i < 10; i++) {
        queue.push(i);
    }
    
    while (!queue.empty()) {
        cout << queue.top() << " ";
        queue.pop();
    }
}