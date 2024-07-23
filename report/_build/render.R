source("_build/utils.R")

projectFolder <- file.path(".") 
buildFolder <- file.path("_build")
markupFolder <- file.path("_markup")
publishFolder <- file.path("_publish")
exportFolder <- file.path("_export")
renderFolder <- file.path("_render")
markup_filename <- "markup.Rds"
index_filename <- "index.qmd"
quarto_filename <- "_quarto.yml"


source("_build/preRender.R")
.encode(language ="EN")
.decode(language="EN")
.buildYAML(language="EN",output_format=c("revealjs","html"),output_dir=publishFolder)

# quarto::quarto_render(input = "index.qmd",output_format = "html",execute_params=list(ext="png",render="none"))
quarto::quarto_render(input = "index.qmd",output_format = "revealjs",execute_params=list(ext="png",render="none"))
# quarto::quarto_render(input = "index.qmd",output_format = "els-pdf",execute_params=list(ext="png",render="none"))
# quarto::quarto_render(input = "index.qmd",output_format = "docx",execute_params=list(ext="png",render="none"))

source("_build/postRender.R")



