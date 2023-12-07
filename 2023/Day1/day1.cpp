#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <unordered_map>    


int main() {
    std::ifstream file("data.txt");
    if (!file) {
        std::cerr << "Error opening file" << std::endl;
        return EXIT_FAILURE;
    }

    std::string line;
    int sum = 0;

    std::unordered_map<std::string, int> numbers = {
        {"one", 1}, {"two", 2}, {"three", 3},
        {"four", 4}, {"five", 5}, {"six", 6},
        {"seven", 7}, {"eight", 8}, {"nine", 9}
    };

    while (getline(file, line)) {
        int i = 0, front = -1, back = -1;

        while (line[i]) {

            if (isdigit(line[i])) {
                if(front == -1) {
                    front = line[i] - '0';
                }
                back = line[i] - '0';
            }

            for (int n = 0; n < numbers.size(); ++n) {
                for (auto number : numbers) {
                    int j = 0;

                    while (number.first[j]) {
                        if (i + j < line.size()) {
                            if (number.first[j] != line[i + j]) {
                                break;
                            }
                            if(j == number.first.size() - 1) {
                                if (front == -1) {
                                    front = number.second;
                                }
                                back = number.second;
                            }
                        }
                        ++j;
                    }
                }
            }
            ++i;
        }

        if (front != -1 && back != -1) {
            sum += (front * 10) + back;
        }
    }

    printf("Sum: %d\n", sum);

    return EXIT_SUCCESS;
}
