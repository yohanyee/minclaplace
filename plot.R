library(RMINC)

obj_file <- "/hpf/largeprojects/MICe/yyee/projects/Grandjean_cortical_recon/animal1/minclaplace_test_JGdata/rotated_surface.obj"
cfile <- "/hpf/largeprojects/MICe/yyee/projects/Grandjean_cortical_recon/animal1/minclaplace_test_JGdata/solved.txt"

objdata <- read_obj(obj_file)
objmesh <- create_mesh(objdata)

vertex_cols <- read.table(cfile, header = F)[,1]
cmap <- colour_mesh(objmesh, vertex_cols, symmetric = F, colour_range = c(0, 7000))
RMINC::obj_montage(objdata, objdata, vertex_cols, vertex_cols, palette = rainbow(255))
