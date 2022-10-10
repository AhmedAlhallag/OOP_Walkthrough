"""
[DEMO]: 
Side-effects

Additional readings:

Idempotence:

https://en.wikipedia.org/wiki/Side_effect_(computer_science)


"""

import data

data.stored_file_path = "anything!"


"""
Before the re-assignment by prepare_connection, 
the global has been changed! BEFORE EVEN I GOT TO "USE" THE READ FUNTION!

As developers, We will be given black-boxes all the time,
And it does not matter if we do not know how a certain fucntion is implemented

But what really matters is that we should be able to "control how to use" a certain function!

In this case, before i got even start "using" the read function,
a simple human mistake has shown that we do not have control on what the function does!
sometimes you need to be 100% sure that a function is doing what is intended to do
and not any EXTERNAL silly line/statement is able to CHANGE IT'S INNER WORKINGS!

The 101 of creating functions/methods:
is to make them as black-boxes (sandboxes) as much as possible!
taking certaing arguments, and 'returning' certain values


This is a very common issue with globals, thats why it is not advised to use them alot
especiially if we have begginer programmers on the team,
that would think by changing/adding certain globals, their problems are fixed just like that! (on some rare occasions this might be the case)  

Globals are module level variables; it can be "accessed and changed" by any part (module,class,block,function,statement) of your program

So why are globals bad?
The reason global variables are bad is that they enable functions to have hidden
(non-obvious, surprising, hard to detect, hard to diagnose) side effects, 
leading to an increase in complexity, potentially leading to Spaghetti code.
i.e.: Very briefly, it makes program state unpredictable.
[Specific Reasons]:
- no access control 
- no locality, no cohesion: 
you would not know after a while why each global you defined was used in your program unless you manually "trace" the entire control flow
- implicit coupling
- very hard to unit test
READ: http://wiki.c2.com/?GlobalVariablesAreBad


RULE OF THUMB:
Don't use global variables. 
If you think you need them it is usually a sign,
that your design is flawed.

How can we solve globals?
-> using return in functions 
-> using instance variables:
limit the SCOPE & ACCESS CONTROL in which the variable is coupled with,
instead of coupliing it to the global-state/namespace/module, 
narrow it down and couple it to an instance scope only 

"""

data.read("user.json")

"""
Additionally:

- everything seems fine with read  right? like whats the big deal, 
the global get re-assigned anways in read by the filename we send so all good

but what happen if we played with the global value again from outside of read and THEN:
WE CALLED WRITE WHICH DEPENEDS ON THE VALUE IOF THE GLOBAL TO BE CORRECTLY SET BY READ?
"""


data.stored_file_path = "new overwrite!!"


"""
Do you see an error? No?

Check your directory, do you see a file called 'new overwrite!!.txt'?

And here: THIS is what we mean by side-effects!
The worst logical errors you can ever have that is completely hard to debug!


"""

data.write(['a list'])