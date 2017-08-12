def alias(name, function): #
      """Create an alias for a function."""
      exec("global %s; %s = function" % (name, name));
#



def send(*arguments): #
      """Send arguments to a function flexibly.
The last argument must be the function it's self."""

      from itertools import chain;

      function = arguments[-1];

      argument_list = [];
      
      for argument in arguments[:-1]: #

            if ((type(argument) is list) or type(argument) is tuple): #

                  for element in argument: #

                        argument_list.append(element);

                  #
                  
            #
            
            elif (type(argument) is dict): #

                  pass;

            #
            
            else: #

                  argument_list.append(argument);

            #

      #

      exec("print(function(%s))" % (argument_list));

#
                  
                  

      
