source("_build/utils.R")

projectFolder <- file.path(".") 
buildFolder <- file.path("_build")
markupFolder <- file.path("_markup")
publishFolder <- file.path("_publish")
exportFolder <- file.path("_export")
renderFolder <- file.path("_render")
imagesFolder <- file.path("_var")

markup_filename <- "markup.Rds"
index_filename <- "index.qmd"
quarto_filename <- "_quarto.yml"

source("_build/preRender.R")
.encode(language ="EN")
.decode(language="EN")
.buildYAML(language="EN",output_format=c("docx","html"),output_dir=publishFolder)

OUTPUT_FORMAT <- "docx"
quarto::quarto_render(input = "index.qmd",output_format = OUTPUT_FORMAT)

OUTPUT_FORMAT <- "html"
quarto::quarto_render(input = "index.qmd",output_format = OUTPUT_FORMAT)

# OUTPUT_FORMAT <- "els-pdf"
# OUTPUT_FORMAT <- "revealjs"


source("_build/postRender.R")



