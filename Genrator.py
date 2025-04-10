#boilerplate code goes here

#define the boilerplate map
BOILERPLATE_MAP = {
    "sort":"""#include <iostream>
#include <algorithm> // For std::sort
using namespace std;

int main() {
    int arr[] = {10, 1, 0, -1, -2};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "The array before sort: " << endl;
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // Use pointers for sort
    sort(arr, arr + n);

    cout << "The sorted array: " << endl;
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
    }"""
}
def process_file(file_path):
    try:
        # Open the file and read its content
        with open(file_path, 'r+') as file:
            content = file.read()
            # Check for keywords and replace them with boilerplate
            for keyword, code in BOILERPLATE_MAP.items():
                if keyword in content:
                    content = content.replace(keyword, code)
                    print(f"////Replaced '{keyword}' with boilerplate code.////")
            # Write the updated content back to the file
            file.seek(0)
            file.write(content)
            file.truncate()
    except FileNotFoundError:
        print(f"////File {file_path} not found.////")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    cpp_file = input("////enter the cpp file to generate (include .cpp)////")
    process_file(cpp_file) #prompt the user for file