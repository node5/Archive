class Queue(): #

      def __init__(self, size): #

            self.__maximum = size;

            self.__current = 0;
            
            self.__queue = [None for index in range(size)];

      #

      def __str__(self): #

            print(list(filter(lambda item: item != None, self.__queue)), end="");

            return "";

      #

      def __repr__(self): #

            print(list(filter(lambda item: item != None, self.__queue)), end="");

            return "";

      #
            
      def put(self, item): #

            if (self.__current + 1 <= self.__maximum): # 

                  self.__queue[self.__current] = item;

                  self.__current += 1;

            #

            else: #

                  return "Error! The queue is full";

            #

      #

      def pop(self): #

            first = self.__maximum - self.__current;

            self.__queue[first] = None;

            self.__current -= 1;

      #

      def clear(self): #

            self.__current = 0;

            self.__queue = [None for index in range(size)];

      #

#







class Stack(): #

      def __init__(self, size): #

            self.__maximum = size;

            self.__current = 0;
            
            self.__stack = [None for index in range(size)];

      #

      def __str__(self): #

            print(list(filter(lambda item: item != None, self.__stack)), end="");

            return "";

      #

      def __repr__(self): #

            print(list(filter(lambda item: item != None, self.__stack)), end="");

            return "";

      #
            
      def put(self, item): #

            if (self.__current + 1 <= self.__maximum): # 

                  self.__stack[self.__current] = item;

                  self.__current += 1;

            #

            else: #

                  return "Error! The queue is full";

            #

      #

      def pop(self): #

            self.__stack[self.__current - 1] = None;

            self.__current -= 1;

      #

      def clear(self): #

            self.__current = 0;

            self.__stack = [None for index in range(size)];

      #

#
