library(tidyverse)
library(dslabs)
data(stars)
options(digits = 3)   # report 3 significant digits


plot(stars$temp, stars$magnitude)

stars %>%
  ggplot(aes(temp, magnitude)) +
  geom_point() +
  scale_y_reverse()
  
stars %>%
  ggplot(aes(log10(temp), magnitude)) +
  geom_point() +
  scale_x_reverse() +
  scale_y_reverse() 

stars %>%
  ggplot(aes(temp, magnitude)) +
  geom_point() +
  scale_x_reverse() +
  scale_y_reverse() 


stars %>%
  ggplot(aes(temp, magnitude)) +
  geom_point(color = 'darkgrey') +
  scale_x_reverse() +
  scale_y_reverse() +
  geom_text(aes(label = star), check_overlap = TRUE, vjust = -1, size = 3, color = 'black')




stars %>%
  ggplot(aes(temp, magnitude, color = type)) +
  geom_point() +
  #scale_colour_manual(values = c("#000000", "#AAAAAA", "#0022BB", "#22BB00", "#CCCCCC", "#CC00CC", "#CCCC00", "#00CCCC", "#CC0000", "#888888")) +
  scale_x_reverse() +
  scale_y_reverse() +
  xlab("Temperature") +
  ylab("Magnitude") +
  geom_text(aes(label = star), check_overlap = TRUE, vjust = -1, size = 3, color = 'black')

