def replace(p, s, *args):

      """Replace each instance of a patern (p) in a string (s) with other corresponding items
         No flags"""

      
      
      args = list(args)

      s = list(s)

      

      for place, char in enumerate(s):

            if (char == p):

                  s[place] = args.pop(0)

      return ''.join(s)





      

def find(p, s, *args, pos1=0, pos2=0):

      """Return the first found position of a patern (p) in a string (s)
         [v] Additionaly prints a visual locator of (p)
         [c] Turns case senseitivity off
         [w] Treats (s) as a series of individual words"""

      v = True if ("v" in args) else False;

      c = True if ("c" in args) else False;

      w = True if ("w" in args) else False;


      
      if (c):

            p = p.lower();

            s = s.lower();

                        

      try:

            if (pos1 == len(p)):

                  return [pos2 - pos1, pos2];
                  
                  

            elif (p[pos1] == s[pos2]):

                  return find(p, s, pos1=pos1 + 1, pos2=pos2 + 1);

                  

            else:

                  return find(p, s, pos1=0, pos2=pos2 + 1);

            
                  
      except:

            return None;






      
def select(l, r, s, *args):

      """Return a section of a string (s) between two paterns -- left (l) and right (r) 
         [p] Treats (l) and (r) as index positions rather than locateble paterns"""     

      p = True if ("p" in args) else False;
      


      
      if (p):

           return s[l : r];

      

      else:

            return s[s.find(l) : s.find(r)];






def divide(p, s, *args):

      """Divide a string (s) into two strings, given a pivot (s)
         No flags"""

      return [s[ : p], s[p : ]];





      
def contents(p, *args):

      """Print the contents of a file from a path (p)
         [l] Shows line numbers
         [r] Returns the contents of the given file instead of printing it
         ....This allows for function pipelines"""
      
      l = True if ("l" in args) else False;

      r = True if ("r" in args) else False;

      

      path = open(p, "r");

      file = path.readlines();

      path.close();


      
      if (r):

            return "".join(file);

            

      else:
      
            for count, line in enumerate(file):

                  if (l):

                        print("{}\t{}".format(count, line), end="");

                        

                  else:
                              
                        print("{}".format(line), end="");





                        
def clean(p, t): pass;
