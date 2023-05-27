library(dslabs)
data("murders")

murder_rate <- murders$total / murders$population * 100000

index <- murder_rate <= 0.71
murders$state[index]

west <- murders$region == "West"
safe <- murder_rate <= 1
index <- safe & west
murders$state[index]

index <- murders$state == "Massachusetts"
murder_rate[index]

index <- match(c("New York", "Florida", "Texas"), murders$state)
murder_rate[index]

c("Portland", "Las Vegas", "Arizona") %in% murders$state