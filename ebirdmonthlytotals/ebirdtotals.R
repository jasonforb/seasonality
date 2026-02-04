library(tidyverse)

is_exotic <- function(name) {
  exotics = c("Bar-headed Goose", "Graylag Goose", "Swan Goose", "Black Swan", "Whooper Swan", "Egyptian Goose", "Ruddy Shelduck", "South African Shelduck", "Muscovy Duck", "Mandarin Duck", "Yellow-billed Teal", "Baer's Pochard", "Helmeted Guineafowl", "California Quail", "Gambel's Quail", "Gray Partridge", "Golden Pheasant", "Lady Amherst's Pheasant", "Silver Pheasant", "Indian Peafowl", "Red Junglefowl", "Blue-breasted Quail", "Common Quail", "Japanese Quail", "Chukar", "African Collared-Dove", "Spotted Dove", "Diamond Dove", "Chilean Flamingo", "Cockatiel", "Sulphur-crested Cockatoo", "Budgerigar", "Rosy-faced Lovebird", "Monk Parakeet", "White-winged Parakeet", "White-fronted Amazon", "Nanday Parakeet", "Red-masked Parakeet", "Great Tit", "Red-whiskered Bulbul", "Northern Red Bishop", "White-winged Widowbird", "Zebra Finch", "Scaly-breasted Munia", "Chestnut Munia", "Orange-cheeked Waxbill", "Yellow-fronted Canary", "European Goldfinch", "Gray-crowned Goldfinch", "Island Canary", "Saffron Finch")
  name %in% exotics
}

count_this_month <- function(l, month) {
  w1 <- paste(month, "1", sep="")
  w2 <- paste(month, "2", sep="")
  w3 <- paste(month, "3", sep="")
  w4 <- paste(month, "4", sep="")
  s <- (l |> filter(.data[[w1]] > 0 | .data[[w2]]> 0 | .data[[w3]] > 0 | .data[[w4]] >0) |> count())
  paste(month, s)
}

f <- "~/Downloads/ebird_US-MA-017__1900_2025_1_12_barchart.txt"
birds <- read_tsv(f, c("bird", "Jan1", "Jan2", "Jan3", "Jan4", "Feb1", "Feb2", "Feb3", "Feb4", 
                       "Mar1", "Mar2", "Mar3", "Mar4", "Apr1", "Apr2", "Apr3", "Apr4", 
                       "May1", "May2", "May3", "May4", "Jun1", "Jun2", "Jun3", "Jun4",
                       "Jul1", "Jul2", "Jul3", "Jul4", "Aug1", "Aug2", "Aug3", "Aug4",
                       "Sep1", "Sep2", "Sep3", "Sep4", "Oct1", "Oct2", "Oct3", "Oct4",
                       "Nov1", "Nov2", "Nov3", "Nov4", "Dec1", "Dec2", "Dec3", "Dec4"), skip=16)
filtered_birds <- birds |> 
  filter(!grepl('hybrid', bird) & !grepl("/", bird) & !grepl('sp\\.', bird) & !is_exotic(bird))

count_this_month(filtered_birds, "Jan")
count_this_month(filtered_birds, "Feb")
count_this_month(filtered_birds, "Mar")
count_this_month(filtered_birds, "Apr")
count_this_month(filtered_birds, "May")
count_this_month(filtered_birds, "Jun")
count_this_month(filtered_birds, "Jul")
count_this_month(filtered_birds, "Aug")
count_this_month(filtered_birds, "Sep")
count_this_month(filtered_birds, "Oct")
count_this_month(filtered_birds, "Nov")
count_this_month(filtered_birds, "Dec")


