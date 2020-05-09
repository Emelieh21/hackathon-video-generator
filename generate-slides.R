# generate slides
library(yaml)
library(RCurl)
library(jsonlite)

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

# read in project config file
config <- read_yaml('config.yaml')

# get a random gif
search = unlist(config['objective_keyword'])
get <- getURL(paste0("http://api.giphy.com/v1/gifs/search?q=",search,"&api_key=",Sys.getenv("GIPHY_KEY"),"&limit=1"))
dat <- fromJSON(get)
url = paste0("https://media.giphy.com/media/",dat$data$id,"/giphy.gif")
download.file(url,'assets/giphy.gif', mode = 'wb')

# also, get a random nice thank you gif
search = 'thank+you'
get <- getURL(paste0("http://api.giphy.com/v1/gifs/search?q=",search,"&api_key=",Sys.getenv("GIPHY_KEY"),"&limit=1"))
dat <- fromJSON(get)
url = paste0("https://media.giphy.com/media/",dat$data$id,"/giphy.gif")
download.file(url,'assets/thank-you.gif', mode = 'wb')

# read in the template md
readme <- readLines("template.md")

# detect where tables start & end
readme <- gsub('PROJECT_NAME',config["name"], readme)
readme <- gsub('TEAM_NAME',config["team"], readme)
readme <- gsub('STEP_ONE',config$steps$step_one, readme)
readme <- gsub('STEP_TWO',config$steps$step_two, readme)
readme <- gsub('STEP_THREE',config$steps$step_three, readme)
readme <- gsub('ORGANIZERS',config$organizer, readme)

write(readme, "slides.md")
system('darkslide slides.md -i')
