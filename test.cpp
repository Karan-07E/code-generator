#include<iostream>
    using namespace std;
    
    int main(){
     int arr[] = {2, 4, 6, 8, 10};
     int n = sizeof(arr) / sizeof(arr[0]);

     int key = 8;
     bool found = false;

     int low = 0, high = n-1;
     while(low <= high){
        int mid = low + (high - low) / 2;
        if(arr[mid] == key){
            found = true;
            break;
        }
        else if(key > arr[mid]){
            low = mid + 1;
        }
        else{
            high = mid - 1;
        }
     }
     if (found) {
        cout << "Key " << key << " found in the array." << endl;
    } else {
        cout << "Key " << key << " not found in the array." << endl;
    }
    return 0;
  }