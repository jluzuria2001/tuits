## plotting the results in a blox plot

dat <- as.Date( c(
  "2017-03-04",
  "2017-03-05",
  "2017-03-06",
  "2017-03-07",
  "2017-03-08",
  "2017-03-09",
  "2017-03-10"))

tweets <- c(2317, 2108, 2332, 2296, 2295, 2144, 2187)

x <- rep(dat, tweets)
barplot(table(x),
        main="#elephant tweets in China",
        ylab="Count",
        border="red",
        col="blue",
        density=20,
        las=2
)


