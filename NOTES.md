# The Time Calculator Challenge

This challenge could have been named the Modulo challenge becuase I used a lot
of modulo operations in my solution. Mod operations are one of my favorite CS
techniques because its such a neat trick to use. Modulo operations where helpful
in this challenge because we were dealing with clocks. Clocks start 12 and go
round until they get back to beginning and then they start again. 

For example, if it is currently 11 AM and we want to display the time that it will be four hours from
now in a 12 hour format, we can't simply add 11 + 4 because that would be 15.
Instead, we can use the mod operator:

```
>>> (11+4) % 12 
3
```
___note the parentheses above, I was bit a couple times from the order of
evaluation of the mod operator___


In the example, 3 is the hour we would expect because its the remainder of
dividing 15 by 12. That's all the mod operator does, but you can use this simple
operation to simplify many problems. 

This challenge did not only deal with whole hours, its also include minutes, a
count of days elapsed in a duration, and the new day name. I implemented all of
these features using modulo math! Let's briefly cover these solutions.

Dealing with minutes and duration was pretty straight forward. I created two
helper functions to convert the input string in 12 hour format to minutes and
back to 12 hour format. Once the start value and duration were both in minutes
it was a simple matter of adding the duration to the start to get the total time
elapsed. The trickier bit was getting how many days elapsed since start. We
could divide the duration, in minutes, by 24\*60, computing the quotient and
remainder to get the days and minutes in day, but python has a handy function to
do just this divmod().

If we have two inputs, start = "1:15 PM" and duration = "388:02" we can convert
both to minutes and use divmod() to get the quotient (days) and remainder
(minutes left in last day). 

```
# Midnight (12:00 AM) == 0
>>> start_in_minutes = 795
>>> duration_in_minutes = 23282
>>> new_time_in_minutes = 24077

>>> days, minutes = divmod(24077, 60*24)
>>> days
16
>>> minutes
1037

```

This conviently gives us 16 days elapsed since start and the remainder of 1037
minutes that we can covert back to the 12 hour format (5: 17 PM). 

The last way I used modulus math was to get the day of the week. The third
optional parameter pass to add_time() was a day name. Time elapsed was supposed
ot return an output with the new day name. This was not a clock, per se, but if
you stick the days of the week in an array, you can see that as you count
through the days you loop back to the beginning. For example if Friday is at
index 4, three days after Friday is Monday, or index 0. Approaching the days of
the week using an array or list data structure we can use the mod operator as
follows. 

```
>>> days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
          "Sunday"]

>>> start_day = "Friday"
>>> start_day_index = days[start_day] # 4
>>> days_elapsed = 3

>>> new_day_index = (start_day_index + days_elapsed) % 7

>>> days[new_day_index]
"Monday"
```

This example shows how to use the days of the week as a Python list and the mod
operator to wrap around the list to get the desired day. Another great use of
the mod operator!

This write-up covered a few ways to use modulo math to help simplify problems.
Remember, if you can model a problem kind of like a clock, as in you need to
wrap around a discrete number of options, the mod operator might be just the
tool you need. 
