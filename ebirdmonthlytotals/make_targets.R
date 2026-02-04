library(tidyverse)

MAX_MISSING_MONTHS <- 2
MAX_MISSING_SECTIONS <- 4
INPUT_FILE <- '~/projects/seasonality/export-jason-Middlesex20251231.csv'
prefix <- "### "
month_section <- function(date) {
  day <- strtoi(str_sub(date, 9, 10), 10)
  if_else(day>15, "2", "1")
}
  
# pull in the records and grab just the name and half month section
birds <- read_csv(INPUT_FILE) |> 
  mutate(Common =  str_remove(Common, " \\(.+"), month = str_sub(Date, 6, 7), section = month_section(Date)) |>
  select(Common, month, section, Index)  |> 
  distinct()
birds <- birds[order(birds$Index),] # sort taxonomically
names <- birds |> select(Common) |> distinct()

# create tables with every section labeled unseen
biweekly_records <- data.frame(name = names,  c011 = c(0), c012 = c(0),
                               c021 = c(0), c022 = c(0), c031 = c(0), c032 = c(0),
                               c041 = c(0), c042 = c(0), c051 = c(0), c052 = c(0), 
                               c061 = c(0), c062= c(0), c071 = c(0), c072 = c(0), 
                               c081 = c(0), c082 = c(0), c091 = c(0), c092 = c(0), 
                               c101 = c(0), c102 = c(0), c111 = c(0), c112 = c(0), 
                               c121 = c(0), c122 = c(0))
monthly_records <- data.frame(name = names, c01 = c(0), c02 = c(0),
                              c03 = c(0), c04 = c(0), c05 = c(0), c06 = c(0),
                              c07 = c(0), c08 = c(0), c09 = c(0), c10 = c(0),
                              c11 = c(0), c12 = c(0))

# fill in the table for the birds/sections seen
for(b in 1:nrow(birds)) {
  m <- paste("c", birds[b, "month"], sep="")
  bw <- paste(m, birds[b, "section"], sep="")
  monthly_records[monthly_records$Common %in% birds[b, "Common"], m] <- 1
  biweekly_records[biweekly_records$Common %in% birds[b, "Common"], bw] <- 1
}

# add a column counting the number seen
mr <- monthly_records |> mutate(total_months = select(monthly_records, c01:c12) %>% rowSums(na.rm=TRUE))
br <- biweekly_records |> mutate(total_sections = select(biweekly_records, c011:c122) %>% rowSums(na.rm=TRUE))

# filter just the ones we want to output (ie only those within a few of complete)
missing_months <- mr |> filter(total_months>= (12-MAX_MISSING_MONTHS) & total_months<12)
missing_sections <- br |> filter(total_sections>= (24-MAX_MISSING_SECTIONS) & total_sections<24)

# print the monthly targets
months <- c("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
for(m in 1:length(months)) {
  message(prefix, months[m], ":")
  for(b in 1:nrow(missing_months)) {
    if(missing_months[b, (m+1)]==0) {
      message(paste0("* [ ] ", missing_months[b, 1], " (", 12-missing_months[b, 14], ")", sep=""))
    }
  }
  message("")
}

# print the half monthly targets
half_months <- c("Jan 1", "Jan 16", "Feb 1", "Feb 16", "Mar 1", "Mar 16", "Apr 1", "Apr 16", "May 1",
                "May 16", "Jun 1", "Jun 16", "Jul 1", "Jul 16", "Aug 1", "Aug 16", "Sep 1", "Sep 16",
                "Oct 1", "Oct 16", "Nov 1", "Nov 16", "Dec 1", "Dec 16")
for(h in 1:length(half_months)) {
  message(prefix, half_months[h],":")
  for(b in 1:nrow(missing_sections)) {
      if(missing_sections[b, (h+1)]==0) {
        message(paste0("* [ ] ",missing_sections[b, 1], " (", 24-missing_sections[b, 26], ")"))
      }
  }
  message("")
}

# function to print the birds seen before and after but not during a specified half month
process_gaps <- function(bs, section) {
  prev_section <- section - 1
  if(prev_section==0) { prev_section <- 24 } # handle Jan 1
  next_section <- section + 1
  if(next_section==25) { next_section <- 1 } # handle Dec 16
  for(b in 1:nrow(bs)) {
    if(bs[b, prev_section+1]==1 & bs[b, section+1]==0 & bs[b, next_section+1]==1) {
      message(paste0("* [ ] ",bs[b, 1]))
    }
  }
}

# and print the gaps
for(h in 1:length(half_months)) {
  message(prefix, half_months[h], ":")
  process_gaps(biweekly_records, h)
  message("")
}
