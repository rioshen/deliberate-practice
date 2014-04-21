//
//  main.cpp
//  usaco
//
//  Created by Ryo Shen on 4/17/14.
//  Copyright (c) 2014 Rio Shen. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

bool is_unique(char* p_content) {

    if (p_content == NULL || strlen(p_content) == 0) {
        return true;
    }

    bool table[256] = {false};
    for (int i = 0; i < strlen(p_content); i++) {
        int value = int(p_content[i]);
        if (table[value]) {
            return false;
        }
    }

    return true;
}

int main(int argc, const char * argv[]) {
    char my_char[] = "aabbc";
    cout << is_unique(my_char) << endl;
    return 0;
}

