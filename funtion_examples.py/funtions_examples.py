#learninng to use user defined funtions

#define a multiply funtion
def multiply(num1,num2,num3):
    product= num1 * num2 * num3
    print(product)

#define add funtion
def add(num1,num2,num3):
    result= num1 + num2 + num3
    print(result)


#define main funtion - all logic goes here
def main():
    #get input from the user 
    first_num=int(input("give me a number"))
    second_num=int(input("give me a number"))
    third_num=int(input("give me a number"))
    #call multiply function 
    multiply(first_num,second_num,third_num)

 #call add function 
    add(first_num,second_num,third_num)


#call the main funtion 
if __name__=="__main__":
    main()
