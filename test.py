With the increasing amount of data, one of
our many jobs as data scientists is to produce insights using visualizations. R is a very great tool for data visualization
and has different packages. Some of the popular and top data visualization tools
include: ggplot which used for data visualizations such as histograms, bar charts, scatterplots
etc. It allows adding layers and components on
a single visualization. Plotly is an R package can be used to create
web-based data visualizations that can be displayed or saved as individual HTML files. Lattice is a data visualization
tool that is used to implement complex, multi-variable data sets. Lattice is a high-level data visualization
library; it can handle many of the typical graphics without needing many customizations. And Leaflet is very useful in creating interactive
plots. Depending on your need and data science project,
most of these libraries and packages can come in handy. To install these packages in your R environment,
use the install dot packages and the package name command. R also has its own inbuilt functions to create
plots and visualization, it is mostly used using the plot function. For example, the function above is the simplest
form of the plot function and it returns a scatterplot of the values vs the index as
shown here. You can also add lines to the function and
add a title to make it easier to read and understand. Here we add a line to the plot and to add
a title. We specify the title function, and we can see we have added a line, and a title. We can create more beautiful visualizations
using the ggplot libraries. ggplot is a data visualization package for
R. It can handle complex requests allowing for
you to add layers into plots by tweaking the functions and arguments. To create a scatter plot, we will use the
inbuilt dataset Mtcars. We will first read ggplot library into memory
by using the library function and then call ggplot on the dataframe MTcars, specify the
X axis as miles per gallon and Y axis as weight, and then add the geom point function to specify
to ggplot that we want a scatter plot, otherwise it will return an empty plot. It will produce a more beautiful and easier
to read the plot like this You can also add titles and tweak the axis
name by using the ggtitle argument to add a title. And the labs argument to change the names
of the axis by specifying the new names we want to see. We will see an easier to read and understand
graph. In our lab we will be recreating the above
graphics with ggplot and the extension library called GGally. GGally extends ggplot2 by adding several functions
to reduce the complexity of combining geometric objects with transformed data. Please type and execute the following command
in the console window to install both packages. You will not need any coding experience as
the code and commands will be given to you. You are now familiar with:
Popular data visualization packages in R, plotting with Base R plot function,
plotting with ggplot, adding a title, and changing the axis name
using the ggtitle and labs function.