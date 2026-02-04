library(tidyverse)

INPUT_FILE <- '~/projects/seasonality/export-jason-Middlesex20251231.csv'
MAX_MISSING_TOWNS = 5
MAX_MISSING_TWOTOWNS = 3

#TODO: command line args
DO_ALL = FALSE
DO_TWO_TOWNS = TRUE
prefix <- "### "

# pull in the records and grab just the name and town
birds <- read_csv(INPUT_FILE) |> 
  mutate(Common =  str_remove(Common, " \\(.+"), ) |>
  select(Common, City, Index)  |> 
  distinct()
birds <- na.omit(birds)
birds <- birds[order(birds$Index),] # sort taxanomically

names <- birds |> select(Common) |> distinct()
towns <- birds |> select(City) |> distinct()
towns <- towns[order(towns$City),]
# set up the table
mccc <- data.frame(matrix(nrow = nrow(names), ncol=nrow(towns)+1))
colnames(mccc) = c('Bird', sort(towns$City))
mccc$Bird = names$Common
for(t in 2:nrow(towns)+1) {
  mccc[,t] = 0
}
# fill in
for(b in 1:nrow(birds)) {
  bird <- birds[b,]$Common
  town <- birds[b,]$City
  mccc[which(names$Common %in% bird), which(towns$City %in% town)+1] = 1
}
# TODO: exporting mccc here without the header would replace the mccc python program

# add a column counting the number seen
# TODO: don't hardcode the first and last towns
mccc_wt <- mccc |> mutate(total_towns = select(mccc, Acton:Woburn) %>% rowSums(na.rm=TRUE))
if(DO_ALL) {
  # filter just the ones we want to output (ie only those within a few of complete)
  missing <- mccc_wt |> filter(total_towns>=(nrow(towns)-MAX_MISSING_TOWNS))
  
  # print the town targets
  for(t in 1:nrow(towns)) {
    not_used <- TRUE
    for(b in 1:nrow(missing)) {
      if(missing[b, t+1]==0) {
        if(not_used) {
          message(prefix, towns$City[t], ":")
          not_used <- FALSE
        }
  # TODO: hardcoded end
        message(paste0("* [ ] ", missing[b, 1], " (", nrow(towns)-missing[b, 56]), ")")
      }
    }
  }
}

if(DO_TWO_TOWNS) {
  TWO_TOWNS = c("Arlington", "Bedford", "Belmont", "Burlington", "Cambridge", "Concord",
              "Lexington", "Lincoln", "Newton", "Sudbury", "Waltham", "Watertown", "Wayland",
              "Weston", "Winchester", "Woburn")
  twotowns <- mccc |> select(any_of(c("Bird", TWO_TOWNS)))
  twotowns_wt <- twotowns |> mutate(total_towns=select(twotowns, Arlington:Woburn) %>% rowSums(na.rm=TRUE))
  twotowns_missing <- twotowns_wt |> filter(total_towns >= (length(TWO_TOWNS)-MAX_MISSING_TWOTOWNS))  
  for(t in 1:length(TWO_TOWNS)) {
    not_used <- TRUE
    for(b in 1:nrow(twotowns_missing)) {
      if(twotowns_missing[b, t+1]==0) {
        if(not_used) {
          message(prefix, TWO_TOWNS[t], ":")
          not_used <- FALSE
        }
        # TODO: hardcoded end
        message(paste0("* [ ] ", twotowns_missing[b, 1], " (", length(TWO_TOWNS)-twotowns_missing[b, 18]), ")")
      }
    }
  }
  almost <- twotowns_wt |> filter(total_towns==11 | total_towns==12)
  for(t in 1:nrow(almost)) {
    message(paste0("1. ", almost[t, 1], " (", 16-almost[t, 18], ")"))
  }
}
