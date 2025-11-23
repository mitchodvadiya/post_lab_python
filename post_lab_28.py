# post Lab 28
# ------------------------------------------------------------------------------------------------------

# code 1 : 
from plotnine import *
from plotnine.data import mtcars
print(mtcars.head())

# code 2 :
(ggplot(data=mtcars)
 + geom_point(mapping=aes(x="wt", y="mpg", color="factor(gear)"))
 + facet_wrap("~gear"))

# code 3 :
(ggplot(data=mtcars)
 + geom_point(aes("wt", "mpg", color="factor(gear)"))
)

# code 4 :
(ggplot(data=mtcars)
 + geom_point(aes("wt", "mpg", size="factor(gear)"))
)

# code 5 :
(ggplot(data=mtcars)
+ geom_point(aes("wt", "mpg"), color='red')
)

# code 6 :
from plotnine.data import economics

print(economics)

# code 7 :
from plotnine.data import economics
from plotnine import ggplot, aes, geom_line

(
    ggplot(economics)  # What data to use
    + aes(x="date", y="pop")  # What variable to use
    + geom_line()  # Geometric object to use for drawing
)

# code 8 :
from plotnine.data import mpg
from plotnine import ggplot, aes, geom_point

ggplot(mpg) + aes(x="class", y="hwy") + geom_point()



