# generate slides
library(yaml)
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

application <- read_yaml('config.yaml')
# add table to readme
readme <- readLines("slides.md")
write(readme, "assets/README_backup.md")

# detect where tables start & end
a <- which(startsWith(readme,"|") & !lag(startsWith(readme,"|")), arr.ind = TRUE)
readme[a] <- paste0("TABLE",c(1:length(a)))

readme <- readme[!startsWith(readme,"|")]

# https://stackoverflow.com/questions/48768173/replace-one-element-in-vector-with-multiple-elements
lst <- as.list(readme)
lst <- unlist(lapply(lst, function(x) if(x == "TABLE1") table1 else x))
lst <- unlist(lapply(lst, function(x) if(x == "TABLE2") table2 else x))

write(lst, "README.md")
message("Done")
