"""Sufficiently advanced technology is indistinguishable from magic."""

# Note that this is intended to be more like art than actual programming.

# In this file, I install a new routine into my Neuralink's operating system.
# If this were real code, the outcome would be that my body and mind start the routine *automatically*...
# "Free will" be damned...
# Until I remove the code from the operating system.

from Neuralink import OperatingSystem, Routine

os = OperatingSystem()

# I'm gonna go for a walk, every day, for an hour, between the hours of 9 am and 4 pm, rain or shine.
# I know exactly where I'm gonna go, so there is no need to tell my Neuralink about it because
# I can just reference the trail.
days = {"Monday": True,
        "Tuesday": True,
        "Wednesday": True,
        "Thursday": True,
        "Friday": True,
        "Saturday": True,
        "Sunday": True}
time_limitation = {"after": 9, "before": 16}  # written in hours on the 24 hour clock

daily_walk = Routine("walk", days, 60, time_limitation)

os.install(daily_walk)

# Ok, so that's been established as the form for a routine. Let's see what else we can do with it...
work_days = {"Monday": True,
             "Tuesday": True,
             "Wednesday": True,
             "Thursday": True,
             "Friday": True,
             "Saturday": True,
             "Sunday": False}  # Even while working for yourself, it's important to take a break!

work_time_limit = {"after": 12, "before": 29}  # "5 am the following night" because I am a night-owl!

# Note the lack of a well defined schedule (like "after 12 but before 3 pm") doesn't matter for habit formation here
# as the Neuralink hardware will take care of it by sending the appropriate electrical signals to my brain.
work_habit = Routine("work", work_days, 180, work_time_limit)

# I wish the previous comment were true. I'd get so much work done!
os.install(work_habit)

# Now let's take care of our aesthetics by scheduling a monthly haircut!
# We'll pass something a little bit different to the "schedule" argument of the Routine.
haircut_schedule = {"monthly_schedule": [1, 15]}  # "occurs on the 1st and 15th"

haircut_time = {"at": 15}

haircut = Routine("haircut", haircut_schedule, 45, haircut_time)

os.install(haircut)
