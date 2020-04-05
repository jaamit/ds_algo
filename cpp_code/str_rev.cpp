#include <iostream>
#include <string>

// regular loop
std::string str_rev_reg(std::string src) {
    std::string rev_str;
    for (int i = src.length()-1; i >= 0; i--) {
        rev_str.push_back(src[i]);
    }

    return rev_str;

}

// reverse iterator 
std::string str_rev_rit(std::string src) {
    std::string rev_str;
    for (std::string::reverse_iterator rit = src.rbegin(); rit != src.rend(); rit++) {
        rev_str.push_back(*rit);
        }

    return rev_str;
}


int main(){
    std::cout << str_rev_reg("hello world") << std::endl;

    std::cout << str_rev_rit("hello world") << std::endl;
    
    return 0;
}