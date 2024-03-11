#include<stdio.h>

void print(int arr[], int s);
void insertion(int arr[], int s, int indx, int element);
void deletion(int arr[], int s, int indx);
void searching(int arr[], int s, int key);

int main(){
    
    int array[10],size;
    printf("Enter the size of the array:: ");
    scanf(" %d", &size);

    if(size > 10){
        printf("SORRY!! But the maximum limit is 10 only.\n");
    }
    else{
        printf("\nEnter the elements of the array:\n");
        
        for(int i=0;i<size;i++){
            printf("Element %d: ", i+1);
            scanf("%d",&array[i]);
        }
        // Printing the original array
        printf("\nThe Original Array is : \n");
        print(array, size);

        int option;
        printf("\nMenu\n");
        printf("\nA: Insert an Element at a specified position [Enter 1].");
        printf("\nB: Delete an Element from a specified position [Enter 2].");
        printf("\nC: Display the Array[Enter 3].");
        printf("\nD: Print the Array [Enter 4].");
        printf("\nE: Exit [Enter anything].");
        while (1)
        {
            printf("\n\n   Enter What You Want to Do: ");
            scanf("%d", &option);

            switch (option){
                case '1':
                    int index,element;
                    printf("\nEnter the index where you want to Insert the Element:: ");
                    scanf("%d", &index);

                    if(index <  0 || index >= size){
                        printf("Invalid Index! Please enter a valid Index between 0 and %d.", size-1);
                    }
                    else{
                        printf("\nEnter the Element that you want to Insert: ");
                        scanf("%d", &element);

                        insertion(array, size, index, element);
                    }
                    
                case '2':
                    int delIndex;
                    printf("\nEnter the INDEX of which Element you want to Delete: ");
                    scanf("%d", &delIndex);

                    if(delIndex < 0 || delIndex >= size) {
                        printf("Invalid Index! Please enter a valid Index between 0 and %d.\n", size - 1);
                    }
                    else{
                        deleteElement(array, size, delIndex);
                    }

                case '3':
                    int element;
                    printf("\nEnter the Element that you want to Insert: ");
                    scanf("%d", &element);

                    searchingt(array, size, element);
    
                case '4':
                    print(array, size);

                default :
                    printf("Thank you for using it.....")
                    break;

            }
        }
        
    }
}

void print(int  arr[], int s){
    printf("The array is : \n");
    for(int i=0; i<s; i++){
        printf("[%d]\t",arr[i]);
    }
}

void insertion(int arr[], int s, int indx, int element){

}

void deletion(int arr[], int s, int indx){

}

void searching(int arr[], int s, int key){

}