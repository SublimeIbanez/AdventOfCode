#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

typedef struct {
    char* key;
    int value;
} Pair;


int main() {
    char *file_path = "data.txt";
    FILE *data = fopen(file_path, "r");
    if(!data) {
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    int sum = 0;
    char *line = NULL;
    size_t length = 0;
    ssize_t read;

    Pair nums[9] = {
        {"one", 1},
        {"two", 2},
        {"three", 3},
        {"four", 4},
        {"five", 5},
        {"six", 6},
        {"seven", 7},
        {"eight", 8},
        {"nine", 9}
    };
    

    while ((read = getline(&line, &length, data)) != -1) {
        int front = -1, back = -1;
        int i = 0;
        while(line[i] != '\0') {
            if(isdigit(line[i])) {
                if(front == -1) {
                    front = line[i] - '0';
                }
                back = line[i] - '0';
            }
            for(int p = 0; p < 9; ++p) {
                int j = 0;
                while(nums[p].key[j] != '\0') {
                    if(line[i + j] != nums[p].key[j]) {
                        break;
                    }
                    if(j == strlen(nums[p].key) - 1) {
                        if(front == -1) {
                            front = nums[p].value;
                        }
                        back = nums[p].value;
                    }
                    j++;
                }
            }
            i++;
        }
        if(front != -1 && back != -1) {
            sum += (front * 10) + back;
        }

        free(line);
        line = NULL;
    }
    fclose(data);
    if(line) {
        free(line);
        line = NULL;
    }

    printf("%d\n", sum);
    
    return EXIT_SUCCESS;
}
