
install.packages("udpipe")

library(udpipe)
udmodel <- udpipe_download_model(language = "finnish")
udmodel <- udpipe_load_model(file = udmodel$file_model)
my_data <- read.delim("TXT_102.txt")
x <- udpipe_annotate(udmodel, x=my_data)
x <- as.data.frame(x)
x
x

View(x)
