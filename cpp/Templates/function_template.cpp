#include <bits/stdc++.h>
using namespace std;

//define template function 
template<typename T>
T temp_max (T a, T b){
    return b < a ? a : b;
}

int main (){
    int a = 1;
    int b = 23;
    cout << temp_max (a,b) << "\n";
}