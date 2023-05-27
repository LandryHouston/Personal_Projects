library(tidyverse)
library(dslabs)
data(temp_carbon)
data(greenhouse_gases)
data(historic_co2)

#carbon emissions based on min or max year

temp_carbon %>%
  filter(!is.na(carbon_emissions)) %>%
  .$year %>%
  min()

temp_carbon %>%
  filter(!is.na(carbon_emissions)) %>%
  .$year %>%
  max()

carbon1 <- temp_carbon %>%
  filter(year == 1751) %>%
  .$carbon_emissions

carbon2 <- temp_carbon %>%
  filter(year == 2014) %>%
  .$carbon_emissions

carbon2/carbon1


# global temperature based on first/last year


temp_carbon %>%
  filter(!is.na(temp_anomaly)) %>%
  .$year %>%
  min()

temp_carbon %>%
  filter(!is.na(temp_anomaly)) %>%
  .$year %>%
  max()

temp1 <- temp_carbon %>%
  filter(year == "1880") %>%
  .$temp_anomaly

temp2 <- temp_carbon %>%
  filter(year == "2018") %>%
  .$temp_anomaly

temp2 - temp1


temp_carbon %>%
  filter(!is.na(temp_anomaly)) %>%
  ggplot() +
  geom_line(aes(year, temp_anomaly), color = "red", linewidth = .7) +
  geom_line(aes(year, land_anomaly), color = "darkgreen", linewidth = .7) +
  geom_line(aes(year, ocean_anomaly), color = "blue", linewidth = .7) +
  geom_hline(aes(yintercept = 0), col = "black") +
  ylab("Temperature anomaly (degrees C)") +
  xlab("Year") +
  geom_text(aes(x = 2000, y = 0.05, label = "20th century mean"), col = "blue") +
  xlim(c(1880, 2018)) +
  ggtitle("Temperature anomaly relative to 20th century mean, 1880-2018")


greenhouse_gases %>%
  ggplot(aes(year, concentration)) +
  geom_line(linewidth = 1) +
  facet_grid(gas~., scales = "free") +
  geom_vline(xintercept = 1850, color = "blue", linewidth = 1) +
  xlab("Year") +
  ylab("Concentration (ch4/n2o ppb, co2 ppm)") +
  ggtitle("Atmospheric greenhouse gas concentration by year, 0-2000") +
  theme(plot.title = element_text(hjust = .5))


temp_carbon %>%
  filter(!is.na(carbon_emissions)) %>%
  ggplot(aes(year, carbon_emissions)) +
  geom_line(linewidth = 1) +
  ylab("Carbon emissions (metric tons)") +
  xlab("Year") +
  ggtitle("Annual global carbon emissions, 1751-2014 ")

